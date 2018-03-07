# Generated by Django 2.0.3 on 2018-03-07 22:20

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
            name='AACC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('cargaHoraria', models.DecimalField(decimal_places=1, max_digits=200, verbose_name='Carga horária')),
                ('instituicao', models.CharField(max_length=200, verbose_name='Instituição')),
                ('local', models.CharField(max_length=200)),
                ('dataCurso', models.DateField(verbose_name='Data do curso')),
                ('dataEmissao', models.DateField(verbose_name='Data de emissão')),
                ('relatorio', models.TextField(blank=True, verbose_name='Relatório')),
                ('anexo', models.FileField(blank=True, default=None, upload_to='')),
                ('linkExterno', models.CharField(blank=True, max_length=200, verbose_name='Link externo')),
                ('tipoAtividade', models.CharField(choices=[('1a', 'Eventos - Participação'), ('1b', 'Eventos - Apresentação de trabalho'), ('1c', 'Eventos - Interpretação'), ('1d', 'Eventos - Organização'), ('2a', 'Defesas - Participação'), ('2b', 'Defesas - Interpretação'), ('3a', 'Pesquisa - Participação como pesquisador'), ('3b', 'Pesquisa - Participação como contribuidor de dados'), ('4a', 'Extensão - Participação em projetos'), ('4b', 'Extensão - Participação como aluno'), ('4b', 'Extensão - Participação como especialista'), ('5a', 'Ensino - Monitoria em Letras-Libras'), ('5b', 'Ensino - Docência em Libras'), ('6a', 'Publicação - Resumos'), ('6b', 'Publicação - Artigos completos'), ('6b', 'Publicação - Material didático'), ('7a', 'Atividades culturais - Participação'), ('7b', 'Atividades culturais - Atuação')], default=('1a', 'Eventos - Participação'), max_length=200)),
                ('ISSN', models.IntegerField(blank=True, null=True)),
                ('ISBN', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField(unique=True, verbose_name='Matrícula')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='aacc',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aaccs.Aluno'),
        ),
        migrations.AddField(
            model_name='aacc',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]