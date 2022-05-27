from rest_framework import permissions

class IsAuthorOrCreateOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow authors of an object to edit it.
    Assumes the model instance has an `author` attribute.
    """

    safe_methods = ('GET', 'POST', 'HEAD', 'OPTIONS')

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, POST, HEAD or OPTIONS requests.
        if request.method in self.safe_methods:
            return True

        # Instance must have an attribute named `author`.
        return obj.author == request.user
