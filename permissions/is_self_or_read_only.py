from rest_framework import permissions

class IsSelfOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow users to edit it their profile.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `author`.
        return obj == request.user
