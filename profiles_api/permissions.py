from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    "Edit own profile"

    def has_object_permission(self, request, view, obj):
        "Check user if try edit any object."
        if request.method in permissions.SAFE_METHODS:
            return True 

        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    "Alow users to update thei own status"

    def has_object_permission(self, request, view, obj):
        "Check the user is trying to update their status"
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id