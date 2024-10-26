from rest_framework import permissions

class IsAdminOrCommentOwner(permissions.BasePermission):
    """
    Permission to check if a user is an admin or comment owner
        To only allow:
        - Admin users to do anything
        - Regular users to only manage their own comments
    """

    def has_permission(self, request, view):
        # ========= Allow if user is authenticated =========
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # ======== Admin can do anything ========
        if request.user.is_staff:
            return True

        # ======== For DELETE, check if the user owns the comment
        if request.method == 'DELETE':
            return obj.user == request.user

        # ======== Allow GET requests ========
        return request.method in permissions.SAFE_METHODS