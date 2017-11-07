from django.shortcuts import render
from django.contrib import messages
from .forms import CapituloForm
from .models import Personaje, Aparicion, Rodaje, Localidad, Capitulo

# Create your views here.
def capitulo_nuevo(request):
    if request.method == "POST":
        formulario = CapituloForm(request.POST)
        if formulario.is_valid():
            capitulo = Capitulo.objects.create(titulo=formulario.cleaned_data['titulo'], serie = formulario.cleaned_data['serie'], fecha = formulario.cleaned_data['fecha'])
            for personaje_id in request.POST.getlist('personajes'):
                aparicion =Aparicion(personaje_id=personaje_id, capitulo_id = capitulo.id)
                aparicion.save()
            for localidad_id in request.POST.getlist('localidades'):
                rodaje = Rodaje(localidad_id=localidad_id, capitulo_id = capitulo.id)
                rodaje.save()
            messages.add_message(request, messages.SUCCESS, 'Capitulo guardado')
    else:
        formulario = CapituloForm()
    return render(request, 'SERIESAPP/capitulo_editar.html', {'formulario': formulario})
