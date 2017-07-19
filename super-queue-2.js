function queueTime(customers, tellers) {
  var tellerTimes = new Array(tellers).fill(0)  

  for (let customer of customers) {
    var nextTellersTime = Math.min(...tellerTimes)
    var nextTellerIndex = tellerTimes.indexOf(nextTellersTime)
    tellerTimes[nextTellerIndex] += customer
  }
  return Math.max(...tellerTimes)
}

console.log(queueTime([10,2,3,3], 1)) // 18
console.log(queueTime([10,2,3,3], 2)) // 10
console.log(queueTime([2,3,10], 2)) // 12
