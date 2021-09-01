from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework.generics import get_object_or_404

from accounts.models import User
from clients.models import Client
from contracts.models import Contract


class ContractForm(forms.ModelForm):
    clients = Client.objects.all()
    clients_choices = ((client, client) for client in clients)
    client = forms.ChoiceField(choices=clients_choices)

    sales_users = User.objects.filter(role=2)
    sales_choices = ((user, user) for user in sales_users)
    sales_contact = forms.ChoiceField(choices=sales_choices)

    class Meta:
        model = Contract
        fields = ('client', 'sales_contact', 'amount', 'payment_due_date', 'is_finished', 'is_paid')

    def clean(self):
        self._validate_unique = True
        print(self.cleaned_data['client'])
        self.cleaned_data['client'] = get_object_or_404(Client, email=self.cleaned_data.get('client'))
        self.cleaned_data['sales_contact'] = get_object_or_404(User, username=self.cleaned_data.get('sales_contact'))
        return self.cleaned_data

    def save(self, commit=True):
        """
        Overrides method in BaseModelForm.
        """
        contract = super().save(commit=False)
        if self.cleaned_data.get("sales_contact") not in self.sales_users:
            raise ValidationError(_("Cet utilisateur ne fait pas partie des vendeurs."))
        if commit:
            contract.save()
        return contract


class ContractAdmin(admin.ModelAdmin):
    form = ContractForm
    list_display = ('client', 'sales_contact', 'amount', 'payment_due_date', 'is_finished', 'is_paid')


admin.site.register(Contract, ContractAdmin)
