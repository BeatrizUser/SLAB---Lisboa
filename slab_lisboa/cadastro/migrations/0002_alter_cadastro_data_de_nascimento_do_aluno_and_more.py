# Generated by Django 4.0.4 on 2022-05-11 09:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='data_de_Nascimento_do_Aluno',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de Nascimento do Aluno'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='email_do_responsavel',
            field=models.EmailField(max_length=75, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='nome_completo_responsavel',
            field=models.CharField(max_length=255, verbose_name='Nome do Responsavel'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Campo preenchido automaticamente'),
        ),
    ]
