from django.conf.urls import url,patterns,include

from . import views


urlpatterns = patterns(
    '',
    url(r'^list/$',views.entrada_lista, name='entrada_lista'),
    url(r'^entrada/(?P<pk>\d+)/$',views.entrada_detalle,\
        name='entrada_detalle'),
 )










