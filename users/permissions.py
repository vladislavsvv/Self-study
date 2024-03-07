from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserIsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class UserIsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешить чтение всем
        if request.method in SAFE_METHODS:
            return True

        # Разрешить запись только владельцу объекта
        return obj.owner == request.user
