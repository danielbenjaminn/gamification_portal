from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
from .forms import CustomAuthenticationForm
from challenges.models import DesafioAtribuido, Pontuacao
from django.db.models import Sum

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'login.html'

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        if user.is_superuser:
            return redirect('/admin')
        else:
            return redirect('user_dashboard')

def get_desafios_pendentes(user):
    return DesafioAtribuido.objects.filter(corretor=user, aceito=False, data_interacao__isnull=True)

def get_desafios_aceitos(user):
    return DesafioAtribuido.objects.filter(corretor=user, aceito=True)

def get_pontuacoes(user):
    return Pontuacao.objects.filter(corretor=user)

def get_pontuacao_total(desafio):
    return Pontuacao.objects.filter(desafio=desafio).aggregate(total_pontos=Sum('pontos'))['total_pontos']

def user_dashboard(request):
    user = request.user

    # Filtrar desafios atribuídos pendentes
    desafios_pendentes = get_desafios_pendentes(user)

    # Filtrar desafios atribuídos aceitos
    desafios_aceitos = get_desafios_aceitos(user)

    # Calcular pontuação total para cada desafio aceito
    for desafio_atribuido in desafios_aceitos:
        desafio_atribuido.pontuacao_total = get_pontuacao_total(desafio_atribuido.desafio)

    context = {
        'desafios_pendentes': desafios_pendentes,
        'desafios_aceitos': desafios_aceitos,
    }
    return render(request, 'user_dashboard.html', context)

def aceitar_desafio(request, desafio_id):
    desafio_atribuido = get_object_or_404(DesafioAtribuido, id=desafio_id, corretor=request.user)
    if request.method == "POST":
        desafio_atribuido.aceito = True
        desafio_atribuido.data_interacao = timezone.now()
        desafio_atribuido.save()
        return redirect('user_dashboard')
    return render(request, 'aceitar_desafio.html', {'desafio_atribuido': desafio_atribuido})

def recusar_desafio(request, desafio_id):
    desafio_atribuido = get_object_or_404(DesafioAtribuido, id=desafio_id, corretor=request.user)
    if request.method == "POST":
        desafio_atribuido.data_interacao = timezone.now()
        desafio_atribuido.save()
        return redirect('user_dashboard')
    return render(request, 'recusar_desafio.html', {'desafio_atribuido': desafio_atribuido})

def redirect_to_login(request):
    return redirect('login')
