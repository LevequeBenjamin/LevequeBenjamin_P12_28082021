from django.contrib import admin
from django import forms

from accounts.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email", "role")

    def save(self, commit=True):
        """
        Overrides method in BaseModelForm.
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if self.cleaned_data.get("role") == 1:
            user.is_staff = True
            user.is_superuser = True
        if commit:
            user.save()
        return user


class UserAdmin(admin.ModelAdmin):
    """
    Overrides attributes in BaseModelAdmin.
    """
    form = UserForm
    list_display = ("id", "username", "email", "role", "is_staff")


admin.site.register(User, UserAdmin)
