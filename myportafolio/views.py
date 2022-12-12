from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import View
from django.http import Http404
from .models import PortafolioModel
from django.core.paginator import Paginator
#from ipware import get_client_ip
#import mysql

from myportafolio.forms import loginform, CustomUserCreationForm, PortafolioForm
from django.contrib.auth import authenticate, login
# Create your views here.
'''
def ip(request):
    if request.method=="GET":
        client_ip, is_routable = get_client_ip(request)
        conexion = mysql.connect('db.sqlite3')
        conexion.execute("insert into Portfolio_ips(ip,enrutable) values (?,?)", (f"{client_ip}", f"{is_routable}"))
        conexion.commit()
        conexion.close()
    return render(request, 'index.html')
'''

class index(View):
    template_get = 'index.html'
    def get(self, request):
        return render(request, self.template_get, {})
class detalles(View):
    template_get = 'portfolio-details.html'
    def get(self, request):
        return render(request, self.template_get, {})

class PortafolioView(View):
    template_get = 'portafolios/PortafolioView.html'
    def get(self, request):
        return render(request, self.template_get, {})

class formlogin(View):
    template_get = 'registration/login.html'
    def get(self, request):
        context ={}
        context['form'] = loginform()
        return render(request, self.template_get, context)
''''
class agregar_portafolio(View):
    template_get = 'portafolios/agregar.html'
    def get(self, request):
        context ={}
        context['form'] = PortafolioForm()
        if request.method == 'POST':
            formulario = PortafolioForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Agregado correctamente")
                return redirect(to="listar")
            else:
                context["form"] = formulario
        return render(request, self.template_get, context)
'''
def agregar_portafolio(request):
    data = {
        'form': PortafolioForm()
    }
    if request.method == 'POST':
        formulario = PortafolioForm(data = request.POST, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado correctamente")
            return redirect(to="agregar_portafolio")
        else:
            data["form"] = formulario

    return render(request, 'portafolios/agregar.html', data)

def listar(request):
    productos =PortafolioModel.objects.all()

    #Si page no existe en url del navegador, devuelve la pagina 1
    page = request.GET.get('page', 1)

    try:
        # 5 productos x pagina, y los muestra segun valor de "page"
        paginator = Paginator(productos, 2)
        productos = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': productos,  # entity para uso de paginador
        'paginator': paginator
    }

    return render(request, 'portafolios/listar.html', data)

"""
class registro(View):
    template_get = 'registration/registro.html'

    def get(self, request):
        context ={}
        context['form'] = CustomUserCreationForm()

        if request.method == 'POST':
            formulario = CustomUserCreationForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()

                # loguear al usuario terminado el registro
                user = authenticate(username=formulario.cleaned_data["username"],
                                    password=formulario.cleaned_data["password1"])
                login(request, user)
                messages.success(request, "Registro Correcto")
                return redirect(to="agregar_portafolio")

            context["form"] = formulario
        return render(request, 'registration/registro.html', context)
"""
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()

            #loguear al usuario terminado el registro
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro Correcto")
            return redirect(to="index")

        data["form"] = formulario
    return render(request, 'registration/registro.html', data)
