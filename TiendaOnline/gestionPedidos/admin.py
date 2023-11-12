from django.contrib import admin
from gestionPedidos.models import Clientes,Articulos,Pedidos,Occidente,Cliente,Area,Empleado,Venta


#crear una clase en admin
class ClientesAdmin(admin.ModelAdmin):
   list_display=("nombre", "direccion","tfno")#datos que solo me muestre en la web
   search_fields=("nombre","tfno")#es un buscador y solo se busca por nombres y telefono

class ArticulosAdmin(admin.ModelAdmin):
   list_filter=("seccion",)#es un filtro para la busqueda mas rapida

admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Articulos,ArticulosAdmin)
admin.site.register(Pedidos)
admin.site.register(Occidente)
admin.site.register(Cliente)
admin.site.register(Area)
admin.site.register(Empleado)
admin.site.register(Venta)

# Register your models here.
