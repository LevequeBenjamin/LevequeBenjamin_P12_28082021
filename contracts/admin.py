"""Customizing the administrator interface."""

# django
from django.contrib import admin
from django import forms

# models
from contracts.models import Contract


class ContractForm(forms.ModelForm):
    """ContractForm inherits from ModelForm for creating Contract form."""

    class Meta:
        """Meta options."""
        model = Contract
        fields = (
            'client', 'sales_contact', 'amount', 'payment_due_date', 'is_finished', 'is_paid'
        )


class ContractAdmin(admin.ModelAdmin):
    """Overrides attributes in BaseModelAdmin."""
    form = ContractForm
    list_display = (
        "id", 'client', 'sales_contact', 'amount', 'payment_due_date', 'is_finished', 'is_paid'
    )


admin.site.register(Contract, ContractAdmin)
