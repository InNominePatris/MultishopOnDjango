# MultishopOnDjango

**Tabla de Contenidos**
- Instalación de Python
- Creación de la base de datos en PostgreSQL
- Instalación y configuración de entorno virtual (venv)
- Instalación y configuracion del proyecto

# Instrucciones de instalación

## Instalar Python
  
*Django esta escrito en Python. Necesitamos Python para hacer cualquier cosa en Django. Comencemos instalandolo!. Este proyecto utiliza específicamente Python en su versión 3.7.0* *el link de descarga estará abajo.*

Ve y descarga [Python 3.7.0](https://www.python.org/downloads/release/python-370/) 

Ya instalado Python procederemos a abrir nuestra terminal de comandos *cmd* mediante el comando:

`Tecla Windows + R`

Luego escribimos `cmd` y ejecutamos.

## Creación de la base de datos en PostgreSQL

Suponiendo que ya tiene instalado PosrgreSQL nos dirigimos a PgAdmin y creamos una base de datos explícitamente con el nombre `base`.

Instalación de PostgreSQL:

> La instalación de PostgreSQL no está cubierta en esta documentación. Le recomendamos tener PostgreSQL >= 11.1 instalado en su ordenador ya que la base de datos de este proyecto se rige bajo una versión >=11.1 del mismo.

## Instalación y configuración de entorno virtual (venv)

Procedemos a crear un entorno virtual para instalar luego nuestro proyecto en Django. Ya dentro de nuestra consola de comandos `cmd` escribimos el comando:

 ```
 python -m venv <nombre del entorno>    //El nombre del entorno usted lo elige, no poner <> solo el nombre
 ```              
 
Ya creado el entorno procedemos a navegar dentro del mismo, como veremos habrá una carpeta llamada *scripts*. Navegamos dentro de la carpeta scripts y escribimos el comando `activate`. 

Se mirará de esta manera:
```
C:\Users\lenovo\Desktop\prueba\Scripts>activate
```
y ejecutamos.

Luego de haber ejecutado el comando notaremos que el nombre de nuestro entorno está encerrado dentro de paréntesis como lo muestra el ejemplo:

```
(prueba) C:\Users\lenovo\Desktop\prueba\Scripts>
```
Luego salimos del directorio *scripts* y del entorno virtual *prueba* ya que lo hemos activado. Escribimos un par de veces  el comando `cd..` para salir de ambos directorios y quedaremos hasta acá:

```
(prueba) C:\Users\lenovo\Desktop>
```

# Instalación y configuracion del proyecto

## Instalación

Procedemos a descargar el proyecto desde el repositorio de GitHub [MultishopOnDjango](https://github.com/InNominePatris/MultishopOnDjango/tree/master) en la pestaña `clone or download` descargamos el proyecto como archivo `.zip` dando click en `Download zip` . Procedemos a descomprimir y tendremos una carpeta de nombre `Human-Resources`

- Volvemos a la consola de comandos. Ya con nuestro entorno virtual activado `(prueba)` navegamos a la carpeta proyecto ya descargada `MultishopOnDjango`. Nuestra dirección en la línea de comandos se verá de la siguiente manera: `(prueba) C:\Users\lenovo\Desktop\MultishopOnDjango>`

## Configuración del proyecto

Ya con Python instalado, la base de datos en PostgreSQL `base` y nuestro entorno virtual activado ademas ya dentro de la carpeta del proyecto que descargamos llamada `MultishopOnDjango` procedemos a trabajar sobre las configuraciones propias de Django para poner en funcionamiento el proyecto.

Siguiendo dentro de nuestro directorio procedemos a instalar Django y todas las librerías correspondientes contenidas en el archivo `.txt` de nombre *requirements* mediante el comando:

```

pip install -r requirements.txt
```

Y automáticamente nuestras librerías de terceros e incluyendo Django se instalarán dentro de nuestro proyecto.

Siguiendo en la misma ruta `(prueba) C:\Users\lenovo\Desktop\MultishopOnDjango> ` procederemos a ejecutar las migraciones de nuestro proyecto mediante dos comandos en orden:

```

python manage.py makemigrations
python manage.py migrate
```
Veremos como nuestras migraciones se comienzan a realizar sobre la base de datos `base` en PostgreSQL.

Luego crearemos al primer usuario mediante el comando: `python manage.py createsuperuser` el cual después de ejecutado nos abrirá las opciones las cuales procederemos a completar:

```
username:
email(optional):
password:

Superuser created successfully
```
Ya creado nuestro superusuario procederemos como último paso a levantar el servidor para que nuestra aplicación de recursos humanos funcione con normalidad mediante el comando:

```

python manage.py runserver
```
Luego de ejecutado nos mostrará un mensaje como este:

```

System check identified no issues (0 silenced).
July 16, 2019 - 23:38:40
Django version 2.0, using settings 'bd2.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
**_Dando click sobre la dirección `http://127.0.0.1:8000/` y luego de la `/` agregándole la plabra `admin` nuestro sitio comenzará a funcionar mostrándonos de entrada el Login del sistema en pantalla. La dirección final a ingresar en el navegador luego de estar corriendo el servidor sería `http://127.0.0.1:8000/admin`._**

**En el login ingresamos el nombre de usuario y contraseña anteriormente creados y  nuestro sistema _funcionará con nomalidad_ sin ningún problema.**
