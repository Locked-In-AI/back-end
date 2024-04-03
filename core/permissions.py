from rest_framework.permissions import IsAuthenticated


class AdminOrOwnerPermission(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user and (
                    request.user.is_staff or
                    request.user == getattr(obj, 'user', None)
            )
    )