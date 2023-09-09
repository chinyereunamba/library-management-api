from django.contrib import admin
from .models import Account, Student, Admin
from django.contrib.admin import ModelAdmin

# Register your models here.


class AccountAdmin(ModelAdmin):
    list_display = [
        "email",
        "username",
        "is_active",
        "is_admin",
        "is_superuser",
        "last_login",
        "date_joined",
    ]

    search_fields = ['email', 'username']
    readonly_fields = ['date_joined', 'last_login', 'password']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class AdminsAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number']

admin.site.register(Account, AccountAdmin)
admin.site.register(Admin, AdminsAdmin)
admin.site.register(Student)