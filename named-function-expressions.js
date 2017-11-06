//Anonymous function expressions
var clickHandler = function() {
  console.log("Hello world")
}

//Named function expression
//Benefits of a named function expression
//1. Handy self reference to the function
//2. Helpful for debugging a stack trace
//3. More self documenting code

var keyHandler = function keyHandler() {
  console.log("Hello world")
}

// Prefers function declarations as opposed to function expression
function helloWorld() {
  console.log("hello world", helloWorld)
}

helloWorld()
