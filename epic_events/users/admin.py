from django.contrib import admin
from .models import Client, User


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'telephone',
                    'compagny_name', 'last_update',
                    'creation_date', 'support_contact')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'department')
