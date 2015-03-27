from django.shortcuts import render
from django.http import HttpResponse
from .models import Temperature
import json

def chart_data_json(request):
    to_json = {}
    to_json['dates'] = 0;
    to_json['values'] = 1;

    return HttpResponse(json.dumps(to_json), mimetype = 'application/json') 

