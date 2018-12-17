"""
This is the dev version for the fighting mechanics in this game.
THis is the main file which should be run inside terminal through
python 2.7. All of the modules being used in this game should be
                already installed with python 2.
"""

import fight as fi
import classes as c
import time
import functions as f

def dev_build_fight():
    menu = """
                  Welcome to the dev build for the fighting mechanics!
        Please remember there will be numerous glitches and bugs in this version
    """
    time.sleep(0.5)
    print(menu)
    f.takeallinput()
    player = c.Person(raw_input("Name? "))
    helmet1 = c.Helmet.helmet_gen(1)
    chest1 = c.Chest.chest_gen(1)
    arms1 = c.Arms.arms_gen(1)
    leggings1 = c.Leggings.leggings_gen(1)
    boots1 = c.Boots.boots_gen(1)
    player.equip_helmet(helmet1)
    player.equip_arms(arms1)
    player.equip_chest(chest1)
    player.equip_leggings(leggings1)
    player.equip_boots(boots1)
    player.gethelmetinventory()
    player.getarmsinventory()
    player.getchestinventory()
    player.getleggingsinventory()
    player.getbootsinventory()
    loot = c.Sword.sword_gen(1)
    player.equip_weapon(loot)
    player.getweaponinventory()

    fi.mercenary_fight(player, 1)

dev_build_fight()
