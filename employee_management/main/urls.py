from django.urls import path
from . import views


urlpatterns = [
    # =====================================================
    # Authentication
    # =====================================================
    path(
        "login/",
        views.login_view,
        name="login",
    ),
    path(
        "register/",
        views.register_view,
        name="register",
    ),
    path(
        "logout/",
        views.logout_view,
        name="logout",
    ),

    # =====================================================
    # Home / Employee List
    # =====================================================
    path(
        "",
        views.index,
        name="index",
    ),

    # =====================================================
    # Employee
    # =====================================================
    # เพิ่มพนักงาน
    path(
        "employee/create/",
        views.create_employee,
        name="create_employee",
    ),
    # แก้ไขข้อมูลพนักงาน
    path(
        "employee/edit/<int:pk>/",
        views.edit_employee,
        name="edit_employee",
    ),
    # ลบข้อมูลพนักงาน
    path(
        "employee/delete/<int:pk>/",
        views.delete_employee,
        name="delete_employee",
    ),

    # =====================================================
    # Profile
    # =====================================================
    path(
        "profile/",
        views.profile_view,
        name="profile",
    ),

    # =====================================================
    # Contact
    # =====================================================
    path(
        "contact/",
        views.contact_view,
        name="contact",
    ),

    # =====================================================
    # Admin
    # =====================================================
    path(
        "admin-dashboard/",
        views.admin_dashboard,
        name="admin_dashboard",
    ),
]