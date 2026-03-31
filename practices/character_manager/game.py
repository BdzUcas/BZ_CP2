from fighter import Fighter
import random as r
from time import sleep
from helper import f
classes = {
    "warrior": {
        "atk": 1,
        "def": 1
    },
    "wizard": {
        "atk": 2,
        "def": 0
    },
    "archer": {
        "atk": 0,
        "def": 2
    }
}
class Game:
    def __init__(self,fighter_dicts):
        fighters = {}
        for f in fighter_dicts:
            fighter = Fighter(f['name'],f['char_class'],int(f['max_hp']),int(f['atk']),int(f['block']),int(f['xp']),f['owner'])
            fighters[f['name']] = fighter
        self.fighters = fighters
    def add_fighter(self,user,name,char_class):
        hp = r.randint(20,30)
        atk = r.randint(3,5) + classes[char_class]['atk']
        block = r.randint(1,3) + classes[char_class]['def']
        fighter = Fighter(name,char_class,hp,atk,block,0,user)
        self.fighters[name] = (fighter)
    def battle(self,fighter,challenger):
        round = 1
        while True:
            print(f('clear',f'Round {round}'))
            sleep(1)
            print(f"{fighter}'s turn!")
            sleep(1)
            print(f'{fighter} attacks!')
            sleep(1)
            dmg = r.randint(0,5) + self.fighters[fighter].atk
            if r.randint(1,10) == 10:
                print(f('red','CRITICAL'))
                sleep(0.5)
                print(f('clear',f"Round {round}\n{fighter}'s turn!\n{fighter} attacks!\n{f('red','CRITICAL HIT')}"))
                sleep(0.5)
            if self.fighters[challenger].hurt(dmg):
                xp = self.fighters[challenger].xp + r.randint(1,3)
                print(f'{self.fighters[fighter].name} gained {xp} xp!')
                self.fighters[fighter].gain_xp(xp)
                input(f('green','\npress ENTER to return to menu > '))
                return
            sleep(1)
            print(f('clear') + f"{challenger}'s turn!")
            sleep(1)
            print(f'{challenger} attacks!')
            sleep(1)
            dmg = r.randint(0,5) + self.fighters[challenger].atk
            if r.randint(1,10) == 10:
                print(f('red','CRITICAL'))
                sleep(0.5)
                print(f('clear',f"{challenger}'s turn!\n{challenger} attacks!\n{f('red','CRITICAL HIT')}"))
                dmg *= 2
                sleep(0.5)
            if self.fighters[fighter].hurt(dmg):
                xp = self.fighters[fighter].xp + r.randint(1,3)
                print(f'{self.fighters[challenger].name} gained {xp} xp!')
                self.fighters[challenger].gain_xp(xp)
                input(f('green','\npress ENTER to return to menu > '))
                return
            round += 1
            input(f('green','\npress ENTER to continue > '))