from ninja import NinjaAPI, Router
from .models import Categoria, Marca
from typing import List
from ninja.security import HttpBearer
from rest_framework_simplejwt.authentication import JWTAuthentication

# Clase para la autenticación JWT
class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            jwt_auth = JWTAuthentication()
            validated_token = jwt_auth.get_validated_token(token)
            user = jwt_auth.get_user(validated_token)
            return user  # Si el token es válido, retorna el usuario
        except Exception:
            return None  # Si el token no es válido, deniega acceso

# Instancia principal de NinjaAPI
api = NinjaAPI()

# Endpoints abiertos
@api.get("/categorias", response=List[str])
def obtener_categorias(request):
    """
    Endpoint abierto para obtener la lista de categorías.
    """
    categorias = Categoria.objects.values_list("nombre", flat=True)
    return list(categorias)

@api.get("/marcas", response=List[str])
def obtener_marcas(request):
    """
    Endpoint abierto para obtener la lista de marcas.
    """
    marcas = Marca.objects.values_list("nombre", flat=True)
    return list(marcas)

# Router con seguridad para endpoints protegidos
secure_router = Router(auth=JWTAuth())

@secure_router.put("/producto/{codigo}")
def modificar_producto(request, codigo: str, payload: dict):
    """
    Endpoint protegido para modificar un producto.
    """
    # request.auth contiene el usuario autenticado
    user = request.auth
    # Lógica para modificar el producto con los datos en `payload`
    return {"detail": f"Producto {codigo} modificado exitosamente.", "user": user.username}

# Registrar el router protegido en la instancia principal
api.add_router("/secure", secure_router)
