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
            'title', 'client', 'amount', 'payment_due_date', 'is_finished', 'is_paid'
        )

    def save(self, commit=True):
        """Overrides method in BaseModelForm."""
        contract = super().save(commit=False)
        contract.sales_contact = self.cleaned_data['client'].sales_contact
        if commit:
            contract.save()
        return contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    """Overrides attributes in BaseModelAdmin."""
    form = ContractForm
    list_display = (
        "id", 'title', 'client', 'sales_contact', 'amount', 'payment_due_date', 'is_finished', 'is_paid'
    )
    search_fields = ('title', )
    list_filter = ('client', 'sales_contact', 'is_finished', 'is_paid')
    autocomplete_fields = ('client', 'sales_contact',)
    list_per_page = 25
