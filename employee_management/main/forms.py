from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from .models import Employee, UserProfile


# =========================================================
# Employee Form
# =========================================================

class EmployeeForm(forms.ModelForm):

    POSITION_CHOICES = [
        ("", "เลือกตำแหน่ง"),
        ("ผู้จัดการ", "ผู้จัดการ"),
        ("หัวหน้าแผนก", "หัวหน้าแผนก"),
        ("พนักงานบัญชี", "พนักงานบัญชี"),
        ("พนักงานขาย", "พนักงานขาย"),
        ("พนักงานฝ่ายบุคคล", "พนักงานฝ่ายบุคคล"),
        ("พนักงานไอที", "พนักงานไอที"),
        ("นักพัฒนาซอฟต์แวร์", "นักพัฒนาซอฟต์แวร์"),
        ("นักศึกษาฝึกงาน", "นักศึกษาฝึกงาน"),
        ("อื่น ๆ", "อื่น ๆ"),
    ]

    DEPARTMENT_CHOICES = [
        ("", "เลือกแผนก"),
        ("ฝ่ายบริหาร", "ฝ่ายบริหาร"),
        ("ฝ่ายบัญชี", "ฝ่ายบัญชี"),
        ("ฝ่ายขาย", "ฝ่ายขาย"),
        ("ฝ่ายบุคคล", "ฝ่ายบุคคล"),
        ("ฝ่ายไอที", "ฝ่ายไอที"),
        ("ฝ่ายการตลาด", "ฝ่ายการตลาด"),
        ("ฝ่ายผลิต", "ฝ่ายผลิต"),
        ("อื่น ๆ", "อื่น ๆ"),
    ]

    EMPLOYMENT_TYPE_CHOICES = [
        ("", "เลือกประเภทการจ้าง"),
        ("พนักงานประจำ", "พนักงานประจำ"),
        ("พนักงานสัญญาจ้าง", "พนักงานสัญญาจ้าง"),
        ("นักศึกษาฝึกงาน", "นักศึกษาฝึกงาน"),
        ("พาร์ทไทม์", "พาร์ทไทม์"),
    ]

    PAY_PERIOD_CHOICES = [
        ("", "เลือกรอบการจ่าย"),
        ("รายเดือน", "รายเดือน"),
        ("รายสัปดาห์", "รายสัปดาห์"),
        ("รายวัน", "รายวัน"),
    ]

    # -----------------------------------------------------
    # ตำแหน่ง
    # -----------------------------------------------------

    position = forms.ChoiceField(
        choices=POSITION_CHOICES,
        required=True,
        label="ตำแหน่ง",
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )

    # -----------------------------------------------------
    # แผนก
    # -----------------------------------------------------

    department = forms.ChoiceField(
        choices=DEPARTMENT_CHOICES,
        required=False,
        label="แผนก",
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )

    # -----------------------------------------------------
    # ประเภทการจ้าง
    # -----------------------------------------------------

    employment_type = forms.ChoiceField(
        choices=EMPLOYMENT_TYPE_CHOICES,
        required=False,
        label="ประเภทการจ้าง",
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )

    # -----------------------------------------------------
    # รอบการจ่ายเงิน
    # -----------------------------------------------------

    pay_period = forms.ChoiceField(
        choices=PAY_PERIOD_CHOICES,
        required=False,
        label="รอบการจ่ายเงิน",
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:

        model = Employee

        fields = [
            "name",
            "address",
            "phone",
            "email",
            "id_card",

            "education_document",
            "bank_document",
            "social_security_document",
            "tax_document",
            "image",

            "position",
            "department",
            "manager",
            "employment_type",
            "start_date",
            "probation_months",

            "salary",
            "overtime_rate",
            "benefits",
            "pay_period",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "กรอกชื่อ-นามสกุล",
                    "autocomplete": "name",
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "กรอกที่อยู่ปัจจุบัน",
                    "rows": 4,
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "เช่น 0812345678",
                    "maxlength": "10",
                    "inputmode": "numeric",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "example@email.com",
                    "autocomplete": "email",
                }
            ),

            "id_card": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "เลขบัตรประชาชน 13 หลัก",
                    "maxlength": "13",
                    "inputmode": "numeric",
                }
            ),

            "education_document": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": ".pdf,.jpg,.jpeg,.png",
                }
            ),

            "bank_document": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": ".pdf,.jpg,.jpeg,.png",
                }
            ),

            "social_security_document": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": ".pdf,.jpg,.jpeg,.png",
                }
            ),

            "tax_document": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": ".pdf,.jpg,.jpeg,.png",
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": ".jpg,.jpeg,.png",
                }
            ),

            "manager": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "เช่น คุณสมชาย ใจดี",
                }
            ),

            "start_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "probation_months": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "เช่น 4",
                    "min": "0",
                    "max": "24",
                }
            ),

            "salary": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "เช่น 18000",
                    "min": "0",
                    "step": "0.01",
                }
            ),

            "overtime_rate": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "เช่น 100",
                    "min": "0",
                    "step": "0.01",
                }
            ),

            "benefits": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "เช่น ประกันสุขภาพ, ค่าเดินทาง, โบนัส",
                    "rows": 4,
                }
            ),
        }

    # =====================================================
    # ตรวจสอบเบอร์โทรศัพท์
    # =====================================================

    def clean_phone(self):

        phone = self.cleaned_data.get("phone", "").strip()

        if phone:

            if not phone.isdigit():
                raise forms.ValidationError(
                    "เบอร์โทรศัพท์ต้องเป็นตัวเลขเท่านั้น"
                )

            if len(phone) != 10:
                raise forms.ValidationError(
                    "เบอร์โทรศัพท์ต้องมี 10 หลัก"
                )

            if not phone.startswith("0"):
                raise forms.ValidationError(
                    "เบอร์โทรศัพท์ต้องขึ้นต้นด้วย 0"
                )

        return phone

    # =====================================================
    # ตรวจสอบเลขบัตรประชาชน
    # =====================================================

    def clean_id_card(self):

        id_card = self.cleaned_data.get("id_card", "").strip()

        if id_card:

            if not id_card.isdigit():
                raise forms.ValidationError(
                    "เลขบัตรประชาชนต้องเป็นตัวเลขเท่านั้น"
                )

            if len(id_card) != 13:
                raise forms.ValidationError(
                    "เลขบัตรประชาชนต้องมี 13 หลัก"
                )

            if id_card.startswith("0"):
                raise forms.ValidationError(
                    "เลขบัตรประชาชนต้องไม่ขึ้นต้นด้วย 0"
                )

        return id_card

    # =====================================================
    # ตรวจสอบเงินเดือน
    # =====================================================

    def clean_salary(self):

        salary = self.cleaned_data.get("salary")

        if salary is not None and salary < 0:
            raise forms.ValidationError(
                "เงินเดือนต้องไม่ติดลบ"
            )

        return salary

    # =====================================================
    # ตรวจสอบค่าล่วงเวลา
    # =====================================================

    def clean_overtime_rate(self):

        overtime_rate = self.cleaned_data.get("overtime_rate")

        if overtime_rate is not None and overtime_rate < 0:
            raise forms.ValidationError(
                "ค่าล่วงเวลาต่อชั่วโมงต้องไม่ติดลบ"
            )

        return overtime_rate

    # =====================================================
    # ตรวจสอบระยะเวลาทดลองงาน
    # =====================================================

    def clean_probation_months(self):

        months = self.cleaned_data.get("probation_months")

        if months is not None:

            if months < 0:
                raise forms.ValidationError(
                    "ระยะเวลาทดลองงานต้องไม่ติดลบ"
                )

            if months > 24:
                raise forms.ValidationError(
                    "ระยะเวลาทดลองงานต้องไม่เกิน 24 เดือน"
                )

        return months


