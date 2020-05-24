from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movies_pk>/like/', views.like, name='like'),
    path('<int:movies_pk>/overview/', views.overview, name='overview'),
    
]
