// Generators allow you to define an iterative algorithm by 
// writing a single function which can maintain its own state

function* gen() {
  yield* ['a', 'b', 'c']
}

const gendog = gen()

console.log(gendog.next().value)
console.log(gendog.next().value)
console.log(gendog.next().value)

// Generators compute their yielded values on demand
// Can efficiently represent sequences that are expensive to compute
// Or even infinite sequences

// The next() method also accepts a value which can be used to
// modify the internal state
// A value passed to next() will be treated as the result of the
// last yield expression that paused the generator
