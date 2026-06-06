from rest_framework import serializers

from .models import Project, ProjectMember

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class CreateProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=5)

    class Meta:
        model = Project
        fields = ['name', 'description']


class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = ['user', 'role', 'joined_at']

class AddProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = ['user', 'role']


