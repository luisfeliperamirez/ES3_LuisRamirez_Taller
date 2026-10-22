from django.shortcuts import render, get_object_or_404
from .models import Album

def inicio(request):
    albumes = Album.objects.prefetch_related('canciones')
    
    # Filtro por disponibilidad (?disponible=1)
    disp = request.GET.get('disponible')
    if disp == '1':
        albumes = albumes.filter(disponible=True)
    elif disp == '0':
        albumes = albumes.filter(disponible=False)
    else:
        # Muestra todos por defecto o ajusta según lo requieras
        albumes = albumes.all()

    # Búsqueda por texto (?q=)
    q = request.GET.get('q')
    if q:
        albumes = albumes.filter(titulo__icontains=q)

    contexto = {
        'albumes': albumes
    }
    return render(request, 'catalogo/inicio.html', contexto)

def detalle_album(request, id):
    # Si el ID existe en la base de datos, mostrará la vista (aunque esté agotado).
    # Si el ID NO existe, responderá adecuadamente un error 404.
    album = get_object_or_404(Album, id=id)
    return render(request, 'catalogo/detalle.html', {'album': album})