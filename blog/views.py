from django.shortcuts import render, get_object_or_404, redirect
from .models import Articulo, Comentario, Seguidor
from .forms import ComentarioForm, SeguidorForm

def index(request):
    articulos = Articulo.objects.all().order_by('-fecha_publicacion')
    return render(request, "blog/index.html", {"articulos": articulos})

def detalle_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)
    comentarios = articulo.comentarios.all()

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = articulo
            comentario.save()
            return redirect('detalle_articulo', articulo_id=articulo.id)
    else:
        form = ComentarioForm()

    return render(request, "blog/detalle.html", {"articulo": articulo, "comentarios": comentarios, "form": form})

def seguir_blog(request):
    if request.method == "POST":
        form = SeguidorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SeguidorForm()
    return render(request, "blog/seguir_blog.html", {"form": form})

def perfil(request):
    return render(request, "blog/perfil.html")