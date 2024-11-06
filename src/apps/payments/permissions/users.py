from rest_framework.permissions import BasePermission


class IsAdminOrIsCompanyOwner(BasePermission):
    """
    Permission to check if a user is an admin or comment owner
        To only allow:
        - Admin users to do anything
        - Regular users to only manage their own payments
    """

    def has_object_permission(self, request, view, obj):
        # ======== Admins can do anything  ========

        if request.user.is_superuser or request.user.is_staff:
            return True

        # ======== GET, HEAD, OPTIONS ========
        return request.method in request.permissions.SAFE_METHODS