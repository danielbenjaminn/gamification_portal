from django.urls import path
from .views import redirect_to_login, CustomLoginView, user_dashboard

urlpatterns = [
    path('', redirect_to_login, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
]
