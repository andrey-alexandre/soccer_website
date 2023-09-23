from django_filters import FilterSet
from .models import *

class MatchesFilter(FilterSet):
    class Meta:
        model = Matches
        fields = '__all__'