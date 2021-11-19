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