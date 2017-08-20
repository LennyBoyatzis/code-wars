function pad(num) {
  return num < 10 ? '0' + num : num
}

function humanReadable(seconds) {
  var hours = parseInt( seconds / 3600 ) ;
  var minutes = parseInt( seconds / 60 ) % 60;
  var seconds = seconds % 60;

  return pad(hours) + ":" +pad(minutes) + ":" + pad(seconds); 
}

console.log(humanReadable(60))
