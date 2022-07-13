"""
Apuntes python, LinkedIn Course Julio 12 2022

Comentarios
Se pueden agregar comentarios de dos formas diferentes:
1 - Con la almohadilla # al principio o después de una línea de código
2 - Con triple comillas, como está escrito este párrafo
"""

# print("Hola angel") # para imprimir en consola

"""
Variables
No es necesario declarar el tipo de valor que tendrá la variable
"""

# from cuadrado import area_cuadrado, perimetro_cuadradp
nombre = "Angel"  # string
edad = 20  # integer
flotante = 1.72  # float, usar el punto como separador
booleano = True  # bool, primera letra en mayúscula

# print(type(nombre)) # imprime el tipo de dato de la variable

"""
Operaciones básicas en python

Suma +
resta - 
multiplicacion + 
division /, el resultado de la division siempre será un número flotante
modulo %
potencia 3**2 = 9
concatenar textos "texto1" + "texto2" = texto1texto2
multiplicar textos "ola"*3 = olaolaola
mayor que >
menor que <
igualdad ==
diferencia !=
"""

"""
Las built-in functions

No es necesario llamar a una librería
print
int() retorna un entero
float() retorna un decimal
string() retorna un texto
type() retorna tipo
help() ayuda
"""

"""
PEP 8

Es la guía de estilos de python
la identación debe ser de cuatro espacios y es muy importante
una línea de código debe tener como máximo 79 caracteres

se debe usar dos líneas en blanco para separar funciones de clases
una linea en blanco para separar métodos
una linea en blanco al final de cada archivo
"""

"""
Estructuras de datos

listas = se definen en { } con duplicados, mantienen el orden que fueron declarados
tuplas = se definen en ( ) con duplicados
diccionarios = se definen en { } cada elemento tiene llave: valor
sets = se definen entre { } sus elementos son únicos
"""

# Listas
"""
lenguajes = {"Python", "Java", "Ruby", "C++"}
cosas = {1, 2.8, True, "Python", 1}
lenguajes[0]
len(lenguajes)
lenguajes.append("Agregar") # agrega eso al último elemento de la lista
lenguajes.extend(otros_lenguajes)
"""

# Tuplas
"""
son inmutables no es posible modificar los elementos 
se usan cuando se requiere mejor tiempo de procesamiento
idiomas = ("Python", "C", "C++")
idiomas = "Python", "C", "C++"
idiomas[0]
idiomas[-1] # último elemento de la lista
"""

# Diccionarios
"""
Permite almacenar información en pares de datos llave y valor
son conocidos como los json
las llaves son únicas y no se pueden repetir
language = {
    "nombre": "Python",
    "creador": "Angel"
}
language["nombre"]
"""

# Sets
"""
No son estructuras ordenadas y no se puede acceder a ellos a traves de índices
pueden tener elementos de diferentes tipos como numeros y textos
no soporta elementos repetidos
set1 = {1,2,3}
len(set1) # nos da el tamaño del set
set1.discard(2) # para eliminar un elemento
set1.remove(3) # si se trata de eliminar un elemento que no existe arroja un error
set1.clear() # borra todos los elementos del set
"""

"""
Condiciones lógicas

==
!=
<
>
>=
<=

expresiones condicionales
is 
and une dos o mas condiciones
or une condiciones y si uno es true la sentencia es true
not 
if 2 == 2:
    print("Son iguales")
else:
    print("No son iguales")

Es importante colocar los dos puntos al final de la comparación

Ciclos for 
ciclos while
"""

"""
a = 1
b = 2

if a > b:
    print("A es mayor que B")
elif a < b:
    print("B es mayor que A")
else:
    print("lo que sea")

if type(a) is bool:
    print("A es booleano")
else:
    print("A es otro tipo de dato")


c = 5
d = 6
e = 10

if c > d and d < e:
    print("Las dos condiciones son verdaderas")
"""

