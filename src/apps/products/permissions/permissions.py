from rest_framework.permissions import BasePermission


class CustomIsCompanyOwnerOrReadOnlyPermission(BasePermission):
    """
    Custom permission to only allow company owners or staff to edit products.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Write permissions are only allowed to the owner of the company or staff
        return request.user == obj.company.owner or request.user.is_staff
