from django.shortcuts import render, redirect

# Lista para almacenar productos registrados
productos_registrados = []

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


