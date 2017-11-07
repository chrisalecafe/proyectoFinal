from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^capitulo/nuevo/$', views.capitulo_nuevo, name='capitulo_nuevo'),
    ]
