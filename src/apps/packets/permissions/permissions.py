from rest_framework import permissions

from apps.companies.models import Company


class IsAdminOrIsCompanyOwner(permissions.BasePermission):
    """
    Permission to check if a user is an admin or Like/Dislike owner
        To only allow:
        - Admin users to do anything
        - Company owner to only view the available packages
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if a user is an admin or Company owner
        """
        if request.user.is_superuser or request.user.is_staff:
            return True

        # ======== For safe methods (GET, HEAD, OPTIONS), check if user is a company owner =========
        if request.method in permissions.SAFE_METHODS:
            print("Requesting User: ", request.user)

            company_owners = Company.objects.filter(owner=request.user)

            return company_owners.exists()

        return False