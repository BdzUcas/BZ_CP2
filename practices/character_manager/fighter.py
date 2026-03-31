from helper import *
#takes an xp amount and finds the relative level, with each level needing twice the amount of xp as the last. so for each level n the xp required is 2^n.
def xp_to_level(xp):
    xp = int(xp)
    i = 0
    if xp == 0:
        return 0
    while True:
        if xp <= 2 ** i:
            return i
        i += 1
class Fighter:
    def __init__(self,name,char_class,hp,atk,block,xp,owner):
        #name
        self.name = name
        #class
        self.char_class = char_class
        #max health
        self.max_hp = hp
        #current health
        self.hp = hp
        #attack stat
        self.atk = atk
        #defense stat
        self.block = block
        #experience points
        self.xp = xp
        #level
        self.lvl = xp_to_level(xp)
        #owner user
        self.owner = owner
    #show character info method
    def display(self):
        print(f'{f('###')} {f('red',self.name)} {f('###')}')
        print(f'Owner: {f('red',self.owner)}')
        print(f'Class: {f('red',self.char_class.title())}')
        print(f'Level: {f('red',self.lvl)}')
        print(f'Max Health: {f('red',self.max_hp)}')
        print(f'Attack: {f('red',self.atk)}')
        print(f'Defense: {f('red',self.block)}')
    #gain xp method
    def gain_xp(self,xp):
        prev_lvl = int(self.lvl)
        self.xp += xp
        self.lvl = xp_to_level(self.xp)
        if self.lvl > prev_lvl:
            print(f'{f('red',self.name)} leveled up to level {f('red',self.lvl)}!')
    #take damage method
    def hurt(self,damage):
        #block stat is subtracted from damage
        damage -= self.block
        if damage < 0:
            damage = 0
        self.hp -= damage
        #if health goes below zero
        if self.hp <= 0:
            #return true and set hp to max hp
            print(f'{f('red',self.name)} was {f('red','KNOCKED OUT!')}')
            self.hp = self.max_hp
            return True
        #otherwise:
        else:
            #tell user how much health is left
            print(f'{f('red',self.name)} has {f('red',round(self.hp))} health remaining!')