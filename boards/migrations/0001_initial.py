# Generated by Django 4.2.2 on 2023-07-13 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='marca')),
                ('description', models.CharField(max_length=255, verbose_name='modelo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')),
            ],
            options={
                'verbose_name': 'vehiculo',
                'verbose_name_plural': 'vehiculos',
                'ordering': ['-created'],
            },
        ),
    ]
