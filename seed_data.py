from ejemplo.models import Familiar
Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()
print("Se cargo con éxito los usuarios de pruebas")



from ejemplo.models import Mascota
Mascota(animal="Perro", nombre="Roi").save()
Mascota(nombre="Gato", nombre="Lolo").save()
Mascota(nombre="Caballo", nombre="Juan").save()
Mascota(nombre="Perro", nombre="Dori").save()
print("Se cargo con éxito los usuarios de pruebas")