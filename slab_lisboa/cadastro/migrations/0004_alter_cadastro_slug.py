# Generated by Django 4.0.4 on 2022-05-09 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_alter_cadastro_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
