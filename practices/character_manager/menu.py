from helper import *
from time import sleep
from game import Game
from data import get_dicts
import random
def menu():
    #introduce the project
    print(f('clear','Welcome to...\n\n\n'))
    sleep(1)
    print(f('clear','Welcome to...\n\n' + f('red','ULTIMATE BATTLE SIMULATOR\n')))
    sleep(1.5)
    print(f('clear','Welcome to...\n\n' + f('red','ULTIMATE BATTLE SIMULATOR 3000\n')))
    sleep(1.5)
    print(f('clear','Welcome to...\n\n' + f('red','ULTIMATE BATTLE SIMULATOR 3000 II\n')))
    sleep(1.5)
    print(f('clear','Welcome to...\n\n' + f('red','ULTIMATE BATTLE SIMULATOR 3000 II v2.0\n')))
    sleep(2)
    print(f('clear','Welcome to...\n\n' + f('red','ULTIMATE BATTLE SIMULATOR 3000 II v2.0!!!!!\n')))
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
                fighters = get_dicts(game.fighters.values())
                potentials = search(fighters)
                potential_names = [fighter['name'] for fighter in potentials]
                fighter = list_choice(potential_names)
                if fighter:
                    game.fighters[fighter].display()
                input(f('green','press ENTER to return to menu > '))
                continue
            case 'quit':
                fighters = get_dicts(game.fighters.values())
                save_csv(fighters,'practices/character_manager/docs/fighters.csv')
                break
            case 'battle':
                fighters = list(game.fighters.values())
                user_fighters = []
                for fighter in fighters:
                    if fighter.owner == user:
                        user_fighters.append(fighter.name)
                fighter = list_choice(user_fighters,'Enter a fighter to battle:')
                if not fighter:
                    input(f('green','press ENTER to return to menu > '))
                    continue
                print(f('clear','Searching for a fighter your level.'))
                sleep(0.5)
                print(f('clear','Searching for a fighter your level..'))
                sleep(0.5)
                print(f('clear','Searching for a fighter your level...'))
                sleep(0.5)
                
                potentials = []
                for challenger in fighters:
                    cr = challenger.lvl - game.fighters[fighter].lvl
                    if cr < 2 and cr > -2 and challenger != game.fighters[fighter]:
                        potentials.append(challenger.name)
                if not potentials:
                    print('No fighters of a similar level!')
                    print('Make a new fighter, or wait for others to catch up!')
                    input(f('green','\npress ENTER to return to menu > '))
                    continue
                challenger = random.choice(potentials)
                print(f("clear","Challenger:\n"))
                game.fighters[challenger].display()
                input(f('green','\npress ENTER to start battle > '))
                game.battle(fighter,challenger)
menu()