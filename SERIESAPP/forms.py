from django import forms

from .models import Personaje, Localidad, Capitulo


class CapituloForm(forms.ModelForm):
    class Meta:
        model = Capitulo
        fields = ('titulo', 'serie', 'fecha', 'personajes', 'localidades')

class PersonajeForm(forms.ModelForm):
    class Meta:
        model = Personaje
        fields = ('nombre', 'edad', 'raza', 'descripcion')

class LocalidadForm(forms.ModelForm):
    class Meta:
        model = Localidad
        fields = ('nombre', 'direccion', 'pais', 'descripcion')


def __init__ (self, *args, **kwargs):
    super(CapituloForm, self).__init__(*args, **kwargs)
    self.fields["personajes"].widget = forms.widgets.CheckboxSelectMultiple()
    self.fields["personajes"].help_text = "Ingrese los personajes de este capitulo"
    self.fields["personajes"].queryset = Personaje.objects.all()
    self.fields["localidades"].widget = forms.widgets.CheckboxSelectMultiple()
    self.fields["localidades"].help_text = "Ingrese las localidades de este capitulo"
    self.fields["localidades"].queryset = Localidad.objects.all()
