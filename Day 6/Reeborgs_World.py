#This is the code from the Reeborg's World Challenges which are done in the web application
#This is the code for getting Reeborg to solve the maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() == 0:
    while front_is_clear():
        move()
    while wall_in_front() and right_is_clear():
        turn_right()
    while wall_in_front() and not right_is_clear():
        turn_left()
