# Generated by Django 4.0.5 on 2023-07-13 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_boards_alter_vehiculo_category_alter_vehiculo_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boards',
            options={'permissions': (('es_miembro_1', 'es miembro con prioridad 1'),)},
        ),
    ]