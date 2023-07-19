from django.contrib import admin
from .models import Vehiculo
# Register your models here.


class VehiculoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(Vehiculo, VehiculoAdmin)
