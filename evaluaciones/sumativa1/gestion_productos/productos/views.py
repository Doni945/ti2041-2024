from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Producto

# Lista para almacenar productos registrados
productos_registrados = []

def despliegue_productos(request):
    # Simulación de datos para los menús desplegables
    marcas = ['Marca A', 'Marca B', 'Marca C']
    categorias = ['Categoría 1', 'Categoría 2', 'Categoría 3']
    caracteristicas = ['Característica X', 'Característica Y', 'Característica Z']
    
    # Aplicar filtros
    productos = Producto.objects.all()
    
    if 'marca' in request.GET and request.GET['marca']:
        productos = productos.filter(marca=request.GET['marca'])
    
    if 'categoria' in request.GET and request.GET['categoria']:
        productos = productos.filter(categoria=request.GET['categoria'])
    
    if 'caracteristicas' in request.GET and request.GET['caracteristicas']:
        productos = productos.filter(caracteristicas=request.GET['caracteristicas'])
    
    return render(request, 'despliegue_productos.html', {
        'productos': productos,
        'marcas': marcas,
        'categorias': categorias,
        'caracteristicas': caracteristicas,
    })



def lista_productos(request):
    productos = Producto.objects.all()  # Obtener todos los productos del modelo
    return render(request, 'index.html', {'productos': productos})

def registro_producto(request):
    if request.method == 'POST':
        producto = {
            'codigo': request.POST['codigo'],
            'nombre': request.POST['nombre'],
            'marca': request.POST['marca'],
            'fecha_vencimiento': request.POST['fecha_vencimiento'],
        }
        productos_registrados.append(producto)
        return redirect('resultado_producto')
    return render(request, 'registro.html')  # Ajustar la ruta

def resultado_producto(request):
    if productos_registrados:  # Asegúrate de que la lista no esté vacía
        return render(request, 'resultado.html', {'producto': productos_registrados[-1]})
    return redirect('consulta_productos')  # Redirige si no hay productos registrados

def consulta_productos(request):
    return render(request, 'consulta.html', {'productos': productos_registrados})  # Ajustar la ruta

def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_productos')  # Redirige a la lista de productos después de iniciar sesión
        else:
            # Manejo de error si el inicio de sesión falla
            return render(request, 'login.html', {'error': 'Nombre de usuario o contraseña incorrectos.'})
    return render(request, 'login.html')  # Asegúrate de que el nombre sea correcto









