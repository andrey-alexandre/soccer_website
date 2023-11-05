from django.shortcuts import render
from django.http import HttpResponse
import django_tables2 as tables 

import json
import gspread
import pandas as pd

from matches.script.one import action

from .filters import MatchesFilter
from .models import Matches, MatchesAgg
from .tables import MatchesTable

# Create your views here.        
def home(request):
    queryset_agg = MatchesAgg.objects.all()#filter(GameId_id__in=[1187978, 1187977])  # Você pode personalizar a consulta conforme necessário
    
    myFilter = MatchesFilter(request.GET, queryset=queryset_agg)
    queryset = Matches.objects.filter(GameId__in=set(myFilter.qs.values_list('GameId_id', flat=True)))
    table = MatchesTable(queryset)   
    
    context = {'myFilter': myFilter, 'table': table}

    return render(request, 'matches/matches.html', context)

def refresh(request):    
    if request.method == 'GET':
        return render(request, 'matches/refresh.html', {'data': ''})
    elif request.method == "POST": 
        data = action() #the function you want to call 
        return render(request, 'matches/refresh.html', {'data':data})    

def output(request):
    if request.is_ajax():
        py_obj = 1+1
        return render(request, 'matches/output.html', {'output': py_obj})