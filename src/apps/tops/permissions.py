from rest_framework import permissions

from apps.companies.models import Company


class IsCompanyOwner(permissions.BasePermission):
    """
    Permission to check if a user is an admin or Like/Dislike owner
        To only allow:
        - Admin users to do anything
        - Company owner to only view the available packages
    """

    def has_permission(self, request, *args, **kwargs):
        """
        Check if a user is an admin or Company owner
        """

        print("Requesting User: ", request.user)
        
        company_owners = Company.objects.filter(owner=request.user)
        return company_owners.exists()