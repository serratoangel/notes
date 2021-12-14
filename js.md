# JavaScript Notes

## Javascript I / October 20 2021

---

### Declarar variables

Guardar informacion para luego acceder a ella

- var
  variable global
- let
  vive dentro del contexto de ejecucion de la funcion
- const
  variable constante para definir valores dentro de una constante, se usa para arreglos y objetos y no se puede modificar luego de haber sido declarada

### Nombres de variables

cammelcase nombreDeUnaVariable

nombre_de_una_variable

```js
var nombreAlumno = "angel";
let apellido_alumno = "serrato";
const edad = 34;
```

### Node

Para ejecutar en consola el archivo javascript

node demo.js

> para mostrar en consola es con console.log
>
> console.log(nombre, apellido);
>
> console.log(nombre + apellido);

### Cosas extrañas

```js
[] array vacío
{} objeto vacío
0 == "0" true
0 == [] true
"0" == [] false
2 + 2  ==> 4
2 + "2" ==> 22
2 + "a" ==> 2a
```

### Tipos de datos

```js
string;
numeros;
booleanos;
null; // no tiene un valor
undefined;
```

### Operaciones

suma
resta
multiplicacion
division
modulo

### Funciones

Bloque de codigo que realiza alguna funcion

las funciones deben ser invocadas o llamarlas para ejecutarlas

```js
function nombreDeLaFuncion() {
  var nombre = "angel";
  console.log("mi nombre es: ", nombre);
}

nombreDeLaFuncion(); // asi se llama la funcion o se ejecuta
nombreDeLaFuncion; // asi sale la definicion de la funcion
```

Otra forma de definir una funcion

De esta forma asignamos una funcion a una variable

```js
const otraFuncion = function () {
  var apellido = "didier";
  console.log("mi apellido es: ", apellido);
};

//Ejemplo
var funcionTres = "hola";

funcionTres = function () {
  var nombre = "didier";
  console.log("mi nombre es: ", nombre);
};

funcionTres(); // asi se llama la funcion o se ejecuta
```

### Funcion Flecha

```js
const arrowFunction = () => {
  //content
};
```

### Argumentos en las funciones

Los argumentos deben ser enviados en el mismo orden que los recibe la funcion

```js
function argumentosTest(argumentoNombre, apellido) {
  //se puede concatenar con + o con ,
  //console.log es una funcion
  console.log("el nombre es :" + argumentoNombre);
  console.log("el apellido es :", apellido);
}

argumentosTest("Angel", "Serrato");
```

### Funciones return

console.log muestra en consola
return retorna algo y eso significa que debe estar al final porque corta la ejecucion del codigo

```js
function suma(a, b) {
  //este return es el que devuelve el valor para ser guardado en elvalordesumaes
  return a + b;
}
suma(1, 2);

var elvalordesumaes = suma(1, 2);

console.log("la variable suma es :", elvalordesumaes);
```

### Control de flujo

Dentro del parentesis debe retornar un valor booleano

```js
function edad(age) {
  if (edad >= 18) {
    return "es mayor de edad";
  } else {
    return "es menor de edad";
  }
}
var persona = edad(34);
console.log(persona);
```

---

## Javascript II / October 21 2021

---

### Veracidad

Dentro de node

```js
!true //esto es para negar

!!true //entrega el valor real en booleano

!!0 false

!!"asdfasf" true

!!1221 true

1 > 2 false

2 > 1 true

!1 > 2 false

false > 2 false

1 == "1" true

1 === "1" false //no son iguales los enteros a strings

2 === 2 true
```

### Operadores logicos && || NOT

|COSO|COSO2| ACA DEBE IR LA TABLA

### For

DRY Don't Repeat Yourself

```js
//muestra los numeros del 1 al 10
function num() {
  for (let i = 1; i < 11; i = i + 1) {
    console.log(i);
  }
}
```

Para simular matrices

```js
function num() {
  for (let i = 1; i < 11; i = i + 1) {
    for (let j = 1; j < 11; j = j + 1) {
      for (let k = 1; k < 11; k = k + 1) {
        //content
      }
    }
  }
}
```

