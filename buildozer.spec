[app]

# نام برنامه
title = JARVIS

# نام پکیج
package.name = jarvis

# دامنه پکیج
package.domain = org.jarvis

# مسیر سورس
source.dir = .

# فایل‌های قابل استفاده
source.include_exts = py,png,jpg,kv,atlas

# نسخه
version = 1.0

# وابستگی‌ها
requirements = python3,kivy,pyjnius,speechrecognition

# حالت عمودی
orientation = portrait

# تمام صفحه
fullscreen = 0


# -------------------------
# Android
# -------------------------

# نسخه API
android.api = 35

# حداقل نسخه اندروید
android.minapi = 23

# معماری
android.archs = arm64-v8a

# مجوزها
android.permissions = RECORD_AUDIO,INTERNET

# قبول لایسنس Android SDK
android.accept_sdk_license = True

# Java
android.ndk_api = 23


# -------------------------
# Buildozer
# -------------------------

[buildozer]

log_level = 2

warn_on_root = 1
