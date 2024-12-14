from rest_framework import permissions



class CheckCreateCourse(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'teacher':
            return True
        return False



class CheckEditCourse(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
       return  request.user == obj.owner



class CheckCreateLesson(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'teacher'



class CheckReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'teacher':
             return request.method in permissions.SAFE_METHODS
        return request.user.user_role == 'student'



class CheckCertificate(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.user_role == 'teacher'