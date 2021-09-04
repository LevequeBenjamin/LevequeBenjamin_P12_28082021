from django.contrib import admin
from django import forms
from clients.models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'sales_contact')


class ClientAdmin(admin.ModelAdmin):
    """Overrides attributes in BaseModelAdmin."""
    form = ClientForm
    list_display = ("id", 'first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'sales_contact')


admin.site.register(Client, ClientAdmin)
