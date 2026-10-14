from django.db import models
from django.contrib.auth.models import User


# =========================================================
# Employee
# ข้อมูลพนักงาน
# =========================================================

class Employee(models.Model):

    # =====================================================
    # ข้อมูลส่วนตัว
    # =====================================================

    name = models.CharField(
        max_length=100,
        verbose_name="ชื่อ-นามสกุล"
    )

    address = models.TextField(
        blank=True,
        verbose_name="ที่อยู่"
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="เบอร์โทรศัพท์"
    )

    email = models.EmailField(
        blank=True,
        verbose_name="อีเมล"
    )

    id_card = models.CharField(
        max_length=13,
        blank=True,
        verbose_name="เลขบัตรประจำตัวประชาชน"
    )

    # =====================================================
    # เอกสารพนักงาน
    # =====================================================

    education_document = models.FileField(
        upload_to="employees/education/",
        blank=True,
        null=True,
        verbose_name="สำเนาวุฒิการศึกษา"
    )

    bank_document = models.FileField(
        upload_to="employees/bank/",
        blank=True,
        null=True,
        verbose_name="สำเนาหน้าสมุดบัญชีธนาคาร"
    )

    social_security_document = models.FileField(
        upload_to="employees/social_security/",
        blank=True,
        null=True,
        verbose_name="เอกสารประกันสังคม"
    )

    tax_document = models.FileField(
        upload_to="employees/tax/",
        blank=True,
        null=True,
        verbose_name="เอกสารลดหย่อนภาษี"
    )

    # =====================================================
    # รูปโปรไฟล์พนักงาน
    # =====================================================

    image = models.ImageField(
        upload_to="employees/",
        blank=True,
        null=True,
        verbose_name="รูปโปรไฟล์"
    )

    # =====================================================
    # ข้อมูลการทำงานปัจจุบัน
    # =====================================================

    position = models.CharField(
        max_length=100,
        verbose_name="ตำแหน่ง"
    )

    department = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="แผนก"
    )

    manager = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="ผู้จัดการ / ผู้บังคับบัญชา"
    )

    employment_type = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="ประเภทการจ้าง"
    )

    start_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="วันเริ่มงาน"
    )

    probation_months = models.PositiveIntegerField(
        default=0,
        verbose_name="ระยะเวลาทดลองงาน (เดือน)"
    )

    # =====================================================
    # เงินเดือนและค่าตอบแทน
    # =====================================================

    salary = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="เงินเดือน"
    )

    overtime_rate = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="ค่าล่วงเวลาต่อชั่วโมง"
    )

    benefits = models.TextField(
        blank=True,
        verbose_name="สิทธิประโยชน์พิเศษ"
    )

    pay_period = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="รอบการจ่ายเงิน"
    )

    # =====================================================
    # Meta
    # =====================================================

    class Meta:
        ordering = ["-id"]
        verbose_name = "พนักงาน"
        verbose_name_plural = "พนักงาน"

    # =====================================================
    # String
    # =====================================================

    def __str__(self):
        return self.name


# =========================================================
# UserProfile
# ข้อมูลโปรไฟล์ผู้ใช้งานระบบ
# =========================================================

class UserProfile(models.Model):

    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("member", "Member"),
    )

    # =====================================================
    # เชื่อมกับ Django User
    # =====================================================

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="userprofile"
    )

    # =====================================================
    # ข้อมูลส่วนตัว
    # =====================================================

    first_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="ชื่อ"
    )

    last_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="นามสกุล"
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="เบอร์โทรศัพท์"
    )

    # =====================================================
    # รูปโปรไฟล์
    # =====================================================

    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
        verbose_name="รูปโปรไฟล์"
    )

    # =====================================================
    # สิทธิ์ผู้ใช้งาน
    # =====================================================

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="member",
        verbose_name="สิทธิ์ผู้ใช้งาน"
    )

    # =====================================================
    # Meta
    # =====================================================

    class Meta:
        verbose_name = "โปรไฟล์ผู้ใช้"
        verbose_name_plural = "โปรไฟล์ผู้ใช้"

    # =====================================================
    # String
    # =====================================================

    def __str__(self):
        return self.user.username
