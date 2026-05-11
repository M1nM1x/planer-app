from django.urls import path, include
from users import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls))
]