### While

Mientras se cumpla x condicion haga tal cosa

```js
function funcion() {
  var i = 0;
  var j = 0;
  while (i < 100) {
    while (j < 100) {
      console.log(i, j);
      j++;
    }
    j = 0;
    i++;
  }
}
funcion();
```

### Switch case

Son if else encadenados, se usa para palabras

```js
function caso(saludo) {
  switch (saludo) {
    case "en":
      console.log("hey there");
    case "es":
      console.log("hola");
    default:
      console.log("no es conocido el idioma");
  }
}
caso("en");
```

### Do while

Loops are used to repeat a block of code until a specified condition is met.

The **do...while** loop is similar to the **while** loop with one important difference. The body of **do...while** loop is executed at least once. Only then, the test expression is evaluated.

```js
function otra() {
  var i = 0;
  do {
    console.log(i);
    i++;
  } while (i <= 100);
}
```

---

## Javascript III / October 25 2021

---

los arreglos ayudan a listar ciertos elementos como se haria con un archivador, en cada cajon se puede guardar cualquier tipo de dato o se puede guardar otro archivador dentro del mismo

asi se puede organizar informacion

```js
var arreglo = []; // asi se declara un arreglo
var objeto = {}; // asi se declara un objeto
var arregloDos = [1,2,"3",5,"maria",8,9,11,true,null,[a,b,c]]
console.log(arregloDos[0]); // los arreglos comienzan desde la posicion cero

arregloDos[0] = "aca puedo cambiar el valor en esa posicion del arreglo"

console.log(arregloDos.length); // el .length va a comenzar desde uno y no desde cero

arregloDos.length - 1; // accede a la ultima posicion del arreglo
```

### Math en los arreglos

#### array.length

se sabe el tamaño del arreglo y comienza contando desde uno

#### push

push sirve para agregar al final del arreglo

```js
var array = [1,2,3,4,5];
array.push(6);
array.push(7,8,9,10);
console.log(array);
console.log(array[4][1]); // para acceder a dos posiciones del arreglo
console.log(array[5][4][1]) // acceder al arreglo que tiene un arreglo dentro de un arreglo
```

#### pop

extrae el ultimo dato del arreglo y lo elimina

para poder guardar este dato se puede asignar a una variable

```js
var array = [1,2,3,4,5]
array.pop();

var item = array.pop(); // para guardar el dato en una variable
```

#### unshift

agrega un valor al inicio del arreglo

```js
array.unshift("dato");
```

#### shift

saca el primer dato del arreglo

```js
array.shift();
var itemDos = array.shift();
```

### recorrer un arreglo

para recorrer un arreglo se puede utilizar un ciclo for

```js
var arreglo = [1,2,3];
for(let i = 0; i < arreglo.length; i++){
  array[i] = "palabra" + i;
  console.log(array[i]);
}
```

#### typeof

sirve para conocer que tipo de dato es

```js
function mostrar(algo){
  if(typeof algo === boolean{ // puede ser boolean number string symbol undefined object
    console.log("es booleano");
  };
}
```
---
## JavaScript IV / October 26 2021
---

### Objetos

en js todo son objetos, es una coleccion de propiedades asociadas a un valor

```js
var objeto = {};
var persona = {
  nombre: "angel", // nombre propiedad: valor propiedad
  apellido: "serrato",
  edad: 34,
  saludar: function(){
    console.log("hola angel");
  }
  hobbies: [caminar, correr],
}
var array = [1,2,3]
array[0]; // acceder al valor del array en la posicion cero
```

#### bracket notation

```js
// aca se utiliza la bracket notation cuando yo no conozco el nombre de la propiedad
persona["nombre"]; // acceder al valor del propiedad nombre dentro del objeto persona, se debe colocar entre comillas el nombre de la propiedad
// si la propiedad no existe el resultado sera undefined
// con string
```

#### dot notation

```js
// aca se utiliza dot notation cuando conozco el nombre de la propiedad
persona.nombre; // para acceder al valor de la propiedad nombre
// con la palabra de la propiedad que estoy buscando
```

#### Object.keys

