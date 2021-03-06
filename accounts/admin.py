from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email', 'first_name', 'last_name', 'gender', 'date_of_birth']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional information', {'fields': ('gender', 'date_of_birth', 'biography', 'avatar',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
