# Generated by Django 4.0.4 on 2022-05-13 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_alter_cadastro_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='alergia',
            field=models.CharField(choices=[('Nao possui Alergia', 'Nao'), ('Possui Alergia', 'Sim')], default=1, max_length=100, verbose_name='Possui Alergias?'),
            preserve_default=False,
        ),
    ]
