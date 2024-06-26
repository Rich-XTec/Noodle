from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .forms import ModelUsuarioChangeForm, ModelUsuarioCreateForm
from .models import ModelUsuario

@admin.register(ModelUsuario)
class ModelUsuarioAdmin(UserAdmin):
    add_form = ModelUsuarioCreateForm
    form = ModelUsuarioChangeForm
    model = ModelUsuario
    list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')

    #quais dados apresentar ao acessar a area
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Information', {'fields': ('first_name', 'last_name', 'fone')}),
        ('Permissions',{'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'data_joined')}),
    )
