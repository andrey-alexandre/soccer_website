from django.shortcuts import render
from django.http import HttpResponse

import json
import gspread
import pandas as pd

from matches.script.one import action


# Create your views here.
def home(request):
    gc = gspread.service_account(filename='Soccer.json')
    sh = gc.open("Soccer")
    worksheet = sh.worksheet('Soccer')
    df = pd.DataFrame(worksheet.get_all_records())
    df = df.head(10)
    
    json_records = df.reset_index().to_json(orient ='records')
    json_data = []
    json_data = json.loads(json_records)
    
    context = {'data': df}
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