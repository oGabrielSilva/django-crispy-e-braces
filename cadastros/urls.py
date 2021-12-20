from django.urls import path

from .forms import CampoCreate, AtividadeCreate, CampusCreate
from .forms import UpdateCampo, UpdateAtividade, UpdateCampus
from .forms import DeleteCampo, DeleteAtividade, DeleteCampus
from .forms import ListCampo, ListAtividade, ListCampus 

urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
    path('cadastrar/campus/', CampusCreate.as_view(), name='cadastrar-campus'),

    #Updates urls
    path('editar/campo/<int:pk>/', UpdateCampo.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>/', UpdateAtividade.as_view(), name='editar-atividade'),
    path('editar/campus/<int:pk>/', UpdateCampus.as_view(), name='editar-campus'),

    #Delete urls
    path('delete/campo/<int:pk>/', DeleteCampo.as_view(), name='delete-campo'),
    path('delete/atividade/<int:pk>/', DeleteAtividade.as_view(), name='delete-atividade'),
    path('delete/campus/<int:pk>/', DeleteCampus.as_view(), name='delete-campus'),

    #List urls
    path('listar/campo/', ListCampo.as_view(), name='listar-campo'),
    path('listar/atividade/', ListAtividade.as_view(), name='listar-atividade'),
    path('listar/campus/', ListCampus.as_view(), name='listar-campus'),
]
