from django.shortcuts import render, get_object_or_404
from .models import Desafio

def detalhe_desafio(request, desafio_id):
    desafio = get_object_or_404(Desafio, id=desafio_id)
    return render(request, 'challenges/templates/detalhe_desafio.html', {'desafio': desafio})
