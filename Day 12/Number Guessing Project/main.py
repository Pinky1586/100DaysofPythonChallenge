import random
import art
print(art.logo2)

guess_left = 0
play_status = True



#def check_guess(guess, computer)

def check_level(level):
    if level == 'easy':
        return 10
    if level == 'hard':
        return 5



while play_status == True:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    # determine the computer's guess:
    computer = random.randint(1, 100)

    #determine player level
    level = input("Choose a difficulty. Type 'easy' or 'hard'. ").lower()

    guess_left = check_level(level)

    print(f'You have {guess_left} guesses remaining to guess the number')
    guess = int(input(f'Make a guess.'))

    #check guess
    while guess_left >= 1:
        if guess != computer:
            if guess > computer:
                print(f'Too high.')
            elif guess < computer:
                print(f'Too low.')

            guess_left -= 1
            print(f'Guess again.')
            if guess_left > 0:
                print(f'You have {guess_left} guesses left.')
            else:
                print(f'This is your final guess! ')
        guess = int(input(f'Make another guess.'))

        if guess == computer:
            print(f'You got it! The answer was {computer}!')
            break

    if guess_left < 1 and guess != computer:
        print(f'Too bad! You ran out of guesses! You lose!')
    play_again = input(f'Would you like to play another game? Type "yes" or "no". ').lower()
    if play_again == "yes":
        play_status = True
    else:
        play_status = False

print(f'Thanks for playing!')