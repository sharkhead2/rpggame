import time
import random
import dictionary as d
import subprocess
import WeaponExtras as we
import ArmorExtras as ae
from os import system, name
import Perks as p
from reprint import output

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class Armor(object):
    def __init__(self, level, type, armor, perks):
        self.level = level
        self.type = type
        self.armor = armor
        self.perks = perks

class Helmet(Armor):
    def __init__(self, name, level, type, armor, perks):
        self.name = name
        super(Helmet, self).__init__(level, type, armor, perks)
        self.gear = 'helmet'
    @classmethod
    def helmet_gen(cls, level):
        name = ae.helmetmakename()
        type = ae.armormaketype()
        armor = ae.makearmor(level, type)
        perks = p.Perks(level, type)
        return cls(name, level, type, armor, perks)

class Arms(Armor):
    def __init__(self, name, level, type, armor, perks):
        self.name = name
        super(Arms, self).__init__(level, type, armor, perks)
        self.gear = 'arms'
    @classmethod
    def arms_gen(cls, level):
        name = ae.armsmakename()
        type = ae.armormaketype()
        armor = ae.makearmor(level, type)
        perks = p.Perks(level, type)
        return cls(name, level, type, armor, perks)

class Chest(Armor):
    def __init__(self, name, level, type, armor, perks):
        self.name = name
        super(Chest, self).__init__(level, type, armor, perks)
        self.gear = 'chest'
    @classmethod
    def chest_gen(cls, level):
        name = ae.chestmakename()
        type = ae.armormaketype()
        armor = ae.makearmor(level, type)
        perks = p.Perks(level, type)
        return cls(name, level, type, armor, perks)

class Leggings(Armor):
    def __init__(self, name, level, type, armor, perks):
        self.name = name
        super(Leggings, self).__init__(level, type, armor, perks)
        self.gear = 'leggings'
    @classmethod
    def leggings_gen(cls, level):
        name = ae.leggingsmakename()
        type = ae.armormaketype()
        armor = ae.makearmor(level, type)
        perks = p.Perks(level, type)
        return cls(name, level, type, armor, perks)

class Boots(Armor):
    def __init__(self, name, level, type, armor, perks):
        self.name = name
        super(Boots, self).__init__(level, type, armor, perks)
        self.gear = 'boots'
    @classmethod
    def boots_gen(cls, level):
        name = ae.bootsmakename()
        type = ae.armormaketype()
        armor = ae.makearmor(level, type)
        perks = p.Perks(level, type)
        return cls(name, level, type, armor, perks)

class Weapon(object):
    def __init__(self, level, type, perks, damage):
        self.level = level
        self.type = type
        self.perks = perks
        self.damage = damage
        self.gear = 'weapon'
    def getname(self):
        return self.name
    def getlevel(self):
        return self.level
    def setlevel(self, gain):
        self.level += gain
    def gettype(self):
        return self.type
    @classmethod
    def normal_gen(cls, level):
        name = we.weaponmakename()
        type = we.weaponmaketype()
        perks = p.Perks(level, type)
        damage = we.weaponmakedamage(self.level, self.type)
        return cls(level, name, type, perks, damage)

class Sword(Weapon):
    def __init__(self, level, name, type, perks, damage):
        super(Sword, self).__init__(level, type, perks, damage)
        self.name = name
        self.critchance = 0
        self.dodgechance = 0
        self.blockchance = 0
        self.misschance = 0
        self.damagebuff = 1
        self.damageconsistency = 0.05
        self.damage *= self.damagebuff
        self.damage = int(self.damage)
    @classmethod
    def sword_gen(cls, level):
        name = we.swordmakename()
        type = we.weaponmaketype()
        perks = p.Perks(level, type)
        damage = we.weaponmakedamage(level, type)
        return cls(level, name, type, perks, damage)

