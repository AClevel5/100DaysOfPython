# Reeborgs world moving the robot to end point will not work in terminal. Hurdle 3 challenge


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while at_goal() == False:
    if wall_in_front() == True:
        jump_hurdle()
    else:
        move()
