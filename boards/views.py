from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from .forms import VehiculoForm, UserRegisterForm, VehiculoForm


from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

# se agrega authenticate y el formulario para el login en nuestro sistema
from django.contrib.auth.forms import AuthenticationForm

# para la gestion de permisos
from .models import Visualizar_Catalogo, Vehiculo
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# mixins
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# para las vistas basadas en funciones podemos usar otras herramientas
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.

def Index(request):
    context = {"inicio": Index}
    return render(request, "boards/index.html", context)


def registro_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            content_type = ContentType.objects.get_for_model(
                Visualizar_Catalogo)
            visualizar_catalogo = Permission.objects.get(
                codename="visualizar_catalogo",
                content_type=content_type
            )
            user = form.save()  # aqui ya tenemos el objeto user
            user.user_permissions.add(visualizar_catalogo)

            login(request, user)
            messages.success(request, "Registrado Satisfactoriamente")
        else:
            messages.error(request, "Registro Invalido")
        return HttpResponseRedirect("/")

    form = UserRegisterForm()
    context = {"register_form": form}
    return render(request, "boards/registro.html", context)


def login_view(request):
    if request.method == "POST":  # preguntamos si el metodo es tipo post o get
        # rellenamos el formulario de autenticacion con los datos post
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():  # preguntamos si los datos son validos
            # si es valido. nos devuelve true
            # obtenemos el dato y limpiamos el campo username
            username = form.cleaned_data.get("username")
            # obtenemos el dato y limpiamos el campo password
            password = form.cleaned_data.get("password")
            # autentificamos al usuario
            user = authenticate(username=username, password=password)
            # si no existe el usuario o no autentifica devuelve NONE
            if user is not None:
                login(request, user)
                messages.info(request, f"iniciaste sesion como {username}.")
                return HttpResponseRedirect("/")
            else:
                messages.error(request, "username o password incorrectos")
                return HttpResponseRedirect("/login/")
        else:
            messages.error(request, "username o password incorrectos")
            return HttpResponseRedirect("/login/")

    form = AuthenticationForm()
    context = {"login_form": form}
    return render(request, "boards/login.html", context)


def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesion correctamente")
    return HttpResponseRedirect("/login/")


# @login_required(login_url="/login/")
# @permission_required(perm="boards.visualizar_catalogo", raise_exception=True)
@login_required(login_url="/login/")
@permission_required(perm="boards.add_vehiculomodel", raise_exception=True)
def formulario_view(request):
    # logica de si se trata de una solicitud post
    if request.method == "POST":
        # crear una instancia del formulario con los datos ingresados
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()  # guardamos los datos ingresados en el formulario de la base de datos
            # procesamos y validamos los datos
            return HttpResponseRedirect("/")
    else:
        # si es un metodo GET
        form = VehiculoForm()
        context = {"form": form}
        return render(request, "boards/formulario.html", context)


@login_required(login_url="/login/")
def listado(request):
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        if vehiculo.price < 10000:
            vehiculo.condicion = 'Bajo'
        elif 10000 <= vehiculo.price < 30000:
            vehiculo.condicion = 'Medio'
        else:
            vehiculo.condicion = 'Alto'
    return render(request, "boards/listado.html", {'vehiculos': vehiculos})
