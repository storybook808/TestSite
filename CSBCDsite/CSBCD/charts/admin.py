from django.contrib import admin

# Register your models here.
from .models import TemperatureOverTimeChart

class TemperatureOverTimeChartAdmin(admin.ModelAdmin):
    class Meta:
        model = TemperatureOverTimeChart

admin.site.register(TemperatureOverTimeChart, TemperatureOverTimeChartAdmin)