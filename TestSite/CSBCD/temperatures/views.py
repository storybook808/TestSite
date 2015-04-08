from django.shortcuts import render
from django.http import HttpResponse
from .models import Temperature
import json

def chart_data_json(request):
    to_json = []
    for i in range(10):
        data_dict = {}
        data_dict['timestamp'] = i
        data_dict['values'] = i
        to_json.append(data_dict)        
    response_data = json.dumps(to_json)
    return HttpResponse(response_data, content_type="application/json")
