from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dashboards.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^temperaturechart', 'charts.views.temperaturechart', name='temperaturechart'),
    url(r'^windspeedchart', 'charts.views.windspeedchart', name='windspeedchart'),
    url(r'^monthchart', 'charts.views.monthchart', name='monthchart'),
    
    url(r'^temperaturetable', 'tables.views.temperaturetable', name='temperaturetable'),
    url(r'^windspeedtable', 'tables.views.windspeedtable', name='windspeedtable'),
    url(r'^monthtable', 'tables.views.monthtable', name='monthtable'),

    url(r'^tables', 'tables.views.tables', name='tables'),
    url(r'^charts', 'charts.views.charts', name='charts'),
    
    url(r'^analysis', 'analysis.views.analysis', name='analysis'),
    
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)