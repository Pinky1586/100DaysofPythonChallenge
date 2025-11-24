#Imports
import art
import random

#variables
player_hand = []
computer_hand = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_total_11 = 0
player_bust = False
computer_bust = False
player_blackjack = False
computer_blackjack = False


#function to deal cards to all players:
def dealing_fresh():
    count = 2
    while count > 0:
        dealing = random.choice(cards)
        player_hand.append(dealing)
        dealing = random.choice(cards)
        computer_hand.append(dealing)
        count -= 1

def blackjack_check(hand):
    if 11 in hand and 10 in hand:
        return True
    return False

def calculate_hand_totals(hand):
    """
    Returns two totals for a hand:
      - total_as_is: counts all aces as 11
      - total_adjusted: best total ≤ 21, counting some aces as 1 if necessary
    """
    total_as_is = sum(hand)
    ace_count = hand.count(11)

    total_adjusted = total_as_is
    while total_adjusted > 21 and ace_count > 0:
        total_adjusted -= 10
        ace_count -= 1

    return total_as_is, total_adjusted


#informs player of game state
def print_game_state(player_total, player_alt_total, player_hand):
    if player_alt_total != player_total:   # means an ace adjustment exists
        print(f"    Your cards: {player_hand}, current total: {player_total} or {player_alt_total}.")
    else:
        print(f"    Your cards: {player_hand}, current total: {player_total}")


#function for player to draw card:
def player_draw_card():
    dealing = random.choice(cards)
    player_hand.append(dealing)

def computer_draws(hand):
    total, best_total = calculate_hand_totals(hand)
    print(f"Computer's starting hand: {hand}, total: {best_total}")  # always prints initial hand

    while best_total < 17:  # hit until 17
        hand.append(random.choice(cards))
        total, best_total = calculate_hand_totals(hand)
        print(f"Computer draws: {hand[-1]}, Computer hand: {hand}, total now: {best_total}")
    return total, best_total



def declaring_winner(player_total, player_best_total, computer_total, computer_best_total,
                     player_bust, computer_bust, player_blackjack, computer_blackjack):
    # Check for Blackjack first
    if player_blackjack and computer_blackjack:
        print("Both you and the computer have Blackjack! It's a tie!")
        return
    elif player_blackjack:
        print("Congratulations! You have a Blackjack! You win!")
        return
    elif computer_blackjack:
        print("The computer has a Blackjack! You lose!")
        return

    # Check for busts
    if player_bust and computer_bust:
        print("Both players busted! It's a tie!")
        return
    elif player_bust:
        print("You went bust! You lose!")
        return
    elif computer_bust:
        print(f"Computer went bust! You win! Your score: {player_best_total}")
        return

    # Neither busted nor blackjack → compare scores
    if player_best_total > computer_best_total:
        print(f"You win! Your score {player_best_total} beats computer's {computer_best_total}")
    elif player_best_total < computer_best_total:
        print(f"You lose! Your score {player_best_total} loses to computer's {computer_best_total}")
    else:
        print(f"It's a tie! Both scored {player_best_total}")


# print welcome artwork
print(art.welcome)
print(art.logo)
print(art.table)



###Code starts here###
#allows us to iterate
play_condition = input(f"Do you want to play a game of blackjack 'y' for yes, 'n' for no. ").lower()

while play_condition == 'y':
    player_hand.clear()
    computer_hand.clear()
    player_bust = False
    computer_bust = False
    player_blackjack = False
    computer_blackjack = False

    dealing_fresh()
    print(f"Computer's first card: {computer_hand[0]}")

    player_total, player_best_total = calculate_hand_totals(player_hand)
    computer_total, computer_best_total = calculate_hand_totals(computer_hand)

    # check blackjack
    if blackjack_check(player_hand):
        player_blackjack = True
    if blackjack_check(computer_hand):
        computer_blackjack = True
        print("Computer has a Blackjack!")

    # if either has blackjack, immediately declare winner and skip to next game
    if player_blackjack or computer_blackjack:
        declaring_winner(
            player_total,
            player_best_total,
            computer_total,
            computer_best_total,
            player_bust,
            computer_bust,
            player_blackjack,
            computer_blackjack
        )
        play_condition = input("Play again? y/n: ").lower()
        continue

    print_game_state(player_total, player_best_total, player_hand)

    # player draw loop
    draw_condition = input("Draw a card? y/n: ").lower()
    while draw_condition == 'y':
        player_draw_card()
        player_total, player_best_total = calculate_hand_totals(player_hand)
        print_game_state(player_total, player_best_total, player_hand)
        if player_best_total > 21:
            print("You went bust!")
            player_bust = True
            break
        draw_condition = input("Draw another card? y/n: ").lower()

    # computer draws after player is done (if player didn't bust)
    if not player_bust:
        computer_total, computer_best_total = computer_draws(computer_hand)
        if computer_best_total > 21:
            computer_bust = True

    # determine winner
    declaring_winner(
        player_total,
        player_best_total,
        computer_total,
        computer_best_total,
        player_bust,
        computer_bust,
        player_blackjack,
        computer_blackjack
    )

    play_condition = input("Play again? y/n: ").lower()
