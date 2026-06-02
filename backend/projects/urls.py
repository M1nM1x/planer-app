from django.urls import path

from projects import views

urlpatterns = [
    path("api/v1/projects/", views.ProjectListAPIView.as_view(), name="projects"),
    path("api/v1/projects/<int:pk>/", views.ProjectDetailAPIView.as_view(), name="project_detail"),
    path("api/v1/projects/create/", views.CreateProjectAPIView.as_view(), name="create_project"),
]