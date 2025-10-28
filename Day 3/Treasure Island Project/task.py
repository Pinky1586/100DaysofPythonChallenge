print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
#This is the basic intro plotline
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
input("You exit your boat and walk down the path. <Press Enter to Continue> ")
input("After some time, you come to a 'Y' in the path. <Press Enter to Continue> ")
input("You look down the left path. It looks much like the path you are already on. <Press Enter to Continue> ")
input("The path to the right looks very dark, and full of mosquitoes. <Press Enter to Continue> ")

#This is the first choice you have to make after getting off the boat.
boat_path = input("Which path do you choose? <L for Left or R for Right> ")
if boat_path == 'L' or boat_path == 'l':
    lake_path = input("You walk down the path to the left. It winds through grasses and over logs until you reach a lake. "
          "Do you fish or swim? <F for Fish or S for Swim>")
    if lake_path == 'F' or lake_path == 'f':
        input("You have realized you are hungry and decide to see if there are any fish in the lake. <Press Enter to Continue> ")
        input("You take out your trustiest fishing line and lure and cast into the lake. <Press Enter to Continue> ")
        input("Much time passes when you suddenly feel a tug on your fishing line! <Press Enter to Continue> ")
        big_fish = input("Oh my! You have caught a giant fish! Do you eat the fish or do you let the fish go? <Press E for Eat or R for Release> ")
    if lake_path == 'S' or lake_path == 's':
        input("You tighten your pack and wade into the lake. The water is cold. You wade out a little further. <Press Enter to Continue> ")
        input("After breast-stroking for what feels like forever, you are suddenly knocked unconscious by a giant fish! <Press Enter to Continue> ")
        input("You sink to the bottom of the lake where you drown. <Press Enter to Continue> ")
        if big_fish == 'E' or big_fish == 'e':
            input("You whack the fish heartily against a rock. You build a fire and cook, then eat your fish. <Press Enter to Continue> ")
            input("While sitting in the sun your eyelids start to droop and you fall into a deep sleep and forget about the treasure. <Press Enter to Continue> ")
        else:
            input("As you are taking the lure from the fish's mouth, you catch his eye. As you look him in the eye, you begin to feel sad. <Press Enter to Continue>")
            input("You realize you cannot eat this fish now, and set him free. You pack your gear and continue down the path. <Press Enter to Continue> ")
            input("While you are trekking down the path you trip and break your ankle. You lay there and slowly die from starvation. <Press Enter to Continue> ")

#This is the first choice you have to make after getting off the boat.
if boat_path == 'R' or boat_path == 'r':
    input("You decide that it has been long enough since you've been covered from head to toe in mosquito bites. <Press Enter to Continue> ")
    input("You venture down the path to the right. Before long, you find yourself in a very dark and scary forest. <Press Enter to Continue> ")
    input("After wandering for hours you can neither find the way you came into the forest, nor the way out of the forest. YOU ARE LOST! <Press Enter to Continue> ")

print("THE END")
print("Plotline decided by a 6-year-old")
print("6-year-old said they like to make people get lost-")

