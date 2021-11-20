function mifuncion() { /* This part is linked with an exercise in the HTML file */
    document.getElementById("demostracion").innerHTML = "Párrafo cambiado";
}

class Add {
    constructor(...words) {
        this.words = words;
    }
    //your code goes here
    print() {
          var array = []
          for (let i = 0; i < this.words.length; i++) {
              array.push("$" + this.words[i]);
          }
          console.log(array.join("") + "$" );
      }
  }
  
  var x = new Add("hehe", "hoho", "haha", "hihi", "huhu");
  var y = new Add("this", "is", "awesome");
  var z = new Add("lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit");
  x.print();
  y.print();
  z.print();

  //---------------------------------------------------------------------------------------------------------------------------------------------
/*
SoyHenry
Estructuras de datos II
Listas enlazadas
se tiene un nodo inicial y es la cabeza de la lista a partir de ella se conectan con otros nodos
*/
// un nodo es una clase que tiene informacion o datos y va a tener un this.next apunta al siguiente nodo
// luego tiene una lista que es un conjunto de nodos
// this.head es el primer elemento de la lista
// this.length indica la cantidad
 
// class Nodo {
//     constructor(info) {
//         this.data = info;
//         this.siguiente = null;
//     }
// }
 
// class Lista {
//     constructor() {
//         this.head = null;   
//     }
// }
 
// antes de crear los nodos yo debo crear una lista
//var lista1 = new Lista();
 
//creando un nodo
//var nodo1 = new Nodo("Angel");
//creando nodo dos
//var nodo2 = new Nodo("Camilo");
//creando nodo tres
//var nodo3 = new Nodo("Pedro");
//clase agregar metodos adentro
//funciones no tienen constructor
//funciones agregar funciones atraves de prototipos
 
//diciendole a un nodo cual es su siguiente nodo
//nodo1.siguiente = nodo2
//nodo2.siguiente = nodo3
// aca la cabeza de la lista apunta al primer nodo creado
//lista1.head = nodo1
 
class Nodo {
    constructor(info) {
        this.data = info;
        this.siguiente = null;
    }
 }
  
 class Lista {
    constructor() {
        this.inicio = null;
        this.length = 0;
    }
  
    agregar(valor) {
        // el metodo recibe un valor y con ese valor creo un nuevo nodo para agregar a la lista
        let nodo = new Nodo(valor);
  
        // aca preguntamos si el inicio es null eso significa que el nodo que acabamos de ccrear lo agrega al inicio
        // esta validacion solo la puedo hacer una vez cuando el inicio de la lista es null
        if (this.inicio === null) {
            this.inicio = nodo;
            // para ir contando los nodos agregamos el length en el constructor y aca le sumamos uno
            this.length++;
        } else {
            // actual es una variable auxiliar que va a recorrer
            var actual = this.inicio
            // recorrer la lista hasta que el siguiente no sea null
            // mientras que actual sea diferente de null le va a asignar a actual el actual.siguiente
            while (actual.siguiente != null) {
                // si aun no ha llegado al ultimo nodo
                actual = actual.siguiente;
            }
            // cuando encuentre null al final agrega el nodo al final
            actual.siguiente = nodo;
            this.length++;
        }
        // aca puede ir un return
    }
  
    add(value) {
        var node = new Nodo(value);
        if (!this.inicio) {
            this.inicio = node;
        } else {
            var current = this.inicio;
            while (current.siguiente) {
                current = current.siguiente;
            }
            current.siguiente = node;
        }
        this.length++;
    }
  
    tamaño() {
        // para calcular el tamaño
        return this.length;
    }
 }
  
 // var milista = new Lista();
 // agrego un nuevo nodo con el metodo agregar la la clase lista
 // node.add("angel")
 // node.add("luis")
 // node.add("luis")
  
 var otralista = new Lista();
 otralista.add("nodo1")
 otralista.add("nodo2")
 otralista.add("nodo3")
  
 console.log(otralista)

 //---------------------------------------------------------------------------------------------------------------------------------------------
 /*
 estructura de datos III
 arboles binarios
 el arbol tiene un root o raiz
 inicia por un nodo raiz el nodo tiene es padre de nodo b y nodo c
 son sibligns cuando comparten el mismo padre
 el arbol crece hacia abajo y hacia los lados y ese crecimiento se le llama niveles
 el arbol puede tener un nivel de altura
 si no tiene hijos entonces vendría siendo las hojas del arbol no tiene hijos ni izquierdo o derecho
 un arbol principal esta conformado por sub arboles
 los arboles se deben recorrer de forma recursiva porque no conozco cuantos hijos tiene ese arbol
 data left and right
 los arboles no pueden volver a su padre
 un nodo solo conoce a los hijos
 un nodo solo puede tener un padre
 --------------------------------------------------------------------------------------------------
 arbol binario de busqueda
 tiene la condicion de que el dato que ingresa al arbol se compara con el nodo actual y si el dato es menor que el dato actual va por el lado izquierdo
 sino va por el lado derecho
 el arbol binario de busqueda corta a la mitad la cantidad de pasos, entonces es mucho mas rapido que otra estructura de datos
 ------------------------------------------------------------------------------------------
 arbol balanceado
 los niveles de la rama izquierda y los de la rama derecha no superan en uno la diferencia
 no es necesario que siempre esten balanceados
 */
  
 function Arbol(data) {
    this.value = data
    this.left = null
    this.right = null
 }
  
 Arbol.prototype.insert = function (data) {
    var nuevoarbol = new Arbol(data);
    if (data < this.value) {
        if (this.left === null) {
            this.left = nuevoarbol
        } else {
            this.left.insert(data)
        }
    } else if (data >= this.value) {
        if (this.right === null) {
            this.right = nuevoarbol
        } else {
            this.right.insert(data)
        }
    }
    return "Valor agregado"
 }
  
 var miarbol = new Arbol(10);
  
 /*
 recorrer arboles en general
 dfs postorder
 deep first search
 primero pregunta si tiene un hijo izquierdo
 segundo pregunta si tienes un hijo derecho
 tercero retorna el valor
 inicia en el root y avanza por izquierda
  
 dfs preorder
 primero retorna el valor(llamar a callback enviandole el valor)
 segundo pregunta hijo izquierdo
 tercero pregunta hijo derecho
  
 dfs inorder
 primero pregunta si tiene hijo izquierdo
 segunfo retornar
 tercero preguntar si tien hijo derecho
  
 bfs
 breadth first search
 se apoya en una arreglo o una lista o lo que sea
 primero muestra el valor
 segundo le hace push a los hijos
 tercero saca con shift el siguiente arreglo y se repite el proceso
 la condicion de parada es cuando el arreglo auxiliar quede vacio
  
 la tarea es un binary search tree
 cuando hagan el return llamen la funcion de callback enviandole ese valor
 */
 //---------------------------------------------------------------------------------------------------------------------------------------------
 /*
  
 */
 //---------------------------------------------------------------------------------------------------------------------------------------------
 /*
  
 */
 //---------------------------------------------------------------------------------------------------------------------------------------------
 /*
  
 */
 //---------------------------------------------------------------------------------------------------------------------------------------------
 /*
  
 */
  
  
 
 