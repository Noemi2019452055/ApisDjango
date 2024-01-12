from django.db import models



# Create your models here.

        
class Respuestaschatbot(models.Model):
    marca_temporal = models.DateTimeField()
    nombre_completo = models.CharField(max_length=100)
    pregunta1 = models.CharField(max_length=2)
    pregunta2 = models.TextField()
    pregunta3 = models.CharField(max_length=10)
    pregunta4 = models.TextField()
    pregunta5 = models.TextField()
    pregunta6 = models.CharField(max_length=20)
    pregunta7 = models.CharField(max_length=10)

    def str(self):
        return str(self.nombre_completo)
    
    
##########################################################################################
        #pruebas de testing
        # models.pyS

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_stock = models.PositiveIntegerField()
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta {self.id} - Cliente: {self.cliente.nombre}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"DetalleVenta {self.id} - Venta: {self.venta.id}, Producto: {self.producto.nombre}"
