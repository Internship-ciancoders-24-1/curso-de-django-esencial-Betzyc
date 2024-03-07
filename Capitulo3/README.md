# Modulos
## Comandos

### Crear apps

python manage.py startapp users

### Pillow intall

pip install pillow

### Comandos de migración

python manage.py migrate  //Refleja los cambios en la base de datos
python manage.py makemigrations //Busca cambios en los modelos y los refleja en un archivo

python manage.py shell // shell de python

### Correr Servidor

python manage.py runserver

## CRUD

### Create in consola

from posts.models impor User

pablo= User.objects.create(
	email='Hola@gmail.com'
	password=
	first_name=
	last_name=
)

### Otra forma

arturo = User() //se crea una instancia de arturno
arturo.email = 'arturo@platzi.com'
arturo.password='12345'
arturo.is_admin=True
arturo.first_name='Arturo'
arturo.last_name='Martinez'
arturo.save()

### update in consola

pablo.email= 'pablo@gmail.com'
pablo.save()

### Delete in consula
arturo.delete()


### Importar diccionarios

from post.models import User

for user in users:
	obj = User(**user)
	obj.save()
	print(obj.pk, ':', obj.email,':')


## Querys
### Get obtiene solamente un objeto

from post.models import User
user = User.objects.get(email='freddier@platzi.com')
user
type(user)
user.pk // imprime el id de freddier
user.email //imprime el email de freddier

### Filter trae los que coinciden con el query, puede traer mas de un objeto
platzi_users= User.objects.filter(email__endswith = '@platzi.com')
platzi_users

### all trae todos los objetos en la lista

users= User.objects.all()
users

### Update

#### actualiza a administradores todos los usuarios que tienen el email con el dominio platzi

platzi_users = User.objects.filter(email__endswith = '@platzi.com').update(is_admin=True)

## PRACTICAS
### Practica Usuario

![] (Capitulo3/posts.png)

### Implementación de modelo usuario

![] (Capitulo3/4.impl-mod-user-cod.png)
![] (Capitulo3/4.impl-mod-user.png)