from formatting import f
from helper import *
from time import sleep
import json
#time variable stores current hour (1-24) in game. Doing activities increases it. As time increases events occur that can cause decreases in resources, so you have to balance your time between obtaining different resources.
time = 8
#hapiness stores your current hapiness level. The higher your hapiness the more effective activities will be. Getting good sleep increases hapiness but not sleeping or working too much cause your hapiness to go down. Certain activities with your pet increase your hapiness.
hapiness = 5
#money stores how much in-game money you have. This is gained by working and spent on food for yourself and your pets, or toys for your pets to increase hapiness.
money = 100
#inventory stores what resources you have. This includes food and toys for your pets. It is a list of strings (ie 'pet food' 'tug rope')
inventory = []
def menu():
    print(f"{f('###')} Pet Simulator {f('###')}")
    print(f'Welcome to the {f('cyan', 'pet simulator')}!')
    print(f'Do you need instructions? ({f('lime','yes')}/{f('bright red','no')})')
    instruct = choice_input(['y','n','yes','no'])
    if instruct in ('y','yes'):
        print('This pet simulator lets you take care of pets!')
        sleep(1)
        print('You can have as many pets as you want, but multiple can be hard to take care of.')
        sleep(1)
        print("Pets will get hungry, bored, or sad if you don't care for them!")
        sleep(1)
        print("But properly caring for pets requires money and time, so you have to maintain a balance of work, play, and sleep.")
        sleep(1)
        print("Let's get started!")
    user = input('Enter username: ')
    try:
        with open(f'practices/pet_sim/docs/user_data/{user}.json','r') as file:
            account_data = json.load(file)
    except:
        with open(f'practices/pet_sim/docs/user_data/{user}.json','w') as file:
            account_data = {"time": 8, "hapiness": 5, "money": 100, "inventory": [], 'pets': []}
            json.dump(account_data,file)
        print('Account Registered!')
menu()