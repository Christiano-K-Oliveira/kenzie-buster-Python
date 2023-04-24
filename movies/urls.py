from django.urls import path
from . import views


# Create your views here.
urlpatterns = [
    path('movies/', views.MovieView.as_view()),
    path('movies/<int:movie_id>/', views.MovieIdView.as_view())
]
