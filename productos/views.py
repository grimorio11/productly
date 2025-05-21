from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .forms import ProductoForm
from .models import Producto


# Create your views here.
def index(request):
    productos = Producto.objects.all()
    # productos = Producto.objects.filter(stock__gt=0)
    #print(productos)
    #return JsonResponse(list(productos), safe=False)
    return render(
        request, 
        'index.html', 
        context ={'productos': productos}
        )

def detalle(request, producto_id):
    # #return HttpResponse(f"Detalle del producto {producto_id}")
    # try:
    #     producto = Producto.objects.get(id=producto_id)
    # except Producto.DoesNotExist:
    #     return HttpResponse("Producto no encontrado", status=404)
    #     #raise Http404("Producto no encontrado")
    producto = get_object_or_404(Producto, id=producto_id)
    
    return render(
        request, 
        'detalle.html', 
        context ={'producto': Producto.objects.get(id=producto_id)}
        )

def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = ProductoForm()
    
    return render(
        request, 
        'formulario.html', 
        {'form': form}
    )