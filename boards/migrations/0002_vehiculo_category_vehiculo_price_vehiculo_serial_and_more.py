# Generated by Django 4.2.2 on 2023-07-13 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='category',
            field=models.CharField(max_length=20, null=True, verbose_name='categoria'),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='price',
            field=models.CharField(max_length=20, null=True, verbose_name='precio'),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='serial',
            field=models.CharField(max_length=50, null=True, verbose_name='serial carroceria'),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='serial_motor',
            field=models.CharField(max_length=50, null=True, verbose_name='serial motor'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='description',
            field=models.CharField(max_length=100, verbose_name='modelo'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='title',
            field=models.CharField(max_length=20, verbose_name='marca'),
        ),
    ]
