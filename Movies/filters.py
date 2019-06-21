import django_filters
from Movies.models import Movie

class TenMostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Movie
        fields = {'title': ['icontains'],
        }
