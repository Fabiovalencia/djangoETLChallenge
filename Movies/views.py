from rest_framework import generics
from .models import Director,Movie,Actor,MovieActor,Plot
from .serializers import DirectorSerializer, MovieSerializer, ActorMovieSerializer,PlotSerializer
from django.shortcuts import get_object_or_404

def film_list(request):
	films= Movie.object.all()
	filter = FilmFilter(request.GET, queryset = movies)
	return render(request, 'Movies/my_template.html', {'filter' : filter})

#class DirectorList(generics.ListCreateAPIView):
class DirectorList(generics.ListAPIView):
    # queryset = Director.objects.all().filter(director_name = 'James Cameron')
    serializer_class = DirectorSerializer
    def get_queryset(self):
        #director = self.kwargs['director_name']
        return Director.objects.filter(id_director = 1)
    # def get_object(self):
    #     queryset = self.get_queryset()
    #     obj = get_object_or_404(
    #         queryset,
    #         pk=self.kwargs['pk'],
    #     )
    #     return obj
class MovieList(generics.ListAPIView):
    # queryset = Director.objects.all().filter(director_name = 'James Cameron')
    serializer_class = MovieSerializer
    def get_queryset(self):
        director = self.kwargs['director_name']
        director_obj = Director.objects.filter(director_name = director)
        return Movie.objects.filter(movie_director_name = director_obj[0].id_director).order_by('movie_year')

class ActorMovieList(generics.ListAPIView):
    serializer_class = ActorMovieSerializer
    def get_queryset(self):
        actor_obj = Actor.objects.filter(actor_name = self.kwargs['actor_name'])
        id_actor = actor_obj[0].id_actor
        movie_obj = MovieActor.objects.filter(id_actor_id = id_actor)
        movie_key = []
        for i in movie_obj:
            movie_key.append(i.id_movie_id)
        return Movie.objects.filter(id_movie__in = movie_key)

class PlotMovieList(generics.ListAPIView):
    serializer_class = PlotSerializer
    def get_queryset(self):

        return Movie.objects.filter(movie_genres = 1)
