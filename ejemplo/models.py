from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
        
    def __str__(self):
        return f"{self.nombre}, {self.numero_pasaporte}, {self.direccion}, {self.id}"


class Mascota(models.Model):
    animal = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.animal}, {self.nombre}"
        

class Automovil(models.Model):
    marca = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.marca}, {self.color}"

