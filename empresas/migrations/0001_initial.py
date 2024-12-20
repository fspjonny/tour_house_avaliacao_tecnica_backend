# Generated by Django 5.1.3 on 2024-11-15 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=18, unique=True)),
                ('logradouro', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
