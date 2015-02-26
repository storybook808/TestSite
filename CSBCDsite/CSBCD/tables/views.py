from django.shortcuts import render, render_to_response, RequestContext

import json

# Create your views here.
def tables(request):
    return render_to_response("tables.html",
                              locals(),
                              context_instance=RequestContext(request))

def temperaturetable(request):
    return render_to_response("temperaturetable.html",
                              locals(),
                              context_instance=RequestContext(request))

def windspeedtable(request):
    return render_to_response("windspeedtable.html",
                              locals(),
                              context_instance=RequestContext(request))

def monthtable(request):
    return render_to_response("monthtable.html",
                              locals(),
                              context_instance=RequestContext(request))


# Charting
def chart_data_json(request):
    data = {}
    params = request.GET
    
    name = params.get('name', '')
    
    if name == 'tempF':
        data['chart_data'] = ChartData.get_tempF()
        
        return HttpResponse(json.dumps(data), content_type='application/json')
