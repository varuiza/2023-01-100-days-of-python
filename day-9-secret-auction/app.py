import os
from art import logo

bidding_finished = False
bids = {}


def add_new_bid(user_name, bid_amount):
    bids[user_name] = bid_amount


def find_highest_bid(bids):
    highest_bid_name = "Brrrr"
    highest_bid_amount = 0
    for user in bids:
        print(f"{user} bidded for {bids[user]}€")
        if highest_bid_amount < bids[user]:
            highest_bid_amount = bids[user]
            highest_bid_name = user
    print()
    print(f"And the winner is...\n\n{highest_bid_name}!!")


while not bidding_finished:

    # Clearing the Screen
    os.system('cls')

    print(logo)
    print("Welcome to the Secret Auction!\n")
    name = input("What's your name?\n")
    bid = int(input("\nHow much are you willing to pay for this exclusive item?\n"))

    add_new_bid(user_name=name, bid_amount=bid)

    more_users = input(
        "\nAre there more users who want to bid? Type \"yes\" or \"no\"\n")
    if more_users == "no":
        bidding_finished = True

os.system('cls')
find_highest_bid(bids)
