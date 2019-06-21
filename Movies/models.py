from django.db import models
from django.utils import timezone
# Create your models here.
class Color(models.Model):
    id_color = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length = 200)
    def __str__(self):
        return self.color_name

class Plot(models.Model):
    id_plot = models.AutoField(primary_key=True)
    plot_name = models.CharField(max_length = 200)
    def __str__(self):
        return self.plot_name

class ContentRate(models.Model):
    id_contentrate = models.AutoField(primary_key=True)
    contentrate_name = models.CharField(max_length = 200)
    def __str__(self):
        return self.contentrate_name

class Director(models.Model):
    id_director = models.AutoField(primary_key=True)
    director_name = models.CharField(max_length = 200)
    def __str__(self):
        return self.director_name

class Actor(models.Model):
    id_actor = models.AutoField(primary_key=True)
    actor_name = models.CharField(max_length = 200)
    def __str__(self):
        return self.actor_name

class Country(models.Model):
    id_country = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length = 200)
    def __str__(self):
        return self.country_name

class Language(models.Model):
    id_language = models.AutoField(primary_key=True)
    language_name = models.CharField(max_length = 200)
    def __str__(self):
        return self.language_name

class Movie(models.Model):

    id_movie = models.AutoField(primary_key=True)
    movie_title = models.CharField(max_length = 200)
    movie_director_name = models.ForeignKey('Director',on_delete = models.CASCADE)
    movie_imdb_link = models.CharField(max_length = 200, null=True)
    movie_country = models.ForeignKey('Country',on_delete = models.CASCADE)
    movie_language = models.ForeignKey('Language',on_delete = models.CASCADE)
    movie_budget = models.BigIntegerField()
    movie_year = models.IntegerField()
    movie_imdb_score = models.DecimalField(max_digits=8,decimal_places=4)
    movie_aspect_ratio = models.DecimalField(max_digits=8,decimal_places=4)
    movie_facebook_likes = models.IntegerField()
    movie_num_voted_users =  models.IntegerField()
    movie_gross = models.IntegerField()
    movie_color = models.ForeignKey('Color',on_delete = models.CASCADE)
    movie_duration = models.IntegerField()
    movie_director_facebook_likes = models.IntegerField()
    movie_cast_total_facebook_likes = models.IntegerField()
    movie_content_rate = models.ForeignKey('ContentRate',on_delete = models.CASCADE)
    movie_facenumber_in_poster = models.IntegerField()
    movie_num_critc_for_review = models.IntegerField()
    movie_num_user_for_reviews = models.IntegerField()
    movie_genres = models.ManyToManyField(Plot)
    
    def __str__(self):
        return self.movie_title

class MovieActor(models.Model):
    id_actor = models.ForeignKey('Actor',on_delete = models.CASCADE)
    id_movie = models.ForeignKey('Movie',on_delete = models.CASCADE)
    def __str__(self):
        return self.id_actor

class PlotMovie(models.Model):
    id_movie = models.ForeignKey('Movie',on_delete = models.CASCADE)
    id_plot = models.ForeignKey('Plot',on_delete = models.CASCADE)
    def __str__(self):
        return self.id_movie
