from django.urls import path
from movie.views import ActorView, MovieView

urlpatterns = [
    path('/actors', ActorView.as_view()),
    path('/movies', MovieView.as_view())
]