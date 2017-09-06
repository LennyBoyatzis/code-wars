const count = (arr, item) => (arr.filter(el => el === item)).length
const scoreBoard = {
  '111': 1000,
  '666': 600,
  '555': 500,
  '444': 400,
  '333': 300,
  '222': 200,
  '1': 100,
  '5': 50,
}

function score(dice) {
  const arrAsStr = dice.sort().reduce((curr, acc) => {
    acc = curr + acc
    return acc
  }, '')

  var score = 0
  for (var key in scoreBoard) {
    if (arrAsStr.indexOf(key) >= 0) {
      score += scoreBoard[key]
    }
  }

  return score
}

console.log("what is the score", score([5,1,3,4,1]))
console.log("what is the score", score([1,1,1,3,1]))
console.log("what is the score", score([2,4,4,5,4]))
