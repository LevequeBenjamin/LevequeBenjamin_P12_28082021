from django.contrib import admin
from django import forms
from contracts.models import Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ('client', 'sales_contact', 'amount', 'payment_due_date', 'is_finished', 'is_paid')


class ContractAdmin(admin.ModelAdmin):
    form = ContractForm
    list_display = ("id", 'client', 'sales_contact', 'amount', 'payment_due_date', 'is_finished', 'is_paid')


admin.site.register(Contract, ContractAdmin)
