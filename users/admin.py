from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import User

class UserAdmin(BaseUserAdmin):
    """
    Admin View for User
    """

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'bio',
                'profile_picture',
            )
        }),
        (_('Follow'), {'fields': ('followers', 'following',)}),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            ),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, UserAdmin)