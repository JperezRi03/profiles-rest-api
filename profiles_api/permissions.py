from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    "Edit own profile"

    def has_object_permission(self, request, view, obj):
        "Check user if try edit any object."
        if request.method in permissions.SAFE_METHODS:
            return True 

        return obj.id == request.user.id