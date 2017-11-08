from django.conf.urls import url
from . import views

urlpatterns = [

      url(r'^$', views.capitulo_list,name='capitulo_list'),
      url(r'^capitulos/$', views.capitulo_list,name='capitulos_list'),
      url(r'^capitulo/nuevo/$', views.capitulo_nuevo, name='capitulo_nuevo'),
      url(r'^capitulo/(?P<pk>[0-9]+)/$', views.capitulo_detail, name='capitulo_detail'),
      url(r'^capitulo/(?P<pk>\d+)/eliminar/$', views.capitulo_delete, name='capitulo_delete'),

      url(r'^personajes/$', views.personaje_list,name='personaje_list'),
      url(r'^personaje/nuevo/$', views.personaje_nuevo, name='personaje_nuevo'),
      url(r'^personaje/(?P<pk>[0-9]+)/$', views.personaje_detail, name='personaje_detail'),
      url(r'^personaje/(?P<pk>\d+)/eliminar/$', views.personaje_delete, name='personaje_delete'),

       url(r'^localidad/$', views.localidad_list,name='localidad_list'),
       url(r'^localidad/nuevo/$', views.localidad_nuevo, name='localidad_nuevo'),
       url(r'^localidad/(?P<pk>[0-9]+)/$', views.localidad_detail, name='localidad_detail'),
       url(r'^localidad/(?P<pk>\d+)/eliminar/$', views.localidad_delete, name='localidad_delete'),



    ]
