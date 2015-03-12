from django.shortcuts import render
import json

def chart_data_json(request):
    data = {}
    
    data['chart_data'] = ChartData.get_tempF()
  
    return HttpResponse(json.dumps(data), content_type = 'application/json') 

