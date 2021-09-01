from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework.generics import get_object_or_404

from accounts.models import User
from clients.models import Client


class ClientForm(forms.ModelForm):
    sales_users = User.objects.filter(role=2)
    sales_choices = ((user, user) for user in sales_users)
    sales_contact = forms.ChoiceField(choices=sales_choices)

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'sales_contact')

    def clean(self):
        self._validate_unique = True
        self.cleaned_data['sales_contact'] = get_object_or_404(User, username=self.cleaned_data.get('sales_contact'))
        return self.cleaned_data

    def save(self, commit=True):
        """
        Overrides method in BaseModelForm.
        """
        client = super().save(commit=False)
        if self.cleaned_data['sales_contact'] not in self.sales_users:
            raise ValidationError(_("Cet utilisateur ne fait pas partie des vendeurs."))
        if commit:
            client.save()
        return client


class ClientAdmin(admin.ModelAdmin):
    form = ClientForm
    list_display = ('first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'sales_contact')


admin.site.register(Client, ClientAdmin)
