from helper import *
from time import sleep
from game import Game
import random as r
def menu():
    #introduce the project
    print('Welcome to...')
    sleep(1)
    print(f('red','ULTIMATE BATTLE SIMULATOR'))
    sleep(1)
    print(f('red','3000'))
    sleep(1)
    print(f('red','II'))
    sleep(1)
    print(f('red','v2.0'))
    sleep(1)
    print(f('red','!!!!!!'))
    sleep(1)
    input(f('green','press ENTER to start > '))
    #import fighter file
    fighters = csv_to_dictionary('practices/character_manager/docs/fighters.csv')
    game = Game(fighters)
    while True:
        user = uinput('Enter username:\n> ')
        print(f'Your username is: {user}')
        if choice_input(['y','n'],'Continue with this username (y/n)\n> ') == 'y':
            break
    while True:
        #main menu
        print(f('clear'),end='')
        print('MAIN MENU!')
        #ask user if they want to create a fighter, view their fighters, view global fighters, battle, or quit
        choice = list_choice(['create a fighter','view your fighters','view all fighters','battle','quit'])
        match choice:
            case 'create a fighter':
                name = input("What is your character's name?\n> \033[34m")
                print(f("white"),end='')
                if name in game.fighters.keys():
                    print('There is already a fighter with that name!')
                    input(f('green','press ENTER to return to menu > '))
                    continue
                print("What is your fighter's class?")
                char_class = list_choice(['warrior','wizard','archer'])
                print(f('clear','Generating stats.'))
                sleep(0.5)
                print(f('clear','Generating stats..'))
                sleep(0.5)
                print(f('clear','Generating stats...'))
                sleep(0.5)
                print(f('clear'),end='')
                game.add_fighter(user,name,char_class)
                game.fighters[name].display()
                input(f('green','press ENTER to return to menu > '))
                continue
            case 'view your fighters':
                user_fighters = []
                for fighter in game.fighters.values():
                    if fighter.owner == user:
                        user_fighters.append(fighter.name)
                fighter = list_choice(user_fighters,'Enter a fighter to see details:')
                if fighter:
                    print(f('clear'),end='')
                    game.fighters[fighter].display()
                    input(f('green','press ENTER to return to menu > '))
                    continue
            case 'view all fighters':
                fighters = []
                for fighter in game.fighters.values():
                    fighters.append(fighter.__dict__)
                potentials = search(fighters)
                potential_names = [fighter['name'] for fighter in potentials]
                fighter = list_choice(potential_names)
                game.fighters[fighter].display()
menu()
#cogitoergosum