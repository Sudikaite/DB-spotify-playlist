from django.urls import path
from .views import (index, spotify_tracks)

urlpatterns = [
    path('', index, name='index'),
    path('spotify-tracks/', spotify_tracks, name='spotify_tracks'),
]