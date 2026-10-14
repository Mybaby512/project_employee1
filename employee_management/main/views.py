from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

from .models import Employee, UserProfile

from .forms import (
    EmployeeForm,
    RegisterForm,
    UserProfileForm,
)


# =========================================================
# ตรวจสอบสิทธิ์ Admin
# =========================================================

def is_admin(user):
    """
    ตรวจสอบสิทธิ์ Admin อย่างปลอดภัย
    """

    if not user.is_authenticated:
        return False

    # Superuser เป็น Admin
    if user.is_superuser:
        return True

    # ตรวจสอบ UserProfile
    try:
        profile = user.userprofile
    except UserProfile.DoesNotExist:
        return False

    return profile.role == "admin"


# =========================================================
# หน้าแรก / รายการพนักงาน
# =========================================================

@login_required(login_url="login")
def index(request):

    search_query = request.GET.get(
        "search",
        ""
    ).strip()

    employees_list = (
        Employee.objects
        .all()
        .order_by("-id")
    )

    # ค้นหาพนักงาน
    if search_query:
        employees_list = employees_list.filter(
            Q(name__icontains=search_query)
            | Q(position__icontains=search_query)
            | Q(department__icontains=search_query)
            | Q(phone__icontains=search_query)
            | Q(email__icontains=search_query)
        )

    # แบ่งหน้า
    paginator = Paginator(
        employees_list,
        5
    )

    page_number = request.GET.get(
        "page"
    )

    employees = paginator.get_page(
        page_number
    )

    return render(
        request,
        "index.html",
        {
            "employees": employees,
            "search": search_query,
        },
    )


# =========================================================
# ติดต่อเรา
# =========================================================

@login_required(login_url="login")
def contact_view(request):

    return render(
        request,
        "contact.html",
    )


# =========================================================
# สมัครสมาชิก
# =========================================================

def register_view(request):

    # ถ้า Login อยู่แล้ว
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":

        form = RegisterForm(
            request.POST
        )

        if form.is_valid():

            # User คนแรกของระบบเป็น Admin
            is_first_user = not User.objects.exists()

            user = form.save(
                commit=False
            )

            if is_first_user:

                user.is_staff = True
                user.is_superuser = True
                role = "admin"

            else:

                user.is_staff = False
                user.is_superuser = False
                role = "member"

            user.save()

            # สร้าง UserProfile
            UserProfile.objects.create(
                user=user,
                role=role,
            )

            messages.success(
                request,
                "สมัครสมาชิกสำเร็จ กรุณาเข้าสู่ระบบ",
            )

            return redirect(
                "login"
            )

    else:

        form = RegisterForm()

    return render(
        request,
        "register.html",
        {
            "form": form,
        },
    )


# =========================================================
# Login
# =========================================================

def login_view(request):

    # ถ้า Login อยู่แล้ว
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":

        form = AuthenticationForm(
            request,
            data=request.POST,
        )

        if form.is_valid():

            user = form.get_user()

            login(
                request,
                user,
            )

            # สร้าง UserProfile หากยังไม่มี
            UserProfile.objects.get_or_create(
                user=user,
                defaults={
                    "role": (
                        "admin"
                        if user.is_superuser
                        else "member"
                    ),
                },
            )

            messages.success(
                request,
                f"ยินดีต้อนรับ {user.username}",
            )

            return redirect(
                "index"
            )

        messages.error(
            request,
            "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง",
        )

    else:

        form = AuthenticationForm()

    return render(
        request,
        "login.html",
        {
            "form": form,
        },
    )


# =========================================================
# Logout
# =========================================================

@login_required(login_url="login")
def logout_view(request):

    logout(request)

    messages.info(
        request,
        "ออกจากระบบเรียบร้อยแล้ว",
    )

    return redirect(
        "login"
    )


# =========================================================
# Profile
# =========================================================

@login_required(login_url="login")
def profile_view(request):

    profile, created = (
        UserProfile.objects.get_or_create(
            user=request.user,
            defaults={
                "role": (
                    "admin"
                    if request.user.is_superuser
                    else "member"
                ),
            },
        )
    )

    if request.method == "POST":

        form = UserProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "แก้ไขโปรไฟล์สำเร็จ",
            )

            return redirect(
                "profile"
            )

    else:

        form = UserProfileForm(
            instance=profile
        )

    return render(
        request,
        "profile.html",
        {
            "form": form,
            "profile": profile,
        },
    )


# =========================================================
# เพิ่มพนักงาน
# =========================================================

@login_required(login_url="login")
def create_employee(request):

    if request.method == "POST":

        form = EmployeeForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            employee = form.save()

            messages.success(
                request,
                f"เพิ่มข้อมูลพนักงาน {employee.name} สำเร็จ",
            )

            return redirect(
                "index"
            )

    else:

        form = EmployeeForm()

    return render(
        request,
        "create_employee.html",
        {
            "form": form,
        },
    )


# =========================================================
# แก้ไขพนักงาน
# =========================================================

@login_required(login_url="login")
def edit_employee(request, pk):

    employee = get_object_or_404(
        Employee,
        pk=pk,
    )

    if request.method == "POST":

        form = EmployeeForm(
            request.POST,
            request.FILES,
            instance=employee,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "แก้ไขข้อมูลพนักงานสำเร็จ",
            )

            return redirect(
                "index"
            )

    else:

        form = EmployeeForm(
            instance=employee
        )

    return render(
        request,
        "edit.html",
        {
            "form": form,
            "employee": employee,
        },
    )


# =========================================================
# ลบพนักงาน
# =========================================================

@login_required(login_url="login")
def delete_employee(request, pk):

    employee = get_object_or_404(
        Employee,
        pk=pk,
    )

    if request.method == "POST":

        employee_name = employee.name

        employee.delete()

        messages.success(
            request,
            f"ลบข้อมูลพนักงาน {employee_name} สำเร็จ",
        )

        return redirect(
            "index"
        )

    return render(
        request,
        "delete_employee.html",
        {
            "employee": employee,
        },
    )


# =========================================================
# Admin Dashboard
# =========================================================

@login_required(login_url="login")
@user_passes_test(
    is_admin,
    login_url="index",
)
def admin_dashboard(request):

    users = (
        User.objects
        .select_related("userprofile")
        .all()
        .order_by("-date_joined")
    )

    total_users = users.count()

    total_employees = Employee.objects.count()

    total_admins = UserProfile.objects.filter(
        role="admin"
    ).count()

    total_members = UserProfile.objects.filter(
        role="member"
    ).count()

    return render(
        request,
        "admin_dashboard.html",
        {
            "users": users,
            "total_users": total_users,
            "total_employees": total_employees,
            "total_admins": total_admins,
            "total_members": total_members,
        },
    )

