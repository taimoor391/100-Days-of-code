import Auction_logo
print(Auction_logo.logo)

from replit import clear

import art

print(art.logo)


def bids(name, bid):
    bidders.append({"name": name,
                    "bid": bid})


def max_bid():
    for i, j in enumerate(bidders):
        bids.append(bidders[i]['bid'])
    for x, y in enumerate(bids):
        if y == max(bids):
            print("The winner is '{}' with a bid of {}".format(bidders[x]['name'], y))


bid_again = "yes"
bidders = []
while bid_again == "yes":
    name = input("Enter your name\n")
    bid = int(input("Enter your Bid \n"))

    bids(name, bid)
    bid_again = input("Do you want to enter more bids? yes/\n").lower()
    clear()
bids = []
max_bid()


