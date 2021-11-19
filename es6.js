/*
------------------------------------------------------------
ES6 - ECMAScript 6
Solo learn
------------------------------------------------------------
Variables and Strings
    there are three ways to declare a variable in es6

    var - globally or locally
    let - it depends in the scope to the block. one of the best uses for let is in loops
    for example:
    function varTest(){
    var x = 1;
    if(true){
        var x = 2; // same variable
        console.log(x); // 2
    }
    console.log(x); // 2
    }
    function letTest(){
    let x = 1;
    if(true){
        let x = 2; // different variable
        console.log(x); // 2
    }
    console.log(x); // 1
    }

    const - they have the same scope as let but they are not allowed to be reassigned
    for example:
    const a = "Hello";
    a = "Bye";

Template literals
    they are a way to output variables in the string
    for example:

    let name = "Angel";
    let msg = "Welcome" + name + "!";
    console.log(msg);

    let name = "Didier";
    let msg = "Welcome ${name}!";
    console.log(msg);

    let a = 8;
    let b = 2;
    let sum = "The sum is ${a+b}":
    console.log(msg);

Loops and functions
    simple function
*/

function test(a, b = 3, c = 42){
    return a + b + c;
}
//console.log(test(5)); //50

/* Arrow function */
var test = (a, b = 3, c = 42) => {
    return a + b + c;
}
//console.log(test(5)); //50

var scores = [68,95,54,84,77,75,63,74,69,80,71,63] // 7
var contador = 0;
var contador2 = 0;
for (let i = 0; i < scores.length; i++) {
    if (scores[i] > 70){
        contador = contador + 1;
    }
}
// console.log(contador);

var count = 0;
for (const iterator of scores) {
    if(iterator>=70){
        count++;
    }
}
// console.log(count);

// for in => sirve para recorrer un objeto
// for of => sirve para recorrer un array
// for of => sirve para recorrer un string

/* 
ES6 Objects
javascript variables can be object data types that contain many values called properties
*/
let tree = {
    height: 10,
    color: "green",
    // this is a method
    grow() {
        this.height += 2;
    }
};
tree.grow();
// console.log(tree.height);

let height = 5;
let health = 100;
let athlete = {
    height,
    health
};
/*
Computed property names
it is so useful when you need to create custom objects based on a some variables
let prop = "name";
let id = "1234";
let mobile = "8998";

let user = {
    [prop]: "Angel"
    ["user_${id}"]: "${mobile}"
};

Object.assign in ES6
*/
let person = {
    name: "Jack",
    age: 18,
    sex: "male"
};
let student = {
    name: "Bob",
    age: 20,
    xp: "2"
};
// enviamos un {} objeto al cual le queremos aplicar las nuevas propiedades
// let newStudent = Object.assign({}, person, student);
// console.log(newStudent);

let persona = {
    nombre: "angel",
    edad: 34
};
let nuevapersona = Object.assign({}, persona, {nombre:"Carlos"});
// console.log(nuevapersona);

const obj1 = {
    // la variable const no puede ser sobreescrita
    a: 0,
    b: 2,
    c: 4
  };
const obj2 = Object.assign({c: 5, d: 6}, obj1);
// console.log(obj2.c, obj2.d);
/*
Array Destructuring in ES6
you can unpack values from arrays or properties from objects
*/
let arra = ["1","2","3"];
let [one, two, three] = arra;

// console.log(one);
// console.log(two);
// console.log(three);

/*
Object Destructuring in ES6
you can unpack values from arrays or properties from objects
*/
let obj = {h:100, s:true};
let {h, s} = obj;

// console.log(h);
// console.log(s);

/*
The Spread Operator
pass the elements of an array as arguments to a function
*/

const myFunction = (w, x, y, z) => {
    console.log(w, x, y, z);
};
let args = [1, 2, 3];
myFunction(...args, 4);

/*
Spread in array literals
*/
var arr = ["one", "two", "five"];

arr.splice(2, 0 ,"three");
arr.splice(3, 0 ,"four");
console.log(arr);

let newarr = ["three", "four"];
let arr = ["one", "two", ...newarr, "five"];
console.log(arr);
/*
Classes
a class contains a constructor method for initializing
the constructor is a especial method which is used for creating and initializing an object created with a class
*/
class rectangle {
    constructor(height, width){
        this.height = height;
        this.width = width;
    }
}

const square = new rectangle(5, 5);
const poster = new rectangle(2, 3);

//se puede definir una clase con una expresion de clase
var Square = class rectangle {
    constructor(height, width){
        this.height = height;
        this.width = width;
    }
}

//una variable asignada a la definicion de una clase
var Square = class {
    constructor(height, width){
        this.height = height;
        this.width = width;
    }
}
/*
Inheritance
the extends keyword is used in class declarations or class expressions to create a child of a class
the child inherits the properties and methods of the parent
*/
class animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        console.log(this.name + " makes a noise.");
    }
}
class dog extends animal {
    speak() {
        //the parent's speak method is called using the super keyword
        super.speak();
        console.log(this.name + " barks.");
    }
}
let perro = new dog("rex");
console.log(dog.speak());
/*
Map object/Map methods
puede ser usada para guardar pares key/value

methods
set(key, value) Adds a specified key/value pair to the map. If the specified key already exists, value corresponding to it is replaced with the specified value.
get(key) Gets the value corresponding to a specified key in the map. If the specified key doesn't exist, undefined is returned.
has(key) Returns true if a specified key exists in the map and false otherwise.
delete(key) Deletes the key/value pair with a specified key from the map and returns true. Returns false if the element does not exist.
clear() Removes all key/value pairs from map.
keys() Returns an Iterator of keys in the map for each element.
values() Returns an Iterator of values in the map for each element.
entries() Returns an Iterator of array[key, value] in the map for each element.
*/

/*
Set
size property returns the number of distinct values in a set
methods
add(value) Adds a new element with the given value to the Set.
delete(value) Deletes a specified value from the set.
has(value) Returns true if a specified value exists in the set and false otherwise.
clear() Clears the set.
values() Returns an Iterator of values in the set.
*/
/* 
Promises 
*/
new Promise(function(resolve, reject)){
    if (success){
        resolve(result;
    } else {
        reject(Error("failure"));
    }
}

/*
Iterators & Generators
*/
let myIterableObj = {
    [Symbol.iterator] : function* () {
        yield 1;yield 2; yield 3;
    }
}
console.log([...myIterableObj]);

/*
Modules
*/

// lib/math.js
export ​let sum = (x, y) => { return x + y; }
export ​let pi = 3.14

// app.js
import * ​as math from "lib/mat"
console.log(`2p = + ${math.sum(math.pi, math.pi)}`)

/*
Methods
filter
find
findIndex
join
repeat
indexOf
includes
endsWith
startsWith
*/