from rest_framework.permissions import BasePermission


class AdminOrOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user and (
                    request.user.is_staff or
                    request.user == getattr(obj, 'user', None)
            )
    )

    def has_permission(self, request, view):
        return bool(
            request.user
        )
