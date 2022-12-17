# proyecto-famia

a- Abro VSC
b- En la terminal "Clone git repository" URL del proyecto actual
c- En la terminal "python manage.py migrate" "python manage.py runserver"
d- ctrl + c sobre el link a la pagina
e- En la terminal "python manage.py shell import seed_data"


Ejemplo para aregar AUTOMOVIL

a- En MODELS creo un modelo automovil
b- En FORMS importo el modelo y creo una clase AutomovilForm
c- En VIEWS importo el modelo automovil y en FORMS automovilform y genero la clase mostrar_automovil y genero Altaautomovil
d- Creo el TEMPLATE automovil
e- creo el TEMPLATE alta_automovil
f- En URLS importo altaautomovil y mostrar automovil y genero los dos paths
g- python manage.py runserver


Para guardar en el remoto

a- git add . (si quiero guardar todo), sino git add "nombre del archivo"
b- git commit -m "nombre de la modificacion"
c- git push origin main