class Dagger(Weapon):
    def __init__(self, level, name, type, perks, damage):
        super(Dagger, self).__init__(level, type, perks, damage)
        self.name = name
        self.critchance = 0.4
        self.dodgechance = -0.3
        self.blockchance = -0.1
        self.misschance = 0.2
        self.damagebuff = 0.8
        self.damageconsistency = 0.15
        self.damage *= self.damagebuff
        self.damage = int(self.damage)
    @classmethod
    def dagger_gen(cls, level):
        name = we.daggermakename()
        type = we.weaponmaketype()
        perks = p.Perks(level, type)
        damage = we.weaponmakedamage(level, type)
        return cls(level, name, type, perks, damage)

class Mace(Weapon):
    def __init__(self, level, name, type, perks, damage):
        super(Mace, self).__init__(level, type, perks, damage)
        self.name = name
        self.critchance = -0.2
        self.dodgechance = 0.1
        self.blockchance = 0
        self.misschance = 0.1
        self.damagebuff = 0.9
        self.damageconsistency = 0.03
        self.damage *= self.damagebuff
        self.damage = int(self.damage)
    @classmethod
    def mace_gen(cls, level):
        name = we.macemakename()
        type = we.weaponmaketype()
        perks = p.Perks(level, type)
        damage = we.weaponmakedamage(level, type)
        return cls(level, name, type, perks, damage)

class Club(Weapon):
    def __init__(self, level, name, type, perks, damage):
        super(Club, self).__init__(level, type, perks, damage)
        self.name = name
        self.critchance = -0.2
        self.dodgechance = 0
        self.blockchance = 0.2
        self.misschance = -0.1
        self.damagebuff = 1.1
        self.damageconsistency = 0.08
        self.damage *= self.damagebuff
        self.damage = int(self.damage)
    @classmethod
    def club_gen(cls, level):
        name = we.clubmakename()
        type = we.weaponmaketype()
        perks = p.Perks(level, type)
        damage = we.weaponmakedamage(level, type)
        return cls(level, name, type, perks, damage)

class Spear(Weapon):
    def __init__(self, level, name, type, perks, damage):
        super(Spear, self).__init__(level, type, perks, damage)
        self.name = name
        self.critchance = -0.3
        self.dodgechance = 0.2
        self.blockchance = 0.1
        self.misschance = -0.2
        self.damagebuff = 0.9
        self.damageconsistency = 0.1
        self.damage *= self.damagebuff
        self.damage = int(self.damage)
    @classmethod
    def spear_gen(cls, level):
        name = we.spearmakename()
        type = we.weaponmaketype()
        perks = p.Perks(level, type)
        damage = we.weaponmakedamage(level, type)
        return cls(level, name, type, perks, damage)

class Frying_Pan(Weapon):
    def __init__(self, level, name, type, perks, damage):
        super(Frying_Pan, self).__init__(level, type, perks, damage)
        self.name = name
        self.critchance = -0.3
        self.dodgechance = -0.2
        self.blockchance = 0.4
        self.misschance = 0.1
        self.damagebuff = 1.2
        self.damageconsistency = 0.11
        self.damage *= self.damagebuff
        self.damage = int(self.damage)
    @classmethod
    def fryingpan_gen(cls, level):
        name = we.fryingpanmakename()
        type = we.weaponmaketype()
        perks = p.Perks(level, type)
        damage = we.weaponmakedamage(level, type)
        return cls(level, name, type, perks, damage)

class Axe(Weapon):
    def __init__(self, level, name, type, perks, damage):
        super(Axe, self).__init__(level, type, perks, damage)
        self.name = name
        self.critchance = 0.1
        self.dodgechance = -0.1
        self.blockchance = -0.2
        self.misschance = 0
        self.damagebuff = 1.3
        self.damageconsistency = 0.16
        self.damage *= self.damagebuff
        self.damage = int(self.damage)
    @classmethod
    def axe_gen(cls, level):
        name = we.axemakename()
        type = we.weaponmaketype()
        perks = p.Perks(level, type)
        damage = we.weaponmakedamage(level, type)
        return cls(level, name, type, perks, damage)

