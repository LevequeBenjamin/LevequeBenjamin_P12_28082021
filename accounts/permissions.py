# rest_framework
from rest_framework.permissions import BasePermission


class IsSales(BasePermission):
    """
    Verification of global authorizations for project authors.
    Return true if it's a get method and the user is admin.
    """

    # Overrides method in BasePermission
    def has_permission(self, request, view):
        """
        The instance must have an author attribute and be equal to the authenticated user.
        """
        if request.method == 'GET':
            return True
        if request.user.is_superuser:
            return True
        return request.user.role == 2


class IsSupport(BasePermission):
    """
    Verification of global authorizations for project authors.
    Return true if it's a get method and the user is admin.
    """

    # Overrides method in BasePermission
    def has_object_permission(self, request, view, obj):
        """
        The instance must have an author attribute and be equal to the authenticated user.
        """
        if request.method == 'GET':
            return True
        # if request.user.role == "support":
        #     return True
        return obj.support_contact == request.user
