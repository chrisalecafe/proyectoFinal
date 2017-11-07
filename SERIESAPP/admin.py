from django.contrib import admin
from SERIESAPP.models import Personaje,PersonajeAdmin, Localidad, LocalidadAdmin, Capitulo, CapituloAdmin

admin.site.register(Personaje, PersonajeAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Capitulo, CapituloAdmin)

# Register your models here.
