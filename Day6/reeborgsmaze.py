# Reeborgs world maze.


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Prevent the infinite loop if the robot starts without a wall to the right.
while front_is_clear():
    move()
turn_left()


while at_goal() == False:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
