from django.shortcuts import render, render_to_response, RequestContext
from chartit import DataPool, Chart
from .models import TemperatureOverTimeChart

# Create your views here.
def charts(request):
    return render_to_response("charts.html",
                              locals(),
                              context_instance=RequestContext(request))

def monthchart(request):
    return render_to_response("monthchart.html",
                              locals(),
                              context_instance=RequestContext(request))

def temperaturechart(request):
    return render_to_response("temperaturechart.html",
                              locals(),
                              context_instance=RequestContext(request))

def windspeedchart(request):
    return render_to_response("windspeedchart.html",
                              locals(),
                              context_instance=RequestContext(request))

def temperatureovertimechart(request):
    ds = DataPool(
           series=
            [{'options': {
                'source': TemperatureOverTimeChart.objects.all()},
              'terms': [
                'timestamp',
                'tempF', 
                'tempC']}
             ])

    cht = Chart(
            datasource = ds, 
            series_options = 
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'timestamp': [
                    'tempF',
                    'tempC']
                  }}],
            chart_options = 
              {'title': {
                   'text': 'Temperature Over Time'},
                'xAxis': {
                    'title': {
                       'text': 'Time'}},
                'yAxis': {
                    'title': {
                       'text': 'Temperature'}}})
    #end_code
    return render_to_response("charts.html",
                              {'chart_list': cht})    
    
def chart_data_json(request):
    data = {}
    params = request.GET
    days = params.get('days', 0)
    name = params.get('name', '')
    
    if names == 'get_tempF':
        data['chart_data'] = ChartData.get_tempF()
        
    return HttpResponse(json.dumps(data), content_type = 'application/json')
