from rest_framework import permissions

from .models import Project, ProjectMember



class IsProjectOwner(permissions.BasePermission):
    message = "User is not owner"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if obj.owner == request.user:
            return True
        return False

class IsProjectMember(permissions.BasePermission):
    message = "User is not member"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if ProjectMember.objects.filter(project=obj, user=request.user).exists():
            return True
        return False

class IsProjectManager(permissions.BasePermission):
    message = "User is not manager"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if ProjectMember.objects.filter(project=obj, user=request.user, role="MR").exists():
            return True
        return False

class CanManageProjectMember(permissions.BasePermission):
    message = "User have no permissions to manage members"

    @staticmethod
    def get_project_from_view(view):
        try:
            if "pk" in view.kwargs:
                return Project.objects.get(pk=view.kwargs["pk"])

            if "project_pk" in view.kwargs:
                return Project.objects.get(pk=view.kwargs["project_pk"])
        except Project.DoesNotExist:
            return None

        return None

    def has_permission(self, request, view):
        project = self.get_project_from_view(view)

        if not project:
            return False

        if project.owner == request.user:
            return True

        return ProjectMember.objects.filter(
            project=project,
            user=request.user,
            role="MR"
        ).exists()
