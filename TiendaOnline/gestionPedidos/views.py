from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos,Clientes, Pedidos,Cliente,Area,Empleado,Venta
#from TiendaOnline import settings
from django.conf import settings
from django.core.mail import send_mail
from gestionPedidos.forms import FormularioContacto


def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

 





 
def buscar(request):

    if request.GET["prd"]:
      # mensaje="articulo buscado: %r "    %request.GET["prd"]
      producto= request.GET["prd"]
      if len(producto)>20:
          mensaje="texto de busqueda demasiado largo"
      else:
      
         articulos= Articulos.objects.filter(nombre__icontains=producto) #esto es para filtrar lo de articulos es como un select 
         return render(request,"resultados_busqueda.html",{"articulos":articulos, "query":producto})#tenemos que query es lo que se guarda en lo que escribimos en el input 
    else:
        mensaje="no haz introducido nada"

    return HttpResponse(mensaje)







#se puede de esta forma sencilla los formularios
#def contacto(request):
    if request.method=="POST":

        subject= request.POST["asunto"]
        message= request.POST["mensaje"] +" " + request.POST["email"]#de donde se envia el mail 
        email_from= settings.EMAIL_HOST_USER
        recipient_list=["ramosmax487@gmail.com"]#es quien recibe los correos

        send_mail=(subject,message,email_from,recipient_list)




        return render(request, "gracias.html")

    return render(request,"contacto.html")




#tambien se puede con api forms ya que asi queda validado



def contacto(request):
    if request.method=="POST":

        miformulario= FormularioContacto(request.POST)#traer toda la informacion del formulario

        if miformulario.is_valid():

            infForm= miformulario.cleaned_data   #guardar la informacion aqui

            send_mail(infForm["asunto"],infForm["mensaje"], infForm.get('email',''),["ramosmax487@gmail.com"] )

            return render(request, "gracias.html")


    else:
        miformulario= FormularioContacto()#construir formulario vacio en caso de que no lo hayan llenado
     




        

    return render(request,"formulario_contacto.html",{"form":miformulario})

#este es el metodo con el que mostraremos las tablas
#Articulos.objects.all() significa que selecciones todo los registros de esa tabla
#y se almacenan en la variable articulos lo mismo pasa con las otras

def mostrar(request):
    #Cliente,Area,Empleado,Venta
    articulos= Articulos.objects.all()
    clientes= Clientes.objects.all()
    pedidos= Pedidos.objects.all()

    cliente= Cliente.objects.all()
    area= Area.objects.all()
    empleado=Empleado.objects.all()
    venta= Venta.objects.all()




    return render(request,"mostrar.html", {"articulos":articulos, "clientes":clientes,"pedidos":pedidos,"cliente":cliente ,"area":area,"empleado":empleado,"venta":venta})



# Create your views here. aqui se escribe el nombre del archivo html y en el diccionario clave valor
#las variables valores y se les asigna una clave para identificarlas
