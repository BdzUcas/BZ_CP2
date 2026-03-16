import math
from helper import *
import random
foods = {
    "kibble": {
        "hapiness": 0,
        "hunger": -20
    },
    "canned food": {
        "hapiness": 10,
        "hunger": -20
    },
    "hearty kibble": {
        "hapiness": 0,
        "hunger": -60
    },
    "high-quality canned food": {
        "hapiness": 20,
        "hunger": -40
    },
    "treats": {
        "hapiness": 30,
        "hunger": 0
    },
    "birdseed": {
        "hapiness": 0,
        "hunger": -20
    },
    "high-quality bird seed": {
        "hapiness": 20,
        "hunger": -40
    },
    "greens": {
        "hapiness": 10,
        "hunger": -10
    },
    "sand": {
        "hapiness": 20,
        "hunger": -20
    }
}
toys = {
    "stick": {
        "boredom": -10,
        "hapiness": 10,
        "durability": 0.9,
        "generic": "plays with the stick!",
        "dog": "plays fetch with the stick!",
        "cat": "gnaws on the stick!",
        "hampster": "looks at the stick!",
        "rock": "sits next to the stick!"
    },
    "rope": {
        "boredom": -10,
        "hapiness": 10,
        "durability": 0.2,
        "generic": "plays with the rope!",
        "dog": "plays tug with the rope!",
        "cat": "chases the rope!",
        "hampster": "chases the rope!",
        "rock": "sits next to the rope!"
    },
    "sqeaky toy": {
        "boredom": -30,
        "hapiness": 20,
        "durability": 0.5,
        "generic": "plays with the squaky toy!",
        "dog": "plays with the squeaky toy!",
        "cat": "plays with the squeaky toy!",
        "hampster": "plays with the squeaky toy!",
        "dog": "sits next to the squeaky toy!"
    },
    "frisbee": {
        "boredom": -30,
        "hapiness": 10,
        "durability": 0.2,
        "generic": "plays with the frisbee!",
        "dog": "plays fetch with the frisbee!",
        "cat": "sits on top of the frisbee!",
        "hampster": "runs around the frisbee!",
        "dog": "sits next to the frisbee!"
    },
    "string": {
        "boredom": -10,
        "hapiness": 10,
        "durability": 1,
        "generic": "plays with the string!",
        "dog": "eats the string!",
        "cat": "swats at the string!",
        "hampster": "chases the string!",
        "rock": "sits next to the string!"
    },
    "ball": {
        "boredom": -10,
        "hapiness": 30,
        "durability": 0.3,
        "generic": "plays with the ball!",
        "dog": "plays fetch with the ball!",
        "cat": "rolls the ball around!",
        "hampster": "runs inside the ball!",
        "rock": "sits next to the ball!"
    },
    "rock": {
        "boredom": 0,
        "hapiness": 0,
        "durability": 0,
        "generic": "plays with the rock!",
        "dog": "tries to eat the rock!",
        "cat": "looks judgementally at the rock!",
        "hampster": "sits on the rock!",
        "rock": "is horrified!"
    }
}
#generic pet class
class pet:
    #init function
    def __init__(self,name,age,hapiness):
        #initialize name, age (in weeks), age (in ticks (8 hour periods)), hunger, hapiness, boredom, preferred foods, and animal type
        self.name = name
        self.age = age
        self.age_ticks = age * 21
        self.hunger = 0
        self.hapiness = hapiness
        self.boredom = 0
        self.diet = []
        self.type = "generic"
        self.asleep = False
    #die function
    def die(self):
        #delete object
        del self
    #tick function (happens every 8 hours)
    def tick(self):
        #if pet is asleep
        if self.asleep:
            #wake pet up and return
            print(f'{self.name} woke up!')
            self.asleep = False
            return
        costs = 0
        #increase pet age
        self.age_ticks += 1
        self.age = math.floor(self.age_ticks / 21)
        #increase pet hunger
        self.hunger += 20
        #increase pet boredom
        self.boredom += 10
        #if pet hunger went over 100%
        if self.hunger > 100:
            #tell the user their pet starved to death
            print(f"{self.name} has starved to death!")
            #kill the pet
            self.die()
        #if the boredom is over 10%
        if self.boredom > 10:
            #50% chance for a random event to happen
            if chance(0.5):
                #choose a random event
                event = random.choice(['self_play','wander','trouble'])
                match event:
                    #if it was playing by themselves
                    case 'self_play':
                        #tell the user their pet played by itself
                        print(f"{self.name} was bored and played by themselves.\n{self.name}'s boredom decreased!\n{self.name}'s hapiness decreased.")
                        #decrease boredom and hapiness
                        self.boredom -= 10
                        self.hapiness -= 10
                    #if it was wandering
                    case 'wander':
                        #tell the user their pet got out of the house
                        print(f"{self.name} was bored and got out of the house!")
                        #percent chance based on age (newborn has 80% chance of being lost, 8 or more weeks has 10% chance of being lost)
                        lost_chance = 0.9 - self.age/10
                        if lost_chance < 0.1:
                            lost_chance = 0.1
                        if chance(lost_chance):
                            #tell the user their pet is lost
                            print("They got lost! There's no hope of finding them.")
                            #kill the pet
                            self.die()
                        #otherwise
                        else:
                            #tell the user a neighbor brought them back
                            print('A friendly neighbor brought them back!')
                            print('Boredom decreased!')
                            #decrease boredom
                            self.boredom -= 10
                    #if it was getting into trouble
                    case 'trouble':
                        #tell the user their pet broke some furniture and it will cost $10
                        print(f"{self.name} was bored and broke a peice of furniture!")
                        print("It cost you $10!")
                        #increase costs of this tick by 10
                        costs += 10
        #if hapiness is less than or equal to zero
        if self.hapiness <= 0:
            #set hapiness to 0
            self.hapiness = 0
            #tell the user their pet is sulking
            print(f"{self.name} is sulking!")
            print(f"{self.name}'s boredom increased.")
            #increase boredom
            self.boredom += 10
        #return costs
        return costs
    #feed method
    def feed(self, food):
        #if the food is not a food for that pet
        if not food in self.diet:
            #tell the user the pet rejects the food
            print(f"{self.name} rejects the food!")
        #otherwise
        else:
            #if hapiness is 0 (pet is sulking)
            if self.hapiness <= 0:
                #tell the user the pet eats the food halfheartedly
                print(f"{self.name} halfheartedly eats the food.")
                #increase hapiness by half the food's hapiness bonus
                self.hapiness += foods[food]["hapiness"]/2
            #otherwise if hapiness is greater than 100
            elif self.hapiness >= 100:
                #tell the user the pet enthusiastically eats the food
                print(f"{self.name} enthusiastically eats the food!")
                #increase hapiness by twice the food's hapiness bonus
                self.hapiness += foods[food]["hapiness"]*2
            #otherwise
            else:
                #tell the user the pet eats the food
                print(f"{self.name} ate the food.")
                #increase hapiness by the food's hapiness bonus
                self.hapiness += foods[food]["hapiness"]
            #increase hunger by the food's hunger bonus (negative)
            self.hunger += foods[food]["hunger"]
    #play method
    def play(self, toy):
        #display message (i.e. Rufus plays fetch with the frisbee!)
        print(f"{self.name} {toys[toy][self.type]}")
        #if toy is not a rock
        if not toy == "rock":
            #tell user hapiness increased and boredom decreased
            print("Hapiness increased!\nBoredom decreased!")
        #increase hapiness and boredom based on toy stats
        self.hapiness += toys[toy]['hapiness']
        self.boredom += toys[toy]['boredom']
        #random chance based on toys durability:
        if chance(toys[toy]["durability"]):
            #tell user toy broke and return true
            print(f'The {toy} broke!')
            return True
        #return false
        return False