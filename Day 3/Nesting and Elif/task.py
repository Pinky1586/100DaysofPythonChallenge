print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    print("You can ride the rollercoaster.")
    if age <= 12:
        print("It will cost $5.")
    elif agee <=18:
        print("It will cost $7.")
    else:
        print("It will cost $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
