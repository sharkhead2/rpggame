import dictionary as d
import random
import classes as c
import functions as f

def make_name():
    if random.randrange(1, 100) == 34:
        return "Ryan The Poonster"
    elif random.randrange(1, 100) == 54:
        return "Theo The Rode"
    elif random.randrange(1, 100) == 98:
        return "Murray The Rodester"
    elif random.randrange(1, 100) == 78:
        return "Timo Rodestar"
    name = ''
    name += random.choice(d.monster1)
    name += ' '
    name += random.choice(d.monster2)
    if random.randrange(0, 10) < 6:
        name += ' '
        name += random.choice(d.monster3)
    return name

def choose_move(monster, player):
    #AI code goes here
    if player.tempbattlemove == 'nothing' and monster.adrenaline > 5:
        return 'attack'
    if player.health < monster.damage and monster.adrenaline > 10:
        return 'attack'
    if monster.health <= 80 and monster.adrenaline >= 30:
        chance = random.randrange(0, 10)
        if chance in range(0, 6):
            return 'block'
    if monster.adrenaline <= 40:
        chance = random.randrange(0, 10)
        if chance in range(0, 7):
            return 'dodge'
    if monster.adrenaline >= 5:
        if player.tempbattlemove != 'attack':
            if random.randrange(1, 100) > 25:
                return 'attack'
            else:
                return("Nothing")
        else:
            return 'attack'

class Monster(c.Person):

    def level_scale(self, player):
        if player.level > self.maxlevel:
            if player.level - 2 > self.maxlevel:
                self.level = player.level - 2
            else:
                self.level = self.maxlevel
        else:
            self.level = self.maxlevel
    def get_gear(self):
        helmet = c.Helmet.helmet_gen(self.level)
        arms = c.Arms.arms_gen(self.level)
        chest = c.Chest.chest_gen(self.level)
        leggings = c.Leggings.leggings_gen(self.level)
        boots = c.Boots.boots_gen(self.level)
        self.equip_helmet(helmet)
        self.equip_arms(arms)
        self.equip_chest(chest)
        self.equip_leggings(leggings)
        self.equip_boots(boots)
    def get_weapon(self):
        y = ['c.Sword.sword_gen(self.level)', 'c.Dagger.dagger_gen(self.level)', 'c.Mace.mace_gen(self.level)', 'c.Club.club_gen(self.level)', 'c.Spear.spear_gen(self.level)', 'c.Frying_Pan.fryingpan_gen(self.level)', 'c.Axe.axe_gen(self.level)', 'c.Heavy_Blunt.heavyblunt_gen(self.level)']
        type = random.choice(y)
        self.equip_weapon(eval(type))
    def loot_drop(self):
        y = ['self.weapon', 'self.helmet', 'self.arms', 'self.chest', 'self.leggings', 'self.boots']
        drop = random.choice(y)
        return eval(drop)
    def attack_damage(self):
        pass
    def __init__(self, name, maxlevel, player):
        self.devmode = False
        self.name = name
        self.maxlevel = maxlevel
        self.armorperk = 1
        self.damageperk = 1
        self.healthperk = 1
        self.critchanceincrease = 1
        self.dodgechanceincrease = 1
        self.blockchanceincrease = 1
        self.critdamageincrease = 1
        self.weapon = None
        self.helmet = None
        self.arms = None
        self.chest = None
        self.leggings = None
        self.boots = None
        self.level_scale(player)
        self.get_gear()
        self.get_weapon()
        self.health = self.getmaxhealth()
        self.player = False
        self.tempbattlemove = None
        self.dead = False
        self.adrenaline = 100
    def get_anger(self):
        if self.health > int(self.getmaxhealth() - 50):
            return "Happy"
        elif self.health < 50:
            return "Really Mad"
        elif self.health < 100:
            return "Somewhat Mad"
        elif int(self.getmaxhealth()/2) > self.health:
            return "Kind of Enraged"
        elif self.health > int(self.getmaxhealth() - 150):
            return "Somewhat Happy"
        elif self.health < int(self.getmaxhealth() * (3/4)):
            return "Probably Mad"
        elif self.health < int(self.getmaxhealth() * (7/8)):
            return "Probably Happy-ish"
        else:
            return "Can't Decide"
    @classmethod
    def mercenary_gen(cls, maxlevel, player):
        name = make_name()
        return cls(name, maxlevel, player)


f.clear()
# player = c.Person('bob')
# monster = Monster.mercenary_gen(1, player)
# monster.printequipedweapon()
# monster.printequipedhelmet()
# monster.printequipedarms()
# monster.printequipedchest()
# monster.printequipedleggings()
# monster.printequipedboots()
# print monster.name
# print "Health " + str(monster.health)
# print "Damage " + str(monster.damage)
# print "Armor " + str(monster.armor)
# drop = monster.loot_drop()
# f.print_loot(drop)
#
#
# monster.print_adrenaline()
# monster.lose_adrenaline(50)
# monster.print_adrenaline()
# monster.add_adrenaline(100)
# monster.print_adrenaline()
# monster.lose_adrenaline(500)
# monster.print_adrenaline()
# monster.take_battledamage(500)
# print "Health " + str(monster.health)
