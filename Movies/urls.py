from django.conf.urls import url
from Movies.views import *

urlpatterns = [
    url(r'^directors/$', DirectorList.as_view(),name='directors'),
    url(r'^directedby/(?P<director_name>.+)/$', MovieList.as_view()),
    #url(r'^moviesbyactor/(?P<id_actor>.+)/$', ActorMovieList.as_view()),
    url(r'^moviesbyactor/(?P<actor_name>.+)/$', ActorMovieList.as_view()),
    url(r'^plotmovies/$', PlotMovieList.as_view()),
]
