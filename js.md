# JavaScript Notes

---

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
> console.log(nombre, apellido);
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

## Control de flujo

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

## Javascript II

---

## Veracidad

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

Operadores logicos && || NOT

|COSO|COSO2| ACA DEBE IR LA TABLA

## For

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

## While

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

## Switch case

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

## Do while

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

<<<<<<< HEAD
# Intro to CS

## December 6 2021 Intro to CS

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

## December 7 2021 Lecture Intro to CS

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

```js

```

```diff
+    //content
-    //content2
```
