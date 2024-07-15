from django.urls import path
from .views import detalhe_desafio

urlpatterns = [
    path('detalhe_desafio/<int:desafio_id>/', detalhe_desafio, name='detalhe_desafio'),
]
