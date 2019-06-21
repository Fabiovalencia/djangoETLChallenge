from django.test import TestCase
from Movies.models import Director,Movie
# Create your tests here.

class DirectorTestCase(TestCase):
    def setUp(self):
        Director.objects.create(director_name="coco")

class MoviesTestCase(TestCase):
    def setUp(self):
        Movies.objects.create(movie_title="Coco")
