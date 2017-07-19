function dirReduc(plan) {
  var opposites = {
    'NORTH': 'SOUTH',
    'SOUTH': 'NORTH',
    'EAST': 'WEST',
    'WEST': 'EAST',
  }

  return plan.reduce((dirs, dir) => {
    if (dirs[dirs.length - 1] === opposites[dir]) {
      dirs.pop()
    } else {
      dirs.push(dir)
    }
    return dirs
  }, [])
}

const test1 = dirReduc(['NORTH', 'NORTH', 'SOUTH', 'SOUTH', 'EAST'])
console.log("test1", test1)

function dirReducRegex(arr) {
  var str = arr.join('') 
  var pattern = /NORTHSOUTH|EASTWEST|SOUTHNORTH|WESTEAST/

  while (pattern.test(str)) {
    console.log("str", str)
    str = str.replace(pattern, '')
  }

  return str.match(/(NORTH|SOUTH|EAST|WEST)/g) || []
}

const test2 = dirReducRegex(['NORTH', 'NORTH', 'NORTH', 'SOUTH', 'SOUTH', 'EAST'])
console.log("what is test2", test2)
