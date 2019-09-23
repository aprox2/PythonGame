import item
import random

def chooseAction():
    while True:
        x = int(input("1. Attack\n2. Use item\n3. Run\n"))
        if x >= 1 and x <= 3:
            return x
        else:
            "Invalid Choice try again"



def chooseItem(hero):
    print("Choose an item")
    while True:
        print("1. Bomb Current = {}\n2. Healing Potion Current = {}\n3. Stamina Potion Current = {}\n".format(
                hero.items["Bomb"], hero.items["Healing Potion"], hero.items["Stamina Potion"]))
        x = int(input())
        if x == 1:
            return item.Bomb()
        elif x == 2:
            return item.HealingPotion()
        elif x == 3:
            return item.StaminaPotion()
        else:
            "Invalid Choice try again"


def parseChoice(hero, enemy, choice):
    if choice == 1:
        enemy.hit(hero.getDamage())
        return False
    elif choice == 2:
        while True:
            item = chooseItem(hero)
            if hero.checkIfItemExists(item):
                accept = input("Are you sure you want to use " + str(item.returnName()) + "\n")
                if accept == "y":
                    break
                else:
                    continue
            else:
                print("You don't have that item")
        useItem(hero, enemy, item)
        return False
    else:
        print("Trying to run")
        if runAway(hero):
            return True





def useItem(hero, enemy, item):
    itemAttributes = item.returnAttributes()
    enemy.hit(itemAttributes["Damage"])
    hero.heal(itemAttributes["Heal"])
    hero.recover(itemAttributes["Stamina"])

def runAway(hero):
    chanceNum = random.random()
    if chanceNum < hero.evadeChance:
        return True
    else:
        return False