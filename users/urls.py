from django.urls import path
from .views import UsersView, LoginView
from rest_framework_simplejwt import views


urlpatterns = [
    path('users/', UsersView.as_view()),
    path('users/login/', LoginView.as_view())
]
