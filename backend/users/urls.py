from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views

urlpatterns = [
    path("api/v1/user/me/", views.CurrentUserAPIView.as_view(), name='user'),
    path("api/v1/register/", views.RegisterUserAPIView.as_view(), name='register'),
    path('api/v1/logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('api/v1/delete/me/', views.DeleteUserAPIView.as_view(), name='delete'),

    path('api/v1/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