class Heavy_Blunt(Weapon):
    def __init__(self, level, name, type, perks, damage):
        super(Heavy_Blunt, self).__init__(level, type, perks, damage)
        self.name = name
        self.critchance = -0.3
        self.dodgechance = 0.1
        self.blockchance = 0.1
        self.misschance = -0.3
        self.damagebuff = 1.4
        self.damageconsistency = 0.14
        self.damage *= self.damagebuff
        self.damage = int(self.damage)
    @classmethod
    def heavyblunt_gen(cls, level):
        name = we.heavybluntmakename()
        type = we.weaponmaketype()
        perks = p.Perks(level, type)
        damage = we.weaponmakedamage(level, type)
        return cls(level, name, type, perks, damage)

class Person(object):
    #Remember to remove dev mode
    def __init__(self, name):
        self.name = name
        if self.name == 'dev':
            self.devmode = True
            print('You have entered dev mode!')
            time.sleep(1)
        else:
            self.devmode = False
        self.level = 1
        self.xp = 0
        self.health = 500
        self.weaponinventory = []
        self.helmetinventory = []
        self.chestinventory = []
        self.armsinventory = []
        self.leggingsinventory = []
        self.bootsinventory = []
        self.armorperk = 1
        self.damageperk = 1
        self.healthperk = 1
        self.critchanceincrease = 1
        self.dodgechanceincrease = 1
        self.blockchanceincrease = 1
        self.misschanceincrease = 1
        self.critdamageincrease = 1
        self.damageconsistency = 0
        self.weapon = None
        self.helmet = None
        self.arms = None
        self.chest = None
        self.leggings = None
        self.boots = None
        self.damage = 0
        self.armor = 0
        self.player = True
        self.tempbattlemove = None
        self.dead = False
        self.critdamage = 0
        self.adrenaline = 100
    def set_damage(self):
        if self.weapon != None:
            base = self.weapon.damage
            damage = base * self.damageperk
            self.damage = int(damage)
            basecrit = self.damage * 1.3
            self.critdamage = int(basecrit * self.critdamageincrease)
    def set_armor(self):
        base = 0
        if self.helmet != None:
            base += self.helmet.armor
        if self.arms != None:
            base += self.arms.armor
        if self.chest != None:
            base += self.chest.armor
        if self.leggings != None:
            base += self.leggings.armor
        if self.boots != None:
            base += self.boots.armor
        armor = base * self.armorperk
        self.armor = int(armor)
    def set_perks(self):
        armorperk = 1
        damageperk = 1
        healthperk = 1
        critchanceincrease = 1
        dodgechance = 1
        blockchance = 1
        misschance = 1
        damageconsistency = 0
        if self.weapon != None:
            armorperk += self.weapon.perks.get_armor_strength()
            damageperk += self.weapon.perks.get_damage_strength()
            healthperk += self.weapon.perks.get_health_strength()
            critchanceincrease += self.weapon.perks.get_crit_chance()
            critchanceincrease += self.weapon.critchance
            blockchance += self.weapon.blockchance
            dodgechance += self.weapon.dodgechance
            misschance += self.weapon.misschance
            damageconsistency += self.weapon.damageconsistency
        if self.helmet != None:
            armorperk += self.helmet.perks.get_armor_strength()
            damageperk += self.helmet.perks.get_damage_strength()
            healthperk += self.helmet.perks.get_health_strength()
            critchanceincrease += self.helmet.perks.get_crit_chance()
        if self.arms != None:
            armorperk += self.arms.perks.get_armor_strength()
            damageperk += self.arms.perks.get_damage_strength()
            healthperk += self.arms.perks.get_health_strength()
            critchanceincrease += self.arms.perks.get_crit_chance()
        if self.chest != None:
            armorperk += self.chest.perks.get_armor_strength()
            damageperk += self.chest.perks.get_damage_strength()
            healthperk += self.chest.perks.get_health_strength()
            critchanceincrease += self.chest.perks.get_crit_chance()
        if self.leggings != None:
            armorperk += self.leggings.perks.get_armor_strength()
            damageperk += self.leggings.perks.get_damage_strength()
            healthperk += self.leggings.perks.get_health_strength()
            critchanceincrease += self.leggings.perks.get_crit_chance()
        if self.boots != None:
            armorperk += self.boots.perks.get_armor_strength()
            damageperk += self.boots.perks.get_damage_strength()
            healthperk += self.boots.perks.get_health_strength()
            critchanceincrease += self.boots.perks.get_crit_chance()
        self.critchanceincrease = critchanceincrease
        self.dodgechanceincrease = dodgechance
        self.blockchanceincrease = blockchance
        self.misschanceincrease = misschance
        if damageconsistency >= 0:
            self.damageconsistency = damageconsistency
        else:
            self.damageconsistency = 0
        self.armorperk = armorperk
        self.damageperk = damageperk
        self.healthperk = healthperk
    def equip_weapon(self, weapon):
        self.weapon = weapon
        self.set_perks()
        self.set_damage()
        self.set_armor()
    def equip_helmet(self, helmet):
        self.helmet = helmet
        self.set_perks()
        self.set_damage()
        self.set_armor()
    def equip_arms(self, arms):
        self.arms = arms
        self.set_perks()
        self.set_damage()
        self.set_armor()
    def equip_chest(self, chest):
        self.chest = chest
        self.set_perks()
        self.set_damage()
        self.set_armor()
    def equip_leggings(self, leggings):
        self.leggings = leggings
        self.set_perks()
        self.set_damage()
        self.set_armor()
    def equip_boots(self, boots):
        self.boots = boots
        self.set_perks()
        self.set_damage()
        self.set_armor()
    def setname(self, name):
        self.name = name
    def getxpcap(self):
        return self.level * 1000
    def getmaxhealth(self):
        return self.level * 500 * self.healthperk
    def subhealth(self, loss):
        print(str(self.name) + " took {} damage!".format(d.color.RED + str(loss) + d.color.END))
        self.health = int(self.health - loss)
        if self.health <= 0:
            if self.devmode:
                print("Do you want to die? ")
                devinput = raw_input("> ")
                if devinput.lower() in ['n', 'no', '1', 'nope']:
                    self.health += self.getmaxhealth()
                else:
                    self.death()
            else:
                self.death()
        else:
            print(str(self.name) + " now has {} health!".format(d.color.RED + str(self.health) + d.color.END))
    def addhealth(self, gain):
        self.health += gain
        if self.health > self.getmaxhealth():
            self.health = self.getmaxhealth()
    def death(self):
        print(str(self.name) + " died!")
        if self.player:
            self.dead = True
            #Run gameover function
        else:
            self.dead = True
    def setlevel(self, gain):
        self.level += gain
    def addxp(self, gain):
        self.xp += gain
        while self.getxpcap() <= self.xp:
            self.xp -= self.getxpcap()
            self.setlevel(1)
    def take_battledamage(self, damage):
        unrivaled = damage - self.armor
        if unrivaled <= 0:
            urrivaled = 0
        if damage > self.armor:
            rivaled = self.armor/2
        else:
            rivaled = damage/2
        final = unrivaled + rivaled
        if final < 0:
            raise Exception('An entity took negative damage, contact support!')
        self.subhealth(final)
    def calculate_attackdamage(self):
        variationup = 1 + self.damageconsistency
        variationdown = 1 - self.damageconsistency
        critchance = random.randrange(0, 100)
        if critchance in range(0, int(10 * self.critchanceincrease)):
            return random.randrange(int(self.critdamage * variationdown), int(self.critdamage * variationup))
        else:
            return random.randrange(int(self.damage * variationdown), int(self.damage * variationup))
    def printequipedweapon(self):
        if self.weapon != None:
            we.weaponprint(self.weapon)
    def printequipedhelmet(self):
        if self.helmet != None:
            ae.armorprint(self.helmet)
    def printequipedarms(self):
        if self.arms != None:
            ae.armorprint(self.arms)
    def printequipedchest(self):
        if self.chest != None:
            ae.armorprint(self.chest)
    def printequipedleggings(self):
        if self.leggings != None:
            ae.armorprint(self.leggings)
    def printequipedboots(self):
        if self.boots != None:
            ae.armorprint(self.boots)
    def getweaponinventory(self):
        for x in self.weaponinventory:
            we.weaponprint(x)
    def addweaponinventory(self, weapon):
        for w in weapon:
            self.weaponinventory.append(w)
    def getoneweaponinventory(self, number):
        if number in range(0, len(self.weaponinventory)):
            return self.weaponinventory[number]
    def gethelmetinventory(self):
        for x in self.helmetinventory:
            ae.armorprint(x)
    def addhelmetinventory(self, helmet):
        for w in helmet:
            self.helmetinventory.append(w)
    def getonehelmetinventory(self, number):
        if number in range(0, len(self.helmetinventory)):
            return self.helmentinventory[number]
    def getarmsinventory(self):
        for x in self.armsinventory:
            ae.armorprint(x)
    def addarmsinventory(self, arms):
        for w in arms:
            self.armsinventory.append(w)
    def getonearmsinventory(self, number):
        if number in range(0, len(self.armsinventory)):
            return self.armsinventory[number]
    def getchestinventory(self):
        for x in self.chestinventory:
            ae.armorprint(x)
    def addchestinventory(self, chest):
        for w in chest:
            self.chestinventory.append(w)
    def getonechestinventory(self, number):
        if number in range(0, len(self.chestinventory)):
            return self.chestinventory[number]
    def getleggingsinventory(self):
        for x in self.leggingsinventory:
            ae.armorprint(x)
    def addleggingsinventory(self, leggings):
        for w in leggings:
            self.leggingsinventory.append(w)
    def getoneleggingsinventory(self, number):
        if number in range(0, len(self.leggingsinventory)):
            return self.leggingsinventory[number]
    def getbootsinventory(self):
        for x in self.bootsinventory:
            ae.armorprint(x)
    def addbootsinventory(self, boots):
        for w in boots:
            self.bootsinventory.append(w)
    def getonebootsinventory(self, number):
        if number in range(0, len(self.bootsinventory)):
            return self.bootsinventory[number]
    def add_adrenaline(self, amount):
        if self.adrenaline + amount <= 100:
            self.adrenaline += amount
        else:
            self.adrenaline = 100
    def lose_adrenaline(self, amount):
        if self.adrenaline - amount >= 0:
            self.adrenaline -= amount
        else:
            self.adrenaline = 0
    def print_adrenaline(self):
        with output(output_type='dict') as output_lines:
            adrenaline = self.adrenaline
            output_lines['Adrenaline '] = "[{done}{padding}] {percent}%".format(
                done = d.color.RED + "#" * int(adrenaline/10) + d.color.END,
                padding = " " * (10 - int(adrenaline/10)),
                percent = adrenaline
                )
    def blockheal(self):
        heal_amount = random.randrange(self.level * 40, self.level * 60)
        print("{} blocks and heals for {} health!".format(self.name, d.color.RED + str(heal_amount) + d.color.END))
        self.addhealth(heal_amount)
    def tempprintallgear(self):
        self.printequipedweapon()
        self.printequipedhelmet()
        self.printequipedarms()
        self.printequipedchest()
        self.printequipedleggings()
        self.printequipedboots()
