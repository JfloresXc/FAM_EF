from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponseRedirect
from miapp.models import Producto
from django.contrib import messages

# from .forms import CourseForm
# Create your views here.
layout = """"""
def inicio(request):
    return render(request, 'inicio.html')

def integrantes(request):
    integrantes = ['🧑 Jose Flores Chamba','🧑 Edson Alva Chanta','🧑 Miguel Motta Mendoza']
    return render(request, 'integrantes.html', {
        'titulo':'Integrantes del proyecto',
        'integrantes':integrantes
    })


def crearcursos(request):
    return render(request, 'crear-curso.html')

def crearproductos(request):
    return render(request, 'crear-producto.html')

def cursos(request):
    # cursos = Course.objects.raw('SELECT * FROM miapp_course')
    return render(request, 'cursos.html', {'cursos': []})

def formularioCurso(request):
    return render(request, 'curso-agregar.html')

def crear_producto(request):
    # RECIBE DATOS DEL FORMULARIO
    codigo = request.GET['codigo']
    nombre = request.GET['nombre']
    precio_compra = request.GET['precio_compra']
    precio_venta = request.GET['precio_venta']
    fecha_compra = request.GET['fecha_compra']
    estado = request.GET['estado']
    # CREAR OBJETO PRODUCTO
    producto = Producto(
        codigo = codigo,
        nombre = nombre,
        precio_venta = precio_venta,
        precio_compra = precio_compra,
        fecha_compra = fecha_compra,
        estado = estado
    )
    # GUARDA OBJETO
    producto.save()
    # MUESTRA MENSAJE FLASH
    messages.add_message(request, messages.SUCCESS, "Producto agregado con éxito")

    return redirect('/crearproductos/')

def productos(request):
    productos = Producto.objects.raw('SELECT * FROM miapp_producto')
    return render(request, 'productos.html', {'productos': productos})

def agregarCarrera(request):
    return render(request, 'carrera-agregar.html')




