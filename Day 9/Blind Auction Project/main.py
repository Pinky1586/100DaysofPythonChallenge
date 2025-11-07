# TODO-1: Ask the user for input
import art

print(art.logo)

print("Welcome to the secret auction program.")
players_bids = {

}
name = input("What is your name?: ")
bid = input("What's your bid?: $ ")
# TODO-2: Save data into dictionary {name: price}
players_bids[name] = bid

# TODO-3: Whether if new bids need to be added
new_bidders = input("Are there any other bidders? Type 'y' or 'n': ")

while new_bidders == 'y':
    print("\n" * 100)
    name = input("What is your name?: ")
    bid = input("What's your bid?: ")
    players_bids[name] = bid
    new_bidders = input("Are there any other bidders? Type 'y' or 'n': ")

# TODO-4: Compare bids in dictionary
max_key = max(players_bids, key=players_bids.get)
max_bid = max(players_bids.values())

print(f"Congratulations {max_key}! You are the winning bidder with a bid of ${max_bid}!")