asi obtengo las propiedades del objeto por ejemplo persona

```js
console.log(Object.keys(persona));
```

si la propiedad no existe dentro del objeto js la crea y la agrega al final

```js
persona.pasaporte = "col12345";
```

#### buscando propiedades cuando no sabemos el nombre de las mismas

buscar la propiedad del valor con el cual esta la palabra

```js
persona.nombre // cuando conozco el nombre de la propiedad
persona["propiedad"] // cuando no conozco el nombre de la propiedad
```

#### for in 

es un for para recorrer objetos

```js
for(let propiedad in persona){
  // me muestra el nombre de la propiedad y el valor de la propiedad
  console.log(propiedad);
  console.log(persona[propiedad]);
}
```

#### invocar una funcion que esta dentro de un objeto

se le llama metodo a la funcion que esta dentro del objeto y se debe colocar saludar() sino se colocan los corchetes js devuelve la definicion del metodo

```js
console.log( persona.saludar() ); // con dot notation
console.log( persona[saludar]() ); // con bracket notation
```

#### keyword this

cuando yo quiero acceder desde un metodo del propio objeto a alguna de las propiedades que contiene el objeto puedo utilizar la palabra this para hacer referencia al propio objeto(asi mismo)

```js
var persona1 = {
  nombre: "angel",
  saludo: function (){
    console.log("hola angel");
  }
}
var persona2 = {
  nombre: "luis",
  saludo: function (){
    console.log("hola " + this.nombre);
  }
}
```

puedo definir una funcion por aparte y los objetos la usan por dentro, para reutilizar esa funcion

```js
function saludarPersona(){
  console.log(this.nombre);
}
var persona1 = {
  nombre: "angel",
  saludar: saludarPersona
}
var persona2 = {
  nombre: "luis",
  saludar: saludarPersona
}
```

#### acceder a los valores de las propiedades

```js
var alumnos = {
  {
    nombre: "angel",
    edad: 34,
    hobbies: [correr, caminar, nadar],
    amigos: [
      {
        nombre: "brian",
        familia: [{ nombre: "vargas"}]
      }
      {
        nombre: "carlos",
        familia: [{ nombre: "cardenas"}]

      }
    ]
  }
  {
    nombre: "david",
    edad: 30,
    hobbies: [correr, caminar, nadar],
    amigos: [
      {
        nombre: "miguel",
        familia: [{ nombre: "vargas"}]
      }
      {
        nombre: "antonio",
        familia: [{ nombre: "cardenas"}]

      }
    ]
  }
}
// para acceder al dato familia
console.log(alumnos[1].amigos[0].familia[0].nombre) // vargas
console.log(alumnos[1]["amigos"][0].familia[0].nombre) // vargas
```


























# Intro to CS

---

### December 6 2021 Intro to CS

---

Tabla de la verdad

true = 1
false = 0

A   B   And   Or
0   0   0     0   
0   1   0     1
1   0   0     1
1   1   1     1

sistema decimal en base 10 porque tiene 10 simbolos
sistema binario en base 2
sistema hexadecimal en base 16 porque tiene 16 simbolos
0 1 2 3 4 5 6 7 8 9 a b c d e f

8 bits es un bite

### December 7 2021 Lecture Intro to CS

```js
function BinarioADecimal(num){
  // digito por la base elevada a la posicion(esta va de atras para adelante)
  // digito * base ^ posicion
  // recorrer de atras hacia adelante
  // se recorre con un for con string.length - 1
  // 0 * 2**0 + 1 * 2**1 + 1 * 2**2 
  // i = 2
  // "1 1 0"
  // posicion = 0
  var resultado = 0;
  var posicion = 0;
  for(let i = num.length-1; i >= 0; i--){
    resultado = resultado + num[i] * 2 ** posicion;
    posicion++;
  }
  return resultado;
}

function decimalAbinario(num){
  // se debe usar modulo para sacar el resto
  // 11 % 2 
  // se toman los restos y se leen de abajo hacia arriba
  var resultado = "";
  // mientras que numero sea diferente de cero
  while(num !== 0){
    // con este lo pega al principio del string
    resultado = num % 2 + resultado;
    num = Math.floor(num/2);
  }
  return resultado;
}
```

