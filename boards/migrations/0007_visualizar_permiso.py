# Generated by Django 4.2.2 on 2023-07-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_alter_boards_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visualizar_Permiso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
