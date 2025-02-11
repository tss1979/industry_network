from rest_framework.permissions import BasePermission


class UserIsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class UserIsActivePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_active
