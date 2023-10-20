from django.db import models

# Create your models here.
class encuestaSatisfaccion(models.Model):
    pregunta1 = models.TextField(db_column='¿Con qué frecuencia realizas compras en línea?')
    pregunta2 = models.TextField(db_column='¿Cómo te enteraste de nuestra tienda en línea?')
    pregunta3 = models.TextField(db_column='¿Qué tipo de productos sueles comprar en tiendas en línea?')
    pregunta4 = models.TextField(db_column='¿Cuál es tu método de pago preferido al comprar en línea?')
    pregunta5 = models.TextField(db_column='¿Cuál es tu rango de edad?')
    pregunta6 = models.TextField(db_column='¿Qué factores influyen más en tu decisión de compra en línea?')
    pregunta7 = models.TextField(db_column='¿Te gustaría recibir ofertas y noticias de nuestra tienda en línea por correo electrónico?')
    pregunta8 = models.TextField(db_column='¿Qué te impulsaría a recomendar nuestra tienda en línea a amigos o familiares?')
    pregunta9 = models.TextField(db_column='¿Qué dispositivo utilizas principalmente para realizar compras en línea?')
    pregunta10 = models.TextField(db_column='¿Qué consideras más importante al elegir una tienda en línea?')
class Meta:
        db_table: 'encuestaSatisfaccion'
        
