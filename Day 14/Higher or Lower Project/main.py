#Update number 2. I've begun working on some of the logic. I haven't yet completed the player's database.

from art import logo
from art import vs
import random
from game_data_pwhl import players

print(r'Get ready to play:')
print(logo)

player1 = random.choice(players)
player2 = random.choice(players)

print(f'{player1["name"]} plays {player1["position"]} for the {player1["team"]}')
print(vs)
print(f'{player2["name"]} plays {player2["position"]} for the {player2["team"]}')

print(f'Who has more Instagram followers A {player1["name"]} or B {player2["name"]}?: ')

