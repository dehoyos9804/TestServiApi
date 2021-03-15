

### TestServiApi

Test de habilidades generales área de desarrollo - Serviinformación

## Requisitos

- [**Python**](https://www.python.org/downloads/) 3.7.x
- [**Django**](https://www.python.org/downloads/) 3.1.7x
- [**Mysql**](https://www.mysql.com/downloads/) 
- [**virtualenv**](https://virtualenv.pypa.io/en/stable/) (Recomendado)

## Instalación de este repositorio

Clonar este repositorio y alojarlo en una carpeta conveniente.

```shell
git clone https://github.com/dehoyos9804/TestServiApi.git
```

## Activar virtualenv entorno Windows

```shell
\> python -m venv env
\> env/scripts/activate
```

## Instalar las dependencias

Una vez dentro del entorno, instalar las dependencias:

```sh
(env) pip install -r requirements.txt
```

## Iniciando Aplicación

A continuación se describe arrancar el programa :

### 1. Correr migraciones y servidor

una ves instalados la dependencias, se corre los siguientes comandos uno seguido del otro, (recuerda que tienes que tener acceso a mysql)

```sh
(env) python manage.py makemigrations
(env) python manage.py migrate
(env) python manage.py runserver
```

### 2. Crear un superusuario

para crear el superusuario solo basta con implementar el siguiente código, dentro del entorno del proyecto:

```shell
(env) python manage.py createsuperuser
```

### 3. Iniciar Sesión Como Administrador

una ves que el sistema este iniciado dirígete a http://127.0.0.1/admin e inicias sesión con el superusuario creado

### 4. Obtener el client_id

una ves inicies sesión, ya puedes obtener el CLIENT_ID Y CLIENT_SECRET, para esto dirígete a http://127.0.0.1:8000/o/applications/  aquí podrás crear una nueva aplicación.

- [ ] **Client_tye**: confidential
- [ ] **Authorization Grant Type**: password 



## Descripción de los Endpoints

### Registrar un usuario

**endpoint** : http://127.0.0.1:8000/authentication/register/

```json
{
    "username":"user001",
    "first_name":"prueba",
    "last_name":"prueba prueba",
    "password":"@1234567#"
}
```

### Obtener Token

**endpoint** : http://127.0.0.1:8000/authentication/login/

```json
{
    "username":"user001",
    "password":"@1234567#"
}
```

## Colección Postman

colección para ver los endpoint de pruebas que se realizaron

https://www.getpostman.com/collections/4ae531c4a61d4ed12ba6



⌨️ con ❤️ por [AldairDeHoyos](https://github.com/dehoyos9804) 😊

