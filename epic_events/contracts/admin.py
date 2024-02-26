from django.contrib import admin
from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('total_amount', 'remaining_amount', 'status',
                    'creation_date', 'client', 'support_contact')
