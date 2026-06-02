from rest_framework import status, generics

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Project
from projects import serializers

class CreateProjectAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Project.objects.all()
    serializer_class = serializers.CreateProjectSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProjectListAPIView(APIView):

    def get(self, request, *args, **kwargs):
        projects_list = Project.objects.all()
        serializer = serializers.ProjectSerializer(projects_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer