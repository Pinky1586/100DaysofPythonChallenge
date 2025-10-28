print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
ticket_total = 0

if height >= 120:
    age = int(input("What is your age? "))
    photos = input("Do you want photos with your ticket? Y or N ")
    if age <= 12:
        ticket_total += 5
    elif age <= 18:
        ticket_total += 7
    else:
        ticket_total += 12

    if photos == "y" or "Y":
        ticket_total += 3

    print(f'Your total bill is ${ticket_total}')
else:
    print("Sorry, you have to grow taller before you can ride.")

