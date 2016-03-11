from django.shortcuts import (render,
                              get_object_or_404, render_to_response)

from django.views import generic
from .models import Entrada
# Create your views here.


def entrada_detalle(request, pk):
    #entrada = get_object_or_404(Entrada, pk = pk)

    #return render(request, 'blog/entrada/detail.html',\
    #              {'entrada':entrada})

    identrada = Entrada.objects.get(pk=int(pk))
    return render( request,'blog/entrada/detalle.html', \
                               {'entrada':identrada,'usuario':request.user})
def entrada_lista(request):
    entradas = Entrada.objects.all().order_by('-fecha')
    return render(request, 'blog/entrada/list.html',\
                  {'entradas':entradas})


