<h1>Taller mecanico incompleto</h1>
<h3>seguir elaborando</h3>

<h4>Grupo</h4>
<ul>
    <li>Esteban Salas</li>
    <li></li>
    <li></li>
    <li></li>
</ul>

<h4>ingreso a Crud</h4>
<p>usario: admin</p>
<p>contrasena: admin</p>

<h3>pasos para hacer correr proyecto</h3>
<ol>
    <li>_    ejecutar powershell ISE como administrador</li>
    <li>_    ejecutar: set-executionpolicy remotesigned</li>
    <li>_    aceptar todo y cerrar powershell ISE</li>
    <br>
    <li>_    navegar hasta dentro de la carpeta raiz del proyecto</li>
    <li>_    en la url digitar cmd</li>
    <li>_    en cmd digitar una linea a la vez lo siguiente:</li>
    <li>_    python -m venv myvenv</li>
    <li>_    .\myvenv\Scripts\activate.bat</li>
    <p> cuidado lleva "punto" la ruta</p>
    <br>
    <li>_    python -m pip install --upgrade pip</li>
    <li>_    pip install -r requirements.txt</li>
    <li>_    por ultimo: python manage.py runserver</li>
    <li>_    abrir en un navegador la ruta: http://127.0.0.1:8000/</li>
    <li>_    para aprir el crud a la ruta agrege la palabra admin: http://127.0.0.1:8000/admin</li>

</ol>

<!-- omitir esto
Como hacer que funcione el server ahora con el environ 
1- Crear archivo que se llame .env tiene que ir en la carpeta raiz para que lo lea el manage.py y debe contener esto 
SECRET_KEY=$dmfa6(-(7^-)ak7a(lag=s0nkuj+9dfw8pd_4!i=0qok$ec2*
DEBUG=True
DJANGO_SECRET_KEY=ivjauvaop2_+@#zu00+z0u3ax$42yedqja1d54h+sc-+osgvhq

las contrasenas se van actualizando y te la da django en la terminal donde pones este comando: 
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

tambien debes instalar el pip install -r requirements.txt 

y correr el servidor -->
