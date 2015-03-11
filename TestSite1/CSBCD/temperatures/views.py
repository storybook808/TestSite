from django.shortcuts import render
import json

def chart_data_json(request):
    data = {}
    params = request.GET
    
    name = params.get('name', '')
    
    if name == 'get_tempF':
        data['chart_data'] = ChartData.get_tempF()
    
    return HttpResponse(json.dumps(data), content_type = 'application/json') 

