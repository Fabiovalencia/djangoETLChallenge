from .models import Director, Movie, MovieActor,Plot
from rest_framework import serializers

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Director
        fields = ('id_director','director_name')

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_title','movie_year')

class ActorMovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('id_movie','movie_title')

class PlotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('id_movie','movie_title')
