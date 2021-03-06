# Generated by Django 2.2.12 on 2021-12-19 00:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('atualizado', models.DateField(auto_now=True, verbose_name='Atualizado em: ')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=60)),
                ('cidade', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=11)),
            ],
            options={
                'verbose_name_plural': 'Campus',
            },
        ),
        migrations.CreateModel(
            name='Campo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('atualizado', models.DateField(auto_now=True, verbose_name='Atualizado em: ')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=60, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('atualizado', models.DateField(auto_now=True, verbose_name='Atualizado em: ')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
                ('pontos', models.DecimalField(decimal_places=1, max_digits=4)),
                ('detalhes', models.CharField(max_length=100)),
                ('campo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Campo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
