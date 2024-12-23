# ti2041-2024

**Descripción del Proyecto**

"Gestión de Productos S.A." es una aplicación web sencilla que permite a los administradores registrar productos y consultar la lista de productos registrados. Los datos se almacenan temporalmente en memoria mientras el servidor esté en ejecución.

Funcionalidades

**Registro de Productos**: Permite registrar productos con los siguientes datos:
   - Código
   - Nombre
   - Marca
   - Fecha de vencimiento

**Requisitos**
Para ejecutar este proyecto en tu entorno local, asegúrate de tener instalados los siguientes requisitos:
- **Python 3.10+**
- **Django 4.2+**

**super user**
 Ve a http://127.0.0.1:8000/admin/.
 Name: admin
 Contraseña: inacap2024
 Mail: danilo.moreno02@gmail.com

**user login**
 Name: usuario2
 Contraseña: 123456


 **Medidas de Seguridad Aplicadas**
 1_Autenticación de Usuarios con el Decorador @login_required
 Para garantizar que solo los usuarios autenticados puedan acceder a las páginas de gestión de productos, se ha utilizado el decorador @login_required de Django.
 2_Autorización Basada en Grupos de Usuario
 El acceso a las funcionalidades de gestión de productos está restringido a los usuarios que pertenecen al grupo ADMIN_PRODUCTS
 3_Protección Contra CSRF (Cross-Site Request Forgery)
 Django implementa automáticamente protección contra ataques CSRF, los cuales intentan ejecutar solicitudes no autorizadas en nombre del usuario.



Inicia el servidor local de Django:
python manage.py runserver

Abre tu navegador y navega a:
http://127.0.0.1:8000

Desde ahí, puedes:
Registrar nuevos productos en la página de registro.
Consultar los productos ya registrados en la página de consulta.

Autor
Danilo Moreno