"""
Ciclo for

for letra in "Texto": # in sirve para identificar el elemento en el cual vamos a iterar
    print(letra)


cosas = ["uno", "dos", "tres"]
for elemento in cosas:
    print(elemento) # break rompe el ciclo 
    # continue salta el elemento y continua la ejecucion del codigo

for element in range(8):
    print(element)
"""

"""
Ciclo while

tambien se puede usar el break y se utiliza con una conicion
i = 1
while i <= 5:
    print(i)
    i += 1
    if i == 3:
        break
"""


"""
Iterar sobre una lista

cuentos = ["alo","flor","angel"]
for index in range(len(cuentos)):
    print("indice", index)

Muestra la cantidad de letras que contiene el nombre de cada fruta

frutas = ["manzana", "naranja", "piña"]

for fruta in frutas:
    x = 0
    for letra in fruta:
        x += 1
    print("fruta: ", fruta)
    print("tiene: ", x, " letras")
"""

"""
Iterar sobre un diccionario

juegos = {
    "nombre": "Halo",
    "creador": "Angel"
}

for llave in juegos:
    print("llave:", llave)
    print("valor:", juegos[llave])

for elemento in juegos.keys():
    print(elemento) # imprime la llave del diccionario

for elemento in juegos.values():
    print(elemento) # imprime el valor del diccionario

for llave, valor in juegos.items():
    print(llave, valor)
"""

"""
Funciones

tiene instrucciones que se encargan de cumplir con una tarea
permite organizar el codigo en partes pequeñas
reusar el codigo
se define una funcion con def
los parametros van dentro de los parentesis
se debe terminar en dos puntos
APELLIDO = "Serrato" # se define en mayuscula porque es una variable global

def funcion():
    print("hola")
    nombre = "Angel"

funcion() # se debe invocar la funcion

def funcion(lado, unidades):
    perimetro = lado * 4
    print(f"El perimetro es {perimetro} {unidades}")

funcion(25, "metros") # hay dos formas de enviar, se envian los parametros en orden

funcion(lado = 25, unidades="metros") # la segunda forma es colocando el nombre del parametro
"""

"""
Retorno de valores en python

forma 1
def perimetro_cuadrado(lado):
    perimetro = lado * 4
    return perimetro


def area_cuadrado(lado):
    area = lado * lado
    return area


perimetro = perimetro_cuadrado(lado=5)
area = area_cuadrado(lado=5)

print(f"area: {area}, perimetro: {perimetro}")

forma 2
def calcular_cuadrado(lado):
    perimetro = lado * 4
    area = lado * lado
    return area, perimetro


area, perimetro = calcular_cuadrado(lado=2)

print(f"area: {area}, perimetro: {perimetro}")

forma 3
def calcular_cuadrado(lado):
    perimetro = lado * 4
    area = lado * lado
    return area, perimetro


resultado = calcular_cuadrado(lado=2)

print(resultado) # retorna una tupla 
"""


"""
Documentar la funcion

docstrings python
https://www.programiz.com/python-programming/docstrings
https://betterprogramming.pub/3-different-docstring-formats-for-python-d27be81e0d68


"""


def funcion():
    """ La funcion imprime hola.

    Esta funcion recibe el valor de un lado del cuadrado y a partir de este
    Arg:
        lado (int): medida del lado del cuadrado 

    Returns:
        perimetro (int): perimetro del cuadrado
    """
    print("hola")


funcion()  # al hacer hover sobre la funcion en el cuadro de texto explica


def mensaje(men):
    y = ""
    for x in men:
        y = y + x
        print(y)


mensaje("Hola")  # esto imprime hola de forma rara


"""
Modulos

son librerias con funciones o clases
los paquetes son carpetas que contienen funciones
ejemplo pandas para manipulacion de datos
importar una libreria
podemos crear nuestros propios modulos
import datetime
import datetime as dt # se le asigna un alias para que sea mas sencillo
from datetime import datetime

hora = datetime.datetime.now()

print(hora)
"""


