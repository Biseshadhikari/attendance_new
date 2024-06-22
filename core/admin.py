from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("collage", "username", "is_staff", "is_active", "is_superuser", "usertype", "first_name", "last_name", "email")
    list_filter = ("is_staff", "is_active", "is_superuser", "usertype")
    fieldsets = (
        (None, {"fields": ("collage", "username", "password")}),
        ("Personal info", {"fields": ("usertype", "first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("collage", "username", "password1", "password2", "usertype", "is_staff", "is_active", "is_superuser", "first_name", "last_name", "email", "groups", "user_permissions", "last_login", "date_joined"),
        }),
    )
    search_fields = ("collage", "username", "first_name", "last_name", "email")
    ordering = ("username",)

admin.site.register(User, CustomUserAdmin)
admin.site.register(College)
admin.site.register(Class)