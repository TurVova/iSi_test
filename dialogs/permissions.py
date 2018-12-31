from rest_framework.exceptions import ValidationError
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    message = 'You must be The Admin'
    def has_permission(self, request, view):
        return request.user.user_type == 'Admin'