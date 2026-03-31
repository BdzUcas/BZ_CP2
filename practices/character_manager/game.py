from fighter import Fighter
import random as r
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
            fighter = Fighter(f['name'],f['char_class'],f['max_hp'],f['atk'],f['block'],f['xp'],f['owner'])
            fighters[f['name']] = fighter
        self.fighters = fighters
    def add_fighter(self,user,name,char_class):
        hp = r.randint(20,30)
        atk = r.randint(3,5) + classes[char_class]['atk']
        block = r.randint(1,3) + classes[char_class]['def']
        fighter = Fighter(name,char_class,hp,atk,block,0,user)
        self.fighters[name] = (fighter)