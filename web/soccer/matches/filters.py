import django_filters
from django import forms

from .models import *


class MatchesFilter(django_filters.FilterSet):
    t1_metric = django_filters.NumberFilter(field_name='Goal_T1', label='Métrica T1:', lookup_expr='gte',
                                           widget=forms.NumberInput(attrs={'step': 0.1}))
    t2_metric = django_filters.NumberFilter(field_name='Goal_T2', label='Métrica T2:', lookup_expr='gte',
                                           widget=forms.NumberInput(attrs={'step': 0.1}))
    date_filter = django_filters.DateTimeFilter(field_name='Data', label='Data:', lookup_expr='gte',widget=forms.DateInput())
    
    class Meta:
        model = MatchesAgg
        fields =  []
        