from django.db import models
from django.utils.encoding import smart_unicode


# Create your models here.
class TemperatureOverTimeChart(models.Model):
    tempF = models.DecimalField(max_digits = 5, decimal_places = 2)
    tempC = models.DecimalField(max_digits = 5, decimal_places = 2)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    
    def __unicode__(self):
        return smart_unicode(self.timestamp)
