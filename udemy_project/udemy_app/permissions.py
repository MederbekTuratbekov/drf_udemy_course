from rest_framework import permissions


class CreateReviewPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'student'

class CreateCoursePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'teacher'