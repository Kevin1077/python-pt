
import art

print(art.logo)

decision = "yes"
auction_dic = {}

def high_bid(dic):
    highest = 0
    bidder = ""
    for key in dic:
        bid_amount = (dic[key])
        if bid_amount >= highest:
            highest = bid_amount
            bidder = key

    print(f"The highest bid is {highest} from the bidder {bidder}")

while decision == "yes":
    name = input("Enter your name\n")
    bid  = int(input("Enter your bid\n"))
    auction_dic[name] = bid
    decision = input("Do you want to continue (yes/no)").lower()
    if decision == "no":
        high_bid(auction_dic)
        break

    elif decision == "yes":
        print("\n" * 100)
