from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    message = 'You must be The Admin'
    def has_object_permission(self, request, view, obj):
        if request.user.user_type == 'Admin':
            return obj.user == request.user