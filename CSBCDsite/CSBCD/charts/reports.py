from datetime import datetime, timedelta

import core
from .models import TemperatureOverTimeChart

class ChartData(object):
    @classmethod
    def get_tempF(cls):
        tempF_data = TemperatureOverTimeChart.objects.values('timestamp', 'tempF')
        
        return tempF_data