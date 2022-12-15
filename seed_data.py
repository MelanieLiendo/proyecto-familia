from ejemplo.models import Familiar
Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()
print("Se cargo con éxito los usuarios de pruebas")



from ejemplo.models import Mascota
Mascota(animal="Perro", nombre="Roi").save()
Mascota(animal="Gato", nombre="Lolo").save()
Mascota(animal="Caballo", nombre="Juan").save()
Mascota(animal="Perro", nombre="Dori").save()
print("Se cargo con éxito los usuarios de pruebas")

from ejemplo.models import Automovil
Automovil(marca="toyota", color="gris").save()
Automovil(marca="honda", color="gris").save()
Automovil(marca="fiat", color="gris").save()
Automovil(marca="renault", color="gris").save()
print("Se cargo con éxito los usuarios de pruebas")