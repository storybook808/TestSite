from django.shortcuts import render
from django.http import HttpResponse
from .models import Temperature
import simplejson

def chart_data_json(request):
    data = {}
    
    data['chart_data'] = ChartData.get_tempF()
  
    return HttpResponse(json.dumps(data), content_type = 'application/json') 

