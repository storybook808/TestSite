from django.db import models
from django.utils.encoding import smart_unicode

class Temperature(models.Model):
    timestamp =  models.DateTimeField(auto_now_add = True, auto_now = False)
    value = models.DecimalField(max_digits = 7, decimal_places = 3)    
    
    def __unicode__(self):
        return smart_unicode(self.timestamp)

    def tempF(self):
        return self.value
