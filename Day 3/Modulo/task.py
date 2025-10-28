user_number = int(input("Enter a number and I will tell you if it's odd or even "))
mod_number = user_number % 2

if mod_number == 0:
    print("Your number is even")
else:
    print("Your number is odd")