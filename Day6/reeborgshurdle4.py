# Reeborgs world hurdle 4 challenge. Random hurdle placement and height.
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_hurdle():
    turn_left()
    while wall_on_right() == True:
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear() == True:
        move()
    turn_left()


while at_goal() == False:
    if wall_in_front() == True:
        jump_hurdle()
    else:
        move()
