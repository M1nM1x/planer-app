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
