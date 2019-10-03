import item


def attack(hero, enemy, heroTriggered):
    if heroTriggered:
        enemy.hit(hero.getDamage())
    else:
        x=1



def heal(hero, enemy, heroTriggered, ammount):
    if heroTriggered:
        hero.heal(ammount)
    else:
        enemy.heal(ammount)

def recover(hero, enemy, ammount):
    hero.recover(ammount)


def useItem( hero, enemy):
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
    itemAttributes = item.returnAttributes()
    for elements in itemAttributes:
        if elements == "Damage":
            attack(hero, enemy, True)
        if elements == "Heal":
            heal(hero, enemy, True)
def tryRun():
    x=3

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
