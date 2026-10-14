# ระบบจัดการพนักงาน (Django)

โปรเจกต์ Django ตัวอย่างที่มี 3 หน้าเว็บ (หน้าหลัก / สินค้า / ติดต่อสอบถาม)
ใช้เทมเพลตหลักร่วมกันผ่าน `templates/basetemplate.html`

## โครงสร้างโปรเจกต์

```
employee_management/
├── manage.py
├── requirements.txt
├── employee_management/       # ตั้งค่าโปรเจกต์ (settings, urls หลัก)
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── main/                       # แอปหลักที่จัดการทั้ง 3 หน้า
│   ├── views.py                # view: home, products, contact
│   ├── urls.py                 # route ของแต่ละหน้า
│   ├── models.py                # Employee, ContactMessage
│   └── admin.py
├── templates/
│   ├── basetemplate.html       # เทมเพลตหลัก (navbar, footer, block content)
│   ├── home.html                # extends basetemplate.html
│   ├── products.html            # extends basetemplate.html
│   └── contact.html             # extends basetemplate.html
└── static/
    └── css/style.css
```

## วิธีติดตั้งและรัน

1. ติดตั้งไลบรารีที่จำเป็น (แนะนำให้สร้าง virtual environment ก่อน)
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows ใช้: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. สร้างฐานข้อมูล (SQLite ใช้งานได้ทันทีโดยไม่ต้องติดตั้งเพิ่ม)
   ```bash
   python manage.py migrate
   ```

3. (ไม่บังคับ) สร้างบัญชีผู้ดูแลระบบเพื่อเข้าหน้า admin
   ```bash
   python manage.py createsuperuser
   ```

4. รันเซิร์ฟเวอร์
   ```bash
   python manage.py runserver
   ```

5. เปิดเบราว์เซอร์ไปที่
   - หน้าหลัก: http://127.0.0.1:8000/
   - หน้าสินค้า: http://127.0.0.1:8000/products/
   - หน้าติดต่อสอบถาม: http://127.0.0.1:8000/contact/
   - หน้า admin: http://127.0.0.1:8000/admin/

## จุดสำคัญตามโจทย์

- ทุกหน้าใช้ `{% extends 'basetemplate.html' %}` เพื่อดึงโครงสร้าง navbar/footer ร่วมกัน
- เนื้อหาเฉพาะของแต่ละหน้าอยู่ภายใน `{% block content %} ... {% endblock %}`
- `basetemplate.html` กำหนด `{% block title %}` และ `{% block content %}` ไว้ให้แต่ละหน้า override
- ฟอร์ม "ติดต่อสอบถาม" บันทึกข้อมูลลงตาราง `ContactMessage` และแสดงข้อความแจ้งเตือนเมื่อส่งสำเร็จ
- มีโมเดล `Employee` เตรียมไว้สำหรับต่อยอดฟีเจอร์จัดการพนักงาน (CRUD) ในอนาคต