# =========================================================
# Register Form
# =========================================================

class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        label="รหัสผ่าน",
        min_length=8,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "กรอกรหัสผ่านอย่างน้อย 8 ตัวอักษร",
                "autocomplete": "new-password",
            }
        )
    )

    confirm_password = forms.CharField(
        label="ยืนยันรหัสผ่าน",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "กรอกรหัสผ่านอีกครั้ง",
                "autocomplete": "new-password",
            }
        )
    )

    class Meta:

        model = User

        fields = [
            "username",
            "email",
            "password",
            "confirm_password",
        ]

        widgets = {

            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "กรอกชื่อผู้ใช้",
                    "autocomplete": "username",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "example@email.com",
                    "autocomplete": "email",
                }
            ),
        }

        labels = {
            "username": "ชื่อผู้ใช้",
            "email": "อีเมล",
        }

    # =====================================================
    # ตรวจสอบ Username
    # =====================================================

    def clean_username(self):

        username = self.cleaned_data.get("username")

        if username and User.objects.filter(
            username__iexact=username
        ).exists():

            raise forms.ValidationError(
                "ชื่อผู้ใช้นี้ถูกใช้งานแล้ว"
            )

        return username

    # =====================================================
    # ตรวจสอบรหัสผ่าน
    # =====================================================

    def clean_password(self):

        password = self.cleaned_data.get("password")

        if password:
            validate_password(password)

        return password

    # =====================================================
    # ตรวจสอบรหัสผ่านซ้ำ
    # =====================================================

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:

            if password != confirm_password:

                self.add_error(
                    "confirm_password",
                    "รหัสผ่านและยืนยันรหัสผ่านไม่ตรงกัน"
                )

        return cleaned_data

    # =====================================================
    # บันทึก User
    # =====================================================

    def save(self, commit=True):

        user = super().save(commit=False)

        password = self.cleaned_data["password"]

        user.set_password(password)

        if commit:
            user.save()

        return user


# =========================================================
# User Profile Form
# =========================================================

class UserProfileForm(forms.ModelForm):

    class Meta:

        model = UserProfile

        fields = [
            "first_name",
            "last_name",
            "phone",
            "profile_image",
        ]

        widgets = {

            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "ชื่อ",
                }
            ),

            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "นามสกุล",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "เบอร์โทรศัพท์",
                    "maxlength": "10",
                    "inputmode": "numeric",
                }
            ),

            "profile_image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": ".jpg,.jpeg,.png",
                }
            ),
        }

    # =====================================================
    # ตรวจสอบเบอร์โทรศัพท์
    # =====================================================

    def clean_phone(self):

        phone = self.cleaned_data.get("phone", "").strip()

        if phone:

            if not phone.isdigit():
                raise forms.ValidationError(
                    "เบอร์โทรศัพท์ต้องเป็นตัวเลขเท่านั้น"
                )

            if len(phone) != 10:
                raise forms.ValidationError(
                    "เบอร์โทรศัพท์ต้องมี 10 หลัก"
                )

            if not phone.startswith("0"):
                raise forms.ValidationError(
                    "เบอร์โทรศัพท์ต้องขึ้นต้นด้วย 0"
                )

        return phone
