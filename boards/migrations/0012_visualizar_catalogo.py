# Generated by Django 4.0.5 on 2023-07-13 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0011_delete_visualizar_catalogo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visualizar_Catalogo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
