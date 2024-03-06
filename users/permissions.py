from rest_framework.permissions import BasePermission


class UserIsStaff(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_permissions:
            return True
        else:
            return False
