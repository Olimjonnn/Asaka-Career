from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_object_permission(self, request, view, obj):
        # is_admin
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.role == 2