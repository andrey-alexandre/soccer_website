import django_filters
from django import forms

from .models import *


class MatchesFilter(django_filters.FilterSet):
    attr_dict = {'step': 0.1, 'class': 'form-control', 'margin':'10px'}
    t1_goal = django_filters.NumberFilter(field_name='Goal_T1', label='Gols no HT:', lookup_expr='gte',
                                           widget=forms.NumberInput(attrs=attr_dict))
    t2_goal = django_filters.NumberFilter(field_name='Goal_T2', label='Gols no FT:', lookup_expr='gte',
                                           widget=forms.NumberInput(attrs=attr_dict))
    t1_corner = django_filters.NumberFilter(field_name='Corner_T1', label='Escanteios no HT:', lookup_expr='gte',
                                           widget=forms.NumberInput(attrs=attr_dict))
    t2_corner = django_filters.NumberFilter(field_name='Corner_T2', label='Escanteios no FT:', lookup_expr='gte',
                                           widget=forms.NumberInput(attrs=attr_dict))
    t1_win = django_filters.NumberFilter(field_name='Win_T1', label='Vitórias no HT:', lookup_expr='gte',
                                           widget=forms.NumberInput(attrs=attr_dict))
    t2_win = django_filters.NumberFilter(field_name='Win_T2', label='Vitórias no FT:', lookup_expr='gte',
                                           widget=forms.NumberInput(attrs=attr_dict))   
    date_filter= django_filters.DateTimeFromToRangeFilter(
        label='Data:',field_name='Data', widget=django_filters.widgets.RangeWidget(attrs={'placeholder': 'yyyy-mm-dd hh:mm'})
    ) 
    
    class Meta:
        model = MatchesAgg
        fields =  []
        