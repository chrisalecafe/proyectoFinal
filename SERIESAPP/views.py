from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from .forms import CapituloForm, PersonajeForm, LocalidadForm
from .models import Personaje, Aparicion, Rodaje, Localidad, Capitulo
from django.contrib.auth.decorators import login_required

# Create your views here.
def localidad_list(request):
    localidades = Localidad.objects.filter().order_by("id")
    return render(request,'SERIESAPP/listadoL.html', {'localidades':localidades})

@login_required
def localidad_nuevo(request):
    if request.method == "POST":
        formulario = LocalidadForm(request.POST)
        if formulario.is_valid():
            localidad = Localidad.objects.create(nombre=formulario.cleaned_data['nombre'], direccion = formulario.cleaned_data['direccion'], pais = formulario.cleaned_data['pais'], descripcion = formulario.cleaned_data['descripcion'])
            return redirect('localidad_list')

            messages.add_message(request, messages.SUCCESS, 'P guardado')
    else:
        formulario = LocalidadForm()

    return render(request, 'SERIESAPP/localidad_editar.html', {'formulario': formulario})

@login_required
def localidad_detail(request, pk):
    post = get_object_or_404(Localidad, pk=pk)
    if request.method == "POST":
        formulario = LocalidadForm(request.POST, instance=post)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.save()
            return redirect('localidad_list')
    else:
        formulario = LocalidadForm(instance=post)
    return render(request, 'SERIESAPP/localidad_detail.html', {'formulario': formulario, 'upnew': "Update Post"})

@login_required
def localidad_delete(request, pk):
    capitulo = get_object_or_404(Localidad, pk=pk)
    capitulo.delete()
    return redirect('localidad_list')


###################################################################
def personaje_list(request):
    personajes = Personaje.objects.filter().order_by("id")
    return render(request,'SERIESAPP/listadoP.html', {'personajes':personajes})

@login_required
def personaje_nuevo(request):
    if request.method == "POST":
        formulario = PersonajeForm(request.POST)
        if formulario.is_valid():
            personaje = Personaje.objects.create(nombre=formulario.cleaned_data['nombre'], edad = formulario.cleaned_data['edad'], raza = formulario.cleaned_data['raza'], descripcion = formulario.cleaned_data['descripcion'])
            return redirect('personaje_list')

            messages.add_message(request, messages.SUCCESS, 'P guardado')
    else:
        formulario = PersonajeForm()

    return render(request, 'SERIESAPP/personaje_editar.html', {'formulario': formulario})

@login_required
def personaje_detail(request, pk):
    post = get_object_or_404(Personaje, pk=pk)
    if request.method == "POST":
        formulario = PersonajeForm(request.POST, instance=post)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.save()
            return redirect('personaje_list')
    else:
        formulario = PersonajeForm(instance=post)
    return render(request, 'SERIESAPP/personaje_detail.html', {'formulario': formulario, 'upnew': "Update Post"})

@login_required
def personaje_delete(request, pk):
    capitulo = get_object_or_404(Personaje, pk=pk)
    capitulo.delete()
    return redirect('personaje_list')

#cccccccccccccccccccccccccaaaaaaaaaaaaaaaappppppppppppppppppppiiiiiiiiiiiiiiiiitttttttttttuuuuuuuuuuullllllllloooooo
def capitulo_list(request):
    capitulos = Capitulo.objects.filter().order_by("serie")
    return render(request,'SERIESAPP/listado.html', {'capitulos':capitulos})

@login_required
def capitulo_detail(request, pk):
    capitulo = get_object_or_404(Capitulo, pk=pk)
    if request.method == "POST":
        formulario = CapituloForm(request.POST, instance=capitulo)
        if formulario.is_valid():
            capitulo = formulario.save(commit=False)
            capitulo.save()
            for personaje_id in request.POST.getlist('personajes'):
                aparicion =Aparicion(personaje_id=personaje_id, capitulo_id = capitulo.id)
                aparicion.save()
            for localidad_id in request.POST.getlist('localidades'):
                rodaje = Rodaje(localidad_id=localidad_id, capitulo_id = capitulo.id)
                rodaje.save()

            return redirect('capitulos_list')
    else:
        formulario = CapituloForm(instance=capitulo)
    return render(request, 'SERIESAPP/capitulo_detail.html', {'formulario': formulario, 'upnew': "Update Cap"})

@login_required
def capitulo_delete(request, pk):
    capitulo = get_object_or_404(Capitulo, pk=pk)
    capitulo.delete()
    return redirect('capitulos_list')

@login_required
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
                return redirect('capitulos_list')

            messages.add_message(request, messages.SUCCESS, 'Capitulo guardado')
    else:
        formulario = CapituloForm()

    return render(request, 'SERIESAPP/capitulo_editar.html', {'formulario': formulario})
