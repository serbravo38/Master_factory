from django.db import models

class Cliente(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.correo} ({self.nombre})"

class Solicitud(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)  # Si es el nombre de la solicitud, está bien.
    cantidad = models.PositiveSmallIntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)


    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.cantidad)