# JavaScript I

## December 7 2021

javascript se ejecuta en un solo proceso en un solo hilo y ademas es sincronico esto quiere decir que va leyendo linea por linea

### syntax parser

detecta si hay o no errores 

### lexical environment

### execution context

contexto de ejecucion global contiene informacion sobre que codigo se esta ejecutando

contexto de ejecucion puede accer al outer environment pero no al inner environment

el contexto de ejecucion se crea cuando la funcion se ejecuta, cuando se termina de ejecutar su contexto se destruye

scope es el alcance que tiene la variable dentro del contexto de ejecucion

hoisting significa levantar o alzar, sube la declaracion de las variables y sube la definicion de la funcion

### execution stack

la pila de ejecucion que se crea cuando se ejecuta un archivo javascript

### operadores

infix expression es la forma mas facil de escribir
prefix expression
postfix expression

### precedencia de operadores

suma resta multiplicacion division
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence

## pasar por referencia o por valor / reference or value

objeto o arreglo se pasa por referencia porque son direcciones en memoria

pasar por valor pasa una copia 

## This

this en el browser trae el objeto global window










=======
## Javascript III

## Array

Listan elementos para crear un conjunto de varias cosas o diferentes cajones

Por ejemplo un archivador. Los arreglos son una lista de elementos que pueden ser string num o incluso otros arreglos

Se debe separar por comas y se utiliza []

```js
var arreglo = [1, 2, 3, 4, 5];
let array = []; /* arreglo vacio */
const arr = [otro[],"Angel", true, null, 123, , "el anterior es un espacio vacio, cosa que nunca se hace"];
```

Acceder a la informacion del arreglo.

Del arreglo devuelvame el valor en la posicion[i]

```js
var arreglo = [1, 2, 3, 4, 5];
console.log(array[0]);
```

### Asignando valores al array

Cambiarle valores al array

```js
var arreglo = [1, 2, 3, 4, 5];
array[0] = "otro numero"
console.log(array[0]); //otro numero
```

### Propiedades del array

length es una propiedad, funcionalidades como push, shift, unshift

push agrega informacion al final del arreglo

```js
var arreglo = [1, 2, 3, 4, 5];
var lista = ["Angel","Didier","Serrato","Arias"];
console.log(array.length);
console.log(array[array.length - 1]); //acceder al ultimo elemento del array
arreglo.push(6);
arreglo.push(lista);
arreglo.push(["Angel","Didier","Serrato","Arias"]); //se le puede hacer push de otro arreglo tambien
console.log(arreglo[6][0]); //se puede acceder al arreglo que esta dentro ddel arreglo y mostrar la posicion cero en este caso
```

pop extrae el ultimo dato del arreglo y lo elimina

se puede guardar ese dato extraido en una variable si se quiere

```js
var arreglo = [1, 2, 3, 4, 5];
arreglo.pop;
var item = arreglo.pop;
console.log(arreglo); 
```

unshift agrega al inicio del arreglo

```js
var arreglo = [1, 2, 3, 4, 5];
arreglo.unshift(6);
console.log(arreglo); 
```

shift saca el primer dato de un arreglo

```js
var arreglo = [1, 2, 3, 4, 5];
arreglo.shift();
console.log(arreglo); 
```

### Recorrer el arreglo

el tamaño del arreglo va hasta **array.lenght - 1**

```js
var arreglo = [1, 2, 3, 4, 5];
for (let i = 0; i < arreglo.lenght; i++) {
  console.log(i);
}

```


===
>>>>>>> c4d524c6eb73f79cb80d879aa41a13a22d5212db

---
# Javascript
---

### December 13 2021

```js
function nFactorial(n) {
  if(n===0 || n===1) return 1
  if(n % 1 != 0) return "el numero debe ser entero"
  if(n < 0) return "no existen factoriales de numero negativos"
  return n * nFactorial(n-1)
}
```

```js
function Queue(){
  this.arr = [];
}
var miLista = new Queue()
```


```diff
+    //content
-    //content2
```
