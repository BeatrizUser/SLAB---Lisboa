# Generated by Django 4.0.4 on 2022-05-13 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_cadastro_alergia'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='contato_do_responsavel',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cadastro',
            name='idade',
            field=models.CharField(default=1, max_length=2, verbose_name='Idade'),
            preserve_default=False,
        ),
    ]
