from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404

from .models import Campo, Atividade, Campus

################### Create ###################

class CampoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = 'login'
    group_required = u'Admin'
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campo')

    def form_valid(self, form):
        form.instance.servidor = self.request.user
        return super().form_valid(form)

class AtividadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = 'login'
    group_required = u'Admin'
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividade')

    def form_valid(self, form):
        form.instance.servidor = self.request.user
        return super().form_valid(form)

class CampusCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = 'login'
    group_required = u'Admin'
    model = Campus
    fields = ['nome', 'cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campus')

    def form_valid(self, form):
        form.instance.servidor = self.request.user
        return super().form_valid(form)

################### Update ###################

class UpdateCampo(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = 'login'
    group_required = u'Admin'
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campo')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Campo, pk=self.kwargs['pk'], servidor=self.request.user)
        return self.object

class UpdateAtividade(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = 'login'
    group_required = u'Admin'
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividade')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Atividade, pk=self.kwargs['pk'], servidor=self.request.user)
        return self.object

class UpdateCampus(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = 'login'
    group_required = u'Admin'
    model = Campus
    fields = ['nome', 'cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campus')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Campus, pk=self.kwargs['pk'], servidor=self.request.user)
        return self.object

################### Delete ###################

class DeleteCampo(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = 'login'
    group_required = u'Admin'
    model = Campo
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-campo')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Campo, pk=self.kwargs['pk'], servidor=self.request.user)
        return self.object

class DeleteAtividade(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = 'login'
    group_required = u'Admin'
    model = Atividade
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-atividade')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Atividade, pk=self.kwargs['pk'], servidor=self.request.user)
        return self.object

class DeleteCampus(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = 'login'
    group_required = u'Admin'
    model = Campus
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-campus')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Campus, pk=self.kwargs['pk'], servidor=self.request.user)
        return self.object

################### List ###################

class ListCampo(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = (u'Admin', u'Docente')
    model = Campo
    template_name = 'cadastros/lista/campo.html'

    def get_queryset(self):
        self.object_list = Campo.objects.filter(servidor=self.request.user)
        return self.object_list

class ListAtividade(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = (u'Admin', u'Docente')
    model = Atividade
    template_name = 'cadastros/lista/atividade.html'

    def get_queryset(self):
        self.object_list = Atividade.objects.filter(servidor=self.request.user)
        return self.object_list

class ListCampus(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = (u'Admin', u'Docente')
    model = Campus
    template_name = 'cadastros/lista/campus.html'

    def get_queryset(self):
        self.object_list = Campus.objects.filter(servidor=self.request.user)
        return self.object_list
