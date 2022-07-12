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

from time import process_time_ns


nombre = "Angel" # string
edad = 20 # integer
flotante = 1.72 # float, usar el punto como separador
booleano = True # bool, primera letra en mayúscula

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











