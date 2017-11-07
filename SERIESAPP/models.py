from django.db import models
from django.contrib import admin
# Create your models here.
class Personaje(models.Model):

    nombre  =   models.CharField(max_length=300)
    edad  =   models.CharField(max_length=100)
    raza  =   models.CharField(max_length=30)
    descripcion  =   models.CharField(max_length=400)

    def __str__(self):
        return self.nombre

class Localidad(models.Model):

    nombre  =   models.CharField(max_length=300)
    direccion  =   models.CharField(max_length=300)
    pais =   models.CharField(max_length=300)
    descripcion  =   models.CharField(max_length=400)

    def __str__(self):
        return self.nombre

class Capitulo(models.Model):

    titulo    = models.CharField(max_length=300)
    serie    = models.CharField(max_length=300)
    fecha      = models.DateField()
    personajes   = models.ManyToManyField(Personaje, through='Aparicion')
    localidades   = models.ManyToManyField(Localidad, through='Rodaje')

    def __str__(self):

        return self.titulo

class Aparicion(models.Model):
    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE)
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)

class Rodaje(models.Model):

    localidad= models.ForeignKey(Localidad, on_delete=models.CASCADE)

    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)

class AparicionInLine(admin.TabularInline):

    model = Aparicion
    extra = 1


class PersonajeAdmin(admin.ModelAdmin):

    inlines = ( AparicionInLine,)

class RodajeInLine(admin.TabularInline):

    model = Rodaje
    extra = 1

class LocalidadAdmin(admin.ModelAdmin):

    inlines = ( RodajeInLine,)

class CapituloAdmin(admin.ModelAdmin):

    inlines = (AparicionInLine, RodajeInLine,)
