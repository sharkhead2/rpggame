import random
import functions as f
import dictionary as d

class Ability(object):
    def __init__(self, damagemult, healmult, block, adrenaline, level, damagetype = False):
        self.damagemult = damagemult
        self.heal = heal
        self.block = block
        self.adrenaline = adrenaline
        self.damagetype = damagetype
        self.level = level




class Abilities(object):
    def __init__(self):
        self.abilities = {}
    def train_HeavyStrike(self):
        if 'HeavyStrike' not in self.abilities:
            HeavyStrike = Ability(100, False, False, 60, 1, 'normal')
            self.abilities['HeavyStrike'] = HeavyStrike
        elif self.abilities['HeavyStrike'].level == 1:
            self.abilities['HeavyStrike'].level = 2
            self.abilities['HeavyStrike'].damagemult = 150
            self.abilities['HeavyStrike'].adrenaline = 50
        elif self.abilities['HeavyStrike'].level == 2:
            self.abilities['HeavyStrike'].level = 3
            self.abilities['HeavyStrike'].damagemult = 200
            self.abilities['HeavyStrike'].adrenaline = 50
        else:
            #Can't upgrade past level 3
            pass
    def train_SecondWind(self):
        if 'SecondWind' not in self.abilities:
            SecondWind = Ability(False, 0.15, False, 10, 1)
            self.abilities['SecondWind'] = SecondWind
        elif self.abilities['SecondWind'].level == 1:
            self.abilities['SecondWind'].level = 2
            self.abilities['SecondWind'].heal = 0.25
            self.abilities['SecondWind'].adrenaline = 20
        elif self.abilities['SecondWind'].level == 2:
            self.abilities['SecondWind'].level = 3
            self.abilities['SecondWind'].heal = 0.4
            self.abilities['SecondWind'].adrenaline = 30
        else:
            #Can't upgrade past level 3
            pass
    def train_StunAttack(self):
        if 'StunAttack' not in self.abilities:
            StunAttack = Ability(5, False, False, 10, 1, 'stun')
            self.abilities['StunAttack'] = SecondWind
        elif self.abilities['StunAttack'].level == 1:
            self.abilities['StunAttack'].level = 2
            self.abilities['StunAttack'].damagemult = 10
            self.abilities['StunAttack'].adrenaline = 10
        elif self.abilities['StunAttack'].level == 2:
            self.abilities['StunAttack'].level = 3
            self.abilities['StunAttack'].damagemult = 15
            self.abilities['StunAttack'].adrenaline = 8
        else:
            #Can't upgrade past level 3
            pass
    # def train_BlindingBlow(self):
    #     if 'BlindingBlow' not in self.abilities:
    #         BlindingBlow = Ability(20, False, False, 15, 1, 'stun')
    #         self.abilities['BlindingBlow'] = BlindingBlow
    #     elif self.abilities['BlindingBlow'].level == 1:
    #         self.abilities['BlindingBlow'].level = 2
    #         self.abilities['BlindingBlow'].heal = 0.25
    #         self.abilities['BlindingBlow'].adrenaline = 20
    #     elif self.abilities['BlindingBlow'].level == 2:
    #         self.abilities['BlindingBlow'].level = 3
    #         self.abilities['BlindingBlow'].heal = 0.4
    #         self.abilities['BlindingBlow'].adrenaline = 30
    #     else:
    #         #Can't upgrade past level 3
    #         pass



#Abilities in game
