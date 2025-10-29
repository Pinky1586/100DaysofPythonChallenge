letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random

#This is the Easy version

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

input_lett = nr_letters
input_symbols = nr_symbols
input_numbers = nr_numbers

lett = []
symb = []
numb = []

while nr_letters > 0:
    random_lett = random.choice(letters)
    lett.append(random_lett)
    nr_letters -= 1

while nr_numbers > 0:
    random_num = random.choice(numbers)
    numb.append(random_num)
    nr_numbers -= 1

while nr_symbols > 0:
    random_symbol = random.choice(symbols)
    symb.append(random_symbol)
    nr_symbols -= 1

#This section is commented out for the hard version
#combined_lett = "".join(lett)
#combined_numb = "".join(numb)
#combined_symb = "".join(symb)

#print(f'Your new password is: ' + combined_lett + combined_symb + combined_numb)

#Begin Hard version here
hard_string = []



#while input_lett > 0 and input_symbols > 0 and input_numbers > 0:
while input_lett > 0 or input_symbols > 0 or input_numbers > 0:
    #random_num = random.randint(1, 4)
    random_num = random.randint(1, 3)

    #Make sure that if we have exhausted a character type, we pick again.
    if input_lett <= 0 and random_num == 1:
        continue
    if input_symbols <= 0 and random_num == 2:
        continue
    if input_numbers <= 0 and random_num == 3:
        continue

    if random_num == 1:
        #letter = random.choice(random_lett)
        #hard_string.append(lett)
        letter = random.choice(lett)
        hard_string.append(letter)
        #random_lett.remove(letter)
        lett.remove(letter)
        input_lett -= 1
    elif random_num == 2:
        #symbols = random.choice(random_symbol)
        #hard_string.append(symb)
        symbols = random.choice(symb)
        hard_string.append(symbols)
        #random_symbol.remove(symbols)
        symb.remove(symbols)
        input_symbols -= 1
    else:
        #numbers = random.choice(random_num)
        #hard_string.append(numb)
        numbers = random.choice(numb)
        hard_string.append(numbers)
        #random_num.remove(numbers)
        numb.remove(numbers)
        input_numbers -= 1

combined_hard_string = "".join(hard_string)

print(f'Your new password is: ' + combined_hard_string)


