from django.db import models
from accounts.models import User

class Desafio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    banner = models.ImageField(upload_to='banners/')
    regras_pontuacao = models.TextField()

    def __str__(self):
        return self.nome

class DesafioAtribuido(models.Model):
    desafio = models.ForeignKey(Desafio, on_delete=models.CASCADE)
    corretor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='desafios_atribuidos_accounts')
    aceito = models.BooleanField(default=False)
    data_interacao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.desafio.nome} - {self.corretor.cpf}"

class Pontuacao(models.Model):
    corretor = models.ForeignKey(User, on_delete=models.CASCADE)
    desafio = models.ForeignKey(Desafio, on_delete=models.CASCADE)
    pontos = models.IntegerField()

    def __str__(self):
        return f"{self.corretor.cpf} - Desafio ID: {self.desafio.id} - {self.pontos} pontos"
