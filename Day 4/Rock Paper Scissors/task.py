import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

print(f'Welcome to')

print(f'ROCK', rock)
print(f'PAPER', paper)
print(f'SCISSORS', scissors)

human = int(input("Make your choice: Rock, Paper, or Scissors (0, 1, 2) "))

computer = random.randint(0, 2)

print(images[human], images[computer])

if human == 0 and computer == 2:
    print(f"Rock beats Scissors. You win!")
elif human == 1 and computer == 0:
    print(f"Paper beats Rock. You win!")
elif human == 3 and computer == 2:
    print(f'Scissors beats Paper. You win!')
elif human == 0 and computer == 1:
    print(f'Paper beats Rock. You lose!')
elif human == 1 and computer == 2:
    print(f'Scissors beats Paper. You lose!')
elif human == 2 and computer == 0:
    print(f'Rock beats Scissors. You lose!')
elif human == computer:
    print(f'It is a tie. Try again!')