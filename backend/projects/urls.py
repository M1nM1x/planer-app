from django.urls import path

from projects import views

urlpatterns = [
    path("api/v1/projects/", views.ProjectAPIView.as_view(), name="create_list_project"), # GET, POST
    path("api/v1/projects/<int:pk>/", views.ProjectDetailAPIView.as_view(), name="project_detail"), # GET, PUT, PATCH, DELETE

    path("api/v1/projects/<int:pk>/members/", views.ProjectMemberAPIView.as_view(), name="create_list_member"), # GET, POST
    path("api/v1/projects/<int:project_pk>/members/<int:user_pk>/", views.RemoveProjectMemberAPIView.as_view(), name="delete_member"), # DELETE

]

