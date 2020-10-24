from django.contrib import admin
from home.models import Setting

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'address', 'email']

admin.site.register(Setting, SettingAdmin)