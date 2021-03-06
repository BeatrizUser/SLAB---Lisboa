# Generated by Django 4.0.4 on 2022-05-11 08:08

import cadastro.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=75)),
                ('nome_completo_aluno', models.CharField(max_length=255)),
                ('data_de_Nascimento_do_Aluno', models.DateField(default=datetime.datetime(2022, 5, 11, 8, 8, 23, 797852, tzinfo=utc), verbose_name='data_de_Nascimento_do_Aluno')),
                ('morada', models.CharField(max_length=200)),
                ('nome_completo_responsavel', models.CharField(max_length=255)),
                ('documento_de_id', models.CharField(max_length=20)),
                ('email_do_responsavel', models.EmailField(max_length=75)),
                ('foto', models.ImageField(blank=True, null=True, upload_to=cadastro.models.upload_image_aluno)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('nome_completo_aluno',),
            },
        ),
    ]
