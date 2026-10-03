[app]

title = JARVIS
package.name = jarvis
package.domain = org.jarvis

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy,pyjnius,speechrecognition

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2

warn_on_root = 1


[app:android]

android.permissions = RECORD_AUDIO,INTERNET

android.api = 35
android.minapi = 23

android.archs = arm64-v8a, armeabi-v7a

android.accept_sdk_license = True