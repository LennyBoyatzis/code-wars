// 1. Compilation step
// 2. Execution step
// Difference between LHS and 

var foo = "bar";

function bar() {
  var foo = "baz";

  function baz(foo) {
    foo = "bam";
    bam = "yay"; // Unfulfilled LHS References will create an implicit global
  }
  baz();
}

bar();
console.log("foo ", foo); // Global scope
console.log("bam ", bam); // Implicit global set inside baz
// console.log("baz() ", baz()); // Unfulfilled RHS References always create a reference error
