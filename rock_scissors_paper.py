#! python3
import random
import time

player_health = 3
ai_health = 3
items = ['rock','scissor','paper']
ai_selection = ''
player_selection = ''
application = 0
random.seed(time.time()) # to randomize the randint call everytime game gets executed

def ai_select(): # this functions selects one out of 3 options in items for AI
    ai_selection = items[(random.randint(0,2))]
    #print(ai_selection) # some cheating code here
    return ai_selection

def decesion(arg1, arg2):
    if arg1 == items[1] and arg2 == items[2]:
        print('scissor cuts paper! AI lost 1 HP')
        return 1
    elif arg1 == items[1] and arg2 == items[0]:
        print('rock breaks scissor! You lost 1 HP')
        return 0
    if arg1 == items[2] and arg2 == items[0]:
        print('paper covers rock! AI lost 1 HP')
        return 1
    elif arg1 == items[2] and arg2 == items[1]:
        print('scissor cuts paper! You lost 1 HP')
        return 0
    if arg1 == items[0] and arg2 == items[1]:
        print('rock breaks scissor! AI lost 1 HP')
        return 1
    elif arg1 == items[0] and arg2 == items[2]:
        print('paper covers rock! You lost 1 HP')  
        return 0
    else:
        print('its a draw. Try again!')
        return 2
    
while True:
    print('####### ROCK, SCISSOR, PAPER ####### v.1')
    print('Your health is {} and AI health is {}'.format(player_health,ai_health))
    if ai_health == 0:
        print('yaaaaaaaay! You WON!')
        break
    elif player_health == 0:
        print('oooooooops! You LOST!')
        break
    ai_selection = ai_select()
    while True:
        player_selection = input('what do you pick? ')
        if player_selection in items:
            break
        else:
            print('wrong selection! Try again!')
            continue
    print('AI selected {} and you selected {} So: '.format(ai_selection, player_selection),end='')
    application = decesion(player_selection, ai_selection)
    if application == 1:
        ai_health -= 1
    elif application == 0:
        player_health -= 1