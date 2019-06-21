from django.contrib import admin
from .models import Movie,Director
from django.contrib.admin import SimpleListFilter

# Register your models here.
# admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Movie)
