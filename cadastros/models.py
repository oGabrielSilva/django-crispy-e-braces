from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Base(models.Model):
    class Meta:
        abstract = True

    criado = models.DateField('Data de criação', auto_now_add=True)
    atualizado = models.DateField('Atualizado em: ', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True) 

class Campo(Base):
    nome = models.CharField(max_length=60, verbose_name='Nome')
    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    servidor = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return '{} ({}) - {}'.format(self.nome, self.descricao, self.servidor)

class Atividade(Base):
    numero = models.IntegerField(verbose_name='Número')
    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    pontos = models.DecimalField(decimal_places=1, max_digits=4)
    detalhes = models.CharField(max_length=100)
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)
    servidor = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return '{} - {} ({})'.format(self.numero, self.descricao, self.campo.nome)

class Campus(Base):
    class Meta:
        verbose_name_plural = 'Campus'

    nome = models.CharField(max_length=60)
    cidade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100, verbose_name='Endereço')
    telefone = models.CharField(max_length=11)
    servidor = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
