from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm

class UsuarioCreate(CreateView):
    template_name = 'cadastros/form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('index')
