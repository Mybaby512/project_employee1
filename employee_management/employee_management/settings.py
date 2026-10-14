"""
Django settings for employee_management project.
ระบบจัดการพนักงาน - ไฟล์ตั้งค่าหลักของโปรเจกต์
"""

from pathlib import Path

# Path หลักของโปรเจกต์
BASE_DIR = Path(__file__).resolve().parent.parent

# ค่าความปลอดภัย - ในการใช้งานจริงควรเปลี่ยนและเก็บเป็นความลับ (environment variable)
SECRET_KEY = 'django-insecure-change-this-key-before-deploying-to-production'

# โหมด Debug (ควรตั้งเป็น False ตอน deploy จริง)
DEBUG = True

ALLOWED_HOSTS = ['*']

# แอปพลิเคชันที่ติดตั้งในโปรเจกต์
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # แอปของเราเอง
    'main',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'employee_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # กำหนดโฟลเดอร์ templates กลางของโปรเจกต์ ให้ทุกแอปมองเห็น basetemplate.html ร่วมกัน
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'employee_management.wsgi.application'

# ฐานข้อมูล (ใช้ SQLite ซึ่งเป็นค่าเริ่มต้น ไม่ต้องติดตั้งเพิ่ม)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ภาษาและเขตเวลา
LANGUAGE_CODE = 'th'
TIME_ZONE = 'Asia/Bangkok'
USE_I18N = True
USE_TZ = True

# ไฟล์ static (CSS/JS/รูปภาพ)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# บรรทัดนี้บอกให้ Django รู้ว่าหน้า Login ของเราอยู่ที่ URL ไหน
LOGIN_URL = 'login' 
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'login'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# ตั้งค่าสำหรับการอัปโหลดรูปภาพ (Media Files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'