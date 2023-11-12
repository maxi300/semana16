from django.db import models

#creacion de la bd como clases
#la app es gestionPedidos

#ESTAS NO SON LAS QUE PIDIO, LAS QUE PIDIO SE ENCUENTRAN EN LA LINEA 59
# SE CREAN LOS NOMBRES DE LAS TABLAS EN ESTE CASO SE LLAMA CLIENTES Y SE LE COLOCA LOS CAMPOS
class Clientes(models.Model):
    nombre= models.CharField(max_length=30)
    direccion= models.CharField(max_length=30,verbose_name="la direccion")
    email= models.EmailField(blank=True, null=True)#asi es para que el campo sea formato null sin problema
    tfno=models.CharField(max_length=8, verbose_name="telefono")

#ES PARA QUE DEVUELVA EN CADENA CUANDO SEA LLAMADO POR OTRAS CLASES
    def __str__(self) :
        return 'el nombre es %s su direccion es %s su correo es %s y su telefono es %s' %(self.nombre, self.direccion, self.email, self.tfno)


class Articulos(models.Model):
    nombre= models.CharField(max_length=30)
    seccion= models.CharField(max_length=30)
    precio=models.IntegerField()

    def __str__(self) :
        return 'el nombre es %s su seccion %s su precio %s' %(self.nombre, self.seccion, self.precio)


class Pedidos(models.Model):
    numero= models.IntegerField()
    direccion= models.DateField(verbose_name="fecha")
    entregado= models.BooleanField()

    def __str__(self) :
        return 'el numero de pedidos %s' %self.numero


class Occidente(models.Model):
    numero= models.IntegerField()
    direccion= models.DateField(verbose_name="fecha")
    entregado= models.BooleanField()














# Create your models here.



class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.PositiveIntegerField(max_length=3)
    dui=models.PositiveIntegerField(max_length=9)


    def __str__(self):
        return self.nombre + "  " + self.apellido
    #definiendo el modelo Area
class Area(models.Model):
    nombre_del_area=models.CharField(max_length=50)
    descripcion=models.CharField()

    def __str__(self):
        return self.nombre_del_area
    #definiendo el modelo Empleado
class Empleado(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.PositiveIntegerField(max_length=3)
    areaId=models.ForeignKey(Area, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre + "  " + self.apellido
    #definiendo el modelo venta
class Venta(models.Model):
    fecha_venta=models.DateTimeField()
    monto=models.FloatField()
    clienteId=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleadoId=models.ForeignKey(Empleado,on_delete=models.CASCADE)



    def __str__(self):
        return "venta total: $%s" %self.monto
