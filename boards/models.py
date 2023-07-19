from django.db import models

# Create your models here.


class Visualizar_Catalogo(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    # buenas practicas
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class Add_vehiculomodel(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    # buenas practicas
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


CATEGORY_CHOICES = [
    ("PARTICULAR", "Particular"),
    ("TRANSPORTE", "Trasporte"),
    ("CARGA", "Carga"),
]

TITLE_CHOICES = [
    ("FIAT", "Fiat"),
    ("CHEVROLET", "Chevrolet"),
    ("FORD", "Ford"),
    ("TOYOTA", "Toyota"),
]


class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(
        max_length=20, null=True, choices=TITLE_CHOICES, default="Ford", verbose_name="marca")
    description = models.CharField(max_length=100, verbose_name="modelo")
    serial = models.CharField(max_length=50, null=True,
                              verbose_name="serial carroceria")
    serial_motor = models.CharField(
        max_length=50, null=True, verbose_name="serial motor")
    category = models.CharField(
        max_length=20, null=True, choices=CATEGORY_CHOICES, default="Particular", verbose_name="categoria")

    price = models.DecimalField(
        max_digits=10, decimal_places=0, verbose_name="precio")

    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Actualizacion")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "vehiculo"
        verbose_name_plural = "vehiculos"
        ordering = ["-created"]
