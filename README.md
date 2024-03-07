# Challenge-EGO

Para poder entrar al endpoint hay que seguir esta serie de pasos 

1 - Crear el entorno virtual
    Poner esta linea de comando: py -m venv nombrequequierasdelentorno. /n
    Luego entrar al entorno con estos comandos: nombrequequierasdelentorno\Scripts\activate (en Windows)

2 - Instalar las dependencias, poner los siguientes comandos para instalarlos:
    pip install django
    pip install django-rest-framework
    pip install django-cors-headers
    pip install pillow

3 - Correr el proyecto con el siguiente comando: python manage.py runserver

4 - Ir a la siguiente url http://127.0.0.1:8000/, alli le saldra la listas de endpoints aunque por ahora solo hay una
