from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to update only their own profile"""
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if(request.method in permissions.SAFE_METHODS):
            return True
        #For methods of PUT, POST, PATCH or DELETE
        return object.id == request.user.id
