from replit import clear
from art import logo
print(logo)

bids = {}
bidding = False

def find_highest_bidder(maximum):
  highest_bid = 0
  winner = ""
  
  for price in maximum:
    bid_amount = maximum[price]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = price
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  ask = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if ask == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif ask == "yes":
    clear()
