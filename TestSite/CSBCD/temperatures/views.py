from django.shortcuts import render
from django.http import HttpResponse
from .models import Temperature
import simplejson

def chart_data_json(request):
    temperatures = Temperature.objects.all()
    to_json = []

    count = 0
    for temp in temperatures:
        temp_dict['dates'] = count
        temp_dict['values'] = temp.tempF
        to_json.append(temp_dict)
    
    response_data = simplejson.dumps(to_json)
  
    return HttpResponse(response_data, content_type = 'application/json') 