"""
Creando un modulo en python

# creamos el archivo cuadrado.py

# cuadrado.py

def area_cuadrado(lado):
    return lado * lado

def perimetro_cuadrado(lado):
    return lado * 4

# fin cuadrado.py

# se puede hacer utilizando un diccionario
lado = 5
cuadrado = {
    "lado": lado,
    "area": area_cuadrado(lado),
    "perimetro": perimetro_cuadrado(lado)
}

print(cuadrado)

# se puede hacer de la siguiente manera tambien

perimetro = perimetro_cuadrado(lado)
print(perimetro)
"""

"""
Creando un paquete en python

un paquete es un conjunto de modulos
__init__.py
main.py es el archivo principal donde se importa lo demas
"""

"""
Programacion orientada a objetos

POO
es el paradigma mas usado en el desarrollo de software
objetos o instancias que se crean a partir de una clase
los atributos

abstraccion es como un plano que permite definir el objeto
encapsulamiento evita que se manipulen de manera incorrecta
polimorfismo
herencia
"""

"""
Objeto
class Persona: # cammelcase, primera en mayuscula
    def __init__(self): # init es el constructor de la clase self permite acceder a las funciones de la clase
        print("dentro del constructor")

pedro = Persona()
print(type(pedro))

paco = Persona()
print(type(paco))

print(pedro == paco) # falso, los objetos son diferentes y ocupan una posicion diferente
"""

"""
Atributos

cada objeto tiene atributos y son las caracteristicas del objeto
atributos de instancia
    se definen dentro de la funcion __init__
atributos de clase 

class Persona:
    atributo = 123

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


paco = Persona("Paco", 20)
print(paco.nombre)  # nombreObjeto.nombreAtributo
print(paco.edad)
print(paco.atributo)
"""

"""
metodos de una clase

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # metodo cumplir años
    def cumplir_anios(self):
        self.edad += 1
        # f es para darle formato al texto
        print(f"Feliz cumpleaños #{self.edad} {self.nombre}")


paco = Persona("paco", 20)
paco.cumplir_anios()
"""

"""
herencia de clases

clases padre y clases hijo
se crea la clase empleado que hereda los metodos de la clase padre en este caso Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # metodo cumplir años
    def cumplir_anios(self):
        self.edad += 1
        # f es para darle formato al texto
        print(f"Feliz cumpleaños #{self.edad} {self.nombre}")


class Empleado(Persona):
    def __init__(self, horas_totales):
        # permite heredar los atributos de la clase persona
        super(Empleado, self).__init__(nombre, edad)
        self.horas_totales = horas_totales

    def trabajar(self, horas):
        self.horas_totales += horas
        print(f"usted ha trabajado {horas} horas")
        print(f"Horas totales {self.horas_totales}")


pedro = Empleado("paco", 20, 30)
pedro.trabajar(8)
"""

"""
Paquetes de python

descarga paquetes de 
https://pypi.org/

numpy es un paquete muy conocido

se instala con pip
pip es el instalador y administrador de paquetes de python

pip --version
pip install flask = flask es una libreria para desarrollo web
pip freeze = sale una lista de todas las librerias instaladas 
pip unistall = desinstalar

Librerias para ambientes
- virtualenv
- venv
- anaconda

crear ambientes virtuales para manejar varios proyectos

archivo de requerimientos
crea una lista de las librerias que se estan usando en un proyecto
requirements.txt es el nombre estandar

env\Scripts\Activate
pip install requirements.txt
"""

"""
errores de sintaxis
variables no definidas
errores por tipo de dato

try y except se usan para capturar errores
try captura el tipo de error los exception errors
"""

def validar_x(x):
    if x > 1:
        raise Exception("La variable x debe ser mayor a 1")
    else:
        print("x es mayor a 1")

x = 2
validar_x(x)

def calcular_promedio(lista):
    assert len(lista) > 0, "La lista esta vacia"
    return sum(lista) / len(lista)

promedio = calcular_promedio(lista=[1,3,5])
print(promedio)