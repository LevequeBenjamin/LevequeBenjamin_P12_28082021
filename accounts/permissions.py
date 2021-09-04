"""Contains the permissions of accounts app."""

# rest_framework
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission

# models
from clients.models import Client


class IsSales(BasePermission):
    """Verification of global authorizations for the sales team."""

    def has_permission(self, request, view):
        """Overrides method in BasePermission."""
        # Return true if it's a get method and the user is admin.
        # The authenticated user must have a role attribute equal to 2 (sales).
        if request.method == 'GET':
            return True
        if request.user.is_superuser:
            return True
        return request.user.role == 2

    def has_object_permission(self, request, view, obj):
        """Overrides method in BasePermission."""
        # Return true if it's a get method and the user is admin.
        # The authenticated user must be the sales contact of the instance.
        if request.method == 'GET':
            return True
        if request.user.is_superuser:
            return True
        return request.user == obj.sales_contact


class IsClientContact(BasePermission):
    """Verification of global authorizations for the client contact."""

    def has_permission(self, request, view):
        """Overrides method in BasePermission."""
        # Return true if it's a get method and the user is admin.
        # The authenticated user must be the sales contact of the client.
        if request.method == 'GET':
            return True
        if request.user.is_superuser:
            return True
        client = get_object_or_404(Client, pk=request.data.get("client"))
        return request.user == client.sales_contact

    def has_object_permission(self, request, view, obj):
        """Overrides method in BasePermission."""
        # Return true if it's a get method and the user is admin.
        # The authenticated user must be the contact person of the client attribute of instance.
        if request.method == 'GET':
            return True
        if request.user.is_superuser:
            return True
        return request.user == obj.client.sales_contact


class IsSupport(BasePermission):
    """Verification of global authorizations for the support team."""

    def has_object_permission(self, request, view, obj):
        """Overrides method in BasePermission."""
        # Return true if it's a get method and the user is admin.
        # The authenticated user must be the support contact of the instance.
        if request.method == 'GET':
            return True
        if request.user.is_superuser:
            return True
        return request.user == obj.support_contact
