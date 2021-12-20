from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UsuarioCreate

urlpatterns = [
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/cadastro', UsuarioCreate.as_view(), name='cadastrar-usuario'),
]
