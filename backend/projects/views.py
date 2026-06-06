from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

from .models import Project, ProjectMember
from .permissions import IsProjectOwner
from .serializers import (CreateProjectSerializer,
                          ProjectMemberSerializer,
                          ProjectSerializer,
                          AddProjectMemberSerializer)


class ProjectAPIView(generics.ListCreateAPIView):
    """
    Responsible for creating project and listing all projects
    """

    permission_classes = [IsAuthenticated]

    queryset = Project.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProjectSerializer

        return CreateProjectSerializer

class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Responsible for updating and deleting project and getting info about concrete project
    """

    permission_classes = [IsProjectOwner]

    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProjectSerializer

        return CreateProjectSerializer


class ProjectMemberAPIView(generics.ListCreateAPIView):

    permission_classes = [IsProjectOwner]

    queryset = ProjectMember.objects.all()
    serializer_class = AddProjectMemberSerializer

    def get_queryset(self):
        return ProjectMember.objects.filter(project_id=self.kwargs["pk"])

    def perform_create(self, serializer, **kwargs):
        project = Project.objects.get(pk=self.kwargs['pk'])

        serializer.save(project=project)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProjectMemberSerializer

        return AddProjectMemberSerializer

class RemoveProjectMemberAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsProjectOwner]

    queryset = ProjectMember.objects.all()

    def get_object(self):
        return ProjectMember.objects.get(
            project_id=self.kwargs["project_pk"],
            user_id=self.kwargs["user_pk"]
        )