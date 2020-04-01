from random import randint

player_health = 3
ai_health = 3
items = ['scisors','paper','stone']
ai_selection = ''
player_selection = ''
application = 0

def ai_select():
    ai_selection = items[(randint(0,2))]
    return ai_selection

def decesion(arg1, arg2):
    if arg1 == 'scisors' and arg2 == 'paper':
        print('scicors will cut the paper')
        print('AI have lost 1 HP')
        decider = 1
        return decider
    elif arg1 == 'scisors' and arg2 == 'stone':
        print('the stone will crush the scisors')
        print('You have lost 1 HP')
        decider = 0
        return decider
    if arg1 == 'paper' and arg2 == 'stone':
        print('paper will grab the stone')
        print('AI have lost 1 HP')
        decider = 1
        return decider
    elif arg1 == 'paper' and arg2 == 'scisors':
        print('the scisor will cut the paper')
        print('You have lost 1 HP')
        decider = 0
        return decider
    if arg1 == 'stone' and arg2 == 'scisors':
        print('stone will crush the scisors')
        print('AI have lost 1 HP')
        decider = 1
        return decider
    elif arg1 == 'stone' and arg2 == 'paper':
        print('paper will grab the stone')
        print('You have lost 1 HP')   
        decider = 0
        return decider
    else:
        print('its a draw')
        print('Try again!')
        decider = 2
        return decider
    

while True:
    print('Your health is {} and AI health is {}'.format(player_health,ai_health))
    if ai_health == 0:
        print('AI reached zero helth and You Won!')
        break
    elif player_health == 0:
        print('You reached zero health and Lost!')
        break
    ai_selection = ai_select()
    while True:
        player_selection = input('Enter your selection: ')
        if player_selection in items:
            break
        else:
            print('Wrong selection! Try again!')
            continue
    print('AI selected {} and you selected {} So:'.format(ai_selection, player_selection))
    application = decesion(player_selection, ai_selection)
    if application == 1:
        ai_health -= 1
    elif application == 0:
        player_health -= 1