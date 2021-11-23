# JavaScript Notes

---

## Javascript I

---

## Declarar variables

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

## Node

Para ejecutar en consola el archivo javascript

node demo.js

> para mostrar en consola es con console.log
> console.log(nombre, apellido);
> console.log(nombre + apellido);

## Cosas extrañas

```js
[] array vacío
{} objeto vacío
0 == "0" true
0 == [] true
"0" == [] false
2 + 2 4
2 + "2" 22
2 + "a" 2a
```

## Tipos de datos

```js
string;
numeros;
booleanos;
null; // no tiene un valor
undefined;
```

## Operaciones

suma
resta
multiplicacion
division
modulo

## Funciones

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

## Funcion Flecha

```js
const arrowFunction = () => {
  //content
};
```

## Argumentos en las funciones

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

## Funciones return

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

```js

```

```diff
function saludar(){
+    //content
-    //content2
}
```
