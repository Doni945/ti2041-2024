from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import Group
from django.utils.timezone import now

# Lista temporal para almacenar productos
productos_registrados = []

def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Autenticar usuario usando el sistema de Django
        user = authenticate(request, username=username, password=password)
        if user is not None:  # Si las credenciales son válidas
            login(request, user)  # Inicia sesión

            # Configurar variables de sesión
            request.session['username'] = user.username
            request.session['fecha_conexion'] = now().strftime('%Y-%m-%d %H:%M:%S')
            request.session['is_admin_products'] = user.groups.filter(name='ADMIN_PRODUCTS').exists()

            return redirect('lista_productos')  # Redirige a la lista de productos
        else:
            # Si las credenciales son incorrectas
            return render(request, 'login.html', {'error': 'Nombre de usuario o contraseña incorrectos.'})
    
    return render(request, 'login.html')  # Mostrar la página de login

@login_required
@never_cache
def lista_productos(request):
    # Validar si el usuario tiene el grupo ADMIN_PRODUCTS
    if not request.session.get('is_admin_products', False):
        return redirect('acceso_denegado')

    # Muestra todos los productos registrados
    return render(request, 'index.html', {'productos': productos_registrados})

@login_required
@never_cache
def registro_producto(request):
    # Validar si el usuario tiene el grupo ADMIN_PRODUCTS
    if not request.session.get('is_admin_products', False):
        return redirect('acceso_denegado')

    if request.method == 'POST':
        producto = {
            'codigo': request.POST['codigo'],
            'nombre': request.POST['nombre'],
            'marca': request.POST['marca'],
            'fecha_vencimiento': request.POST['fecha_vencimiento'],
        }
        productos_registrados.append(producto)  # Agrega a la lista en memoria
        return redirect('resultado_producto')
    return render(request, 'registro.html')

@login_required
@never_cache
def resultado_producto(request):
    if productos_registrados:
        return render(request, 'resultado.html', {'producto': productos_registrados[-1]})
    return redirect('lista_productos')

@login_required
@never_cache
def consulta_productos(request):
    return render(request, 'consulta.html', {'productos': productos_registrados})

@login_required
def cerrar_sesion(request):
    # Cierra la sesión completamente
    logout(request)
    return redirect('login')  # Redirige al login

@login_required
@never_cache
def despliegue_productos(request):
    # Validar si el usuario tiene el grupo ADMIN_PRODUCTS
    if not request.session.get('is_admin_products', False):
        return redirect('acceso_denegado')

    # Simulación de datos para los menús desplegables
    marcas = ['Marca A', 'Marca B', 'Marca C']
    categorias = ['Categoría 1', 'Categoría 2', 'Categoría 3']
    caracteristicas = ['Característica X', 'Característica Y', 'Característica Z']
    
    productos = []  # Lista vacía, ya que no usamos base de datos

    return render(request, 'despliegue_productos.html', {
        'productos': productos,
        'marcas': marcas,
        'categorias': categorias,
        'caracteristicas': caracteristicas,
    })

def acceso_denegado(request):
    # Vista para mostrar acceso denegado
    return render(request, 'acceso_denegado.html', {'mensaje': 'No tienes permisos para acceder a esta página.'})





