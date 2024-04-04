from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

from municipio.mixins import MunicipioAdminMixin
from usuario.models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(MunicipioAdminMixin, UserAdmin):
    list_display = ('username', 'email', 'persona', 'municipio', 'is_active', 'is_staff', 'is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Otros datos', {'fields': ('persona', 'municipio')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
