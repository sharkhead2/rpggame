import random
import dictionary as d

class type:
   EPIC = '\033[95m' + '\033[1m'
   RARE = '\033[94m' + '\033[1m'
   UNCOMMON = '\033[92m' + '\033[1m'
   LEGENDARY = '\033[93m' + '\033[1m'
   COMMON = '\033[1m' + '\033[37m'
   END = '\033[0m'

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m' + '\033[37m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#Creation

def weaponmakedamage(level, type):
    if type == 'Common':
        x = random.randrange((level * 75), (level * 80))
    elif type == 'Uncommon':
        x = random.randrange((level * 78), (level * 83))
    elif type == 'Rare':
        x = random.randrange((level * 82), (level * 86))
    elif type == 'Epic':
        x = random.randrange((level * 86), (level * 90))
    elif type == 'Legendary':
        x = random.randrange((level * 89), (level * 96))
    else:
        x = 1
    return x

#make names
def weaponmakename():
    one = d.weapon1
    two = d.weapon2
    num1 = random.randrange(0, len(one))
    num2 = random.randrange(0, len(two))
    first = one[num1]
    second = two[num2]
    final = ''
    final += first
    final += ' '
    final += second
    return final

def swordmakename():
    one = d.weapon1
    two = d.sword
    num1 = random.randrange(0, len(one))
    num2 = random.randrange(0, len(two))
    first = one[num1]
    second = two[num2]
    final = ''
    final += first
    final += ' '
    final += second
    return final
def daggermakename():
    one = d.weapon1
    two = d.dagger
    num1 = random.randrange(0, len(one))
    num2 = random.randrange(0, len(two))
    first = one[num1]
    second = two[num2]
    final = ''
    final += first
    final += ' '
    final += second
    return final
def macemakename():
    one = d.weapon1
    two = d.mace
    num1 = random.randrange(0, len(one))
    num2 = random.randrange(0, len(two))
    first = one[num1]
    second = two[num2]
    final = ''
    final += first
    final += ' '
    final += second
    return final
def clubmakename():
    one = d.weapon1
    two = d.club
    num1 = random.randrange(0, len(one))
    num2 = random.randrange(0, len(two))
    first = one[num1]
    second = two[num2]
    final = ''
    final += first
    final += ' '
    final += second
    return final
def spearmakename():
    one = d.weapon1
    two = d.spear
    num1 = random.randrange(0, len(one))
    num2 = random.randrange(0, len(two))
    first = one[num1]
    second = two[num2]
    final = ''
    final += first
    final += ' '
    final += second
    return final
def fryingpanmakename():
    one = d.weapon1
    two = d.fryingpan
    num1 = random.randrange(0, len(one))
    num2 = random.randrange(0, len(two))
    first = one[num1]
    second = two[num2]
    final = ''
    final += first
    final += ' '
    final += second
    return final
def axemakename():
    one = d.weapon1
    two = d.axe
    num1 = random.randrange(0, len(one))
    num2 = random.randrange(0, len(two))
    first = one[num1]
    second = two[num2]
    final = ''
    final += first
    final += ' '
    final += second
    return final
def heavybluntmakename():
    one = d.weapon1
    two = d.heavyblunt
    num1 = random.randrange(0, len(one))
    num2 = random.randrange(0, len(two))
    first = one[num1]
    second = two[num2]
    final = ''
    final += first
    final += ' '
    final += second
    return final

def weaponmaketype():
    u = random.randrange(1,101)
    if u in range(1, 41):
        return 'Common'
    if u in range(41, 71):
        return 'Uncommon'
    if u in range(71, 91):
        return 'Rare'
    if u in range(91, 98):
        return 'Epic'
    if u in range(98, 101):
        return 'Legendary'

def weaponreturnbufftype(type):
    if type == 'Common':
        return None
    if type == 'Uncommon':
        return None
    if type == 'Rare':
        return 1
    if type == 'Epic':
        return 2
    if type == 'Legendary':
        return 2

def weaponperkamount():
    #Subject to change with finished player class
    j = random.randrange(5, 11)
    return str(j) + "% "

def weaponperkbase():
    f = random.randrange(0, len(d.perks))
    return d.perks[f]

def lenweaponperkamount():
    j = random.randrange(50, 80)
    return str(j) + "% "

def weaponmakeperks(type):
    final = []
    number = weaponreturnbufftype(type)
    if number == None:
        return None
    g = 1
    while g <= number:
        thing = ''
        g += 1
        thing += weaponperkamount()
        thing += weaponperkbase()
        final.append(thing)
    if type == 'Legendary':
        leng = ''
        leng += lenweaponperkamount()
        leng += weaponperkbase()
        final.append(leng)
    return final

#Inventory

def weaponprint(weapon):
    print color.BOLD + weapon.name + color.END
    if weapon.type == 'Legendary':
        print '     ' + type.LEGENDARY + weapon.type + type.END
    if weapon.type == 'Epic':
        print '     ' + type.EPIC + weapon.type + type.END
    if weapon.type == 'Rare':
        print '     ' + type.RARE + weapon.type + type.END
    if weapon.type == 'Uncommon':
        print '     ' + type.UNCOMMON + weapon.type + type.END
    if weapon.type == 'Common':
        print '     ' + type.COMMON + weapon.type + type.END
    print '     ' + color.BOLD + str(weapon.damage) + color.END + " damage"
    if weapon.perks != None:
        if weapon.perks.perks != None:
            for x in weapon.perks.perks:
                print "         " + x.get_string()
