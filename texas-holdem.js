var Result = { "win": 1, "loss": 2, "tie": 3 }

function PokerHand(hand) {
  this.hand = hand;
}

// High card
// One Pair
// Two Pair
// Three of a kind
// Straight
// Flush
// Full House
// Four of a kind 
// Straight Flush
// Royal Flush

PokerHand.prototype.compareWith = function(opponentHand) {
  console.log("this.hand", this.hand)
  return Result.tie;
}

var player = new PokerHand("2H 3H 4H 5H 6H")
var opponent = new PokerHand("KS AS TS QS JS")

player.compareWith(opponent)
