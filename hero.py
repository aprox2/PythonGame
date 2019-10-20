import math as m
import random


class Hero:

    def __init__(self):
        self.health = 100
        self.stamina = 100
        self.level = 1
        self.items = {
            "Bomb": 1,
            "Healing Potion": 1,
            "Stamina Potion": 1
        }
        self.str = 10
        self.agl = 10
        self.int = 10
        self.exp = 0
        self.expLim = 100
        self.maxHealth = 100
        self.maxStamina = 100

    @property
    def exp_lim(self):
        x = self.level
        self.expLim = (m.fabs(x - 1 + 300 * 2 ** ((x - 1) / 4))) / 4

    @property
    def evade_chance(self):
        return 1.25/(1+m.exp(-(0.07 * self.agl - 2))) - 0.2

    @property
    def damage(self):
        return self.str + (self.agl * 0.2)

    def get_health(self):
        return self.health

    def set_exp(self, gotten_exp):
        self.exp += gotten_exp
        self.check_level()
        return

    def setExpLimn(self):
        x = self.level
        self.expLim = (m.fabs(x-1 + 300*2**((x-1)/4)))/4

    def check_level(self):
        checking = True
        while checking:
            if self.exp > self.expLim:
                self.exp -= self.expLim
                checking = self.lvl_up()
            else:
                return

    def lvl_up(self):
        choice = int(input("Congratulations choose an attribute to level up\n1.Strength\n2.Agility\n3.Intelligence\n"))
        if choice == 1:
            self.str += 1
            self.maxHealth += 20
        elif choice == 2:
            self.agl += 1
            self.maxStamina += 20
        else:
            self.int += 1
        self.health = self.maxHealth
        self.setExpLimn()
        if self.exp > self.expLim:
            return True
        else:
            return False

    def get_run_chance(self):
        return 1/(1.3 + m.exp(-(self.agl - 14))) + 0.1

    def heal(self, heal_amount):
        curr_health = self.health + heal_amount
        if curr_health > self.maxHealth:
            self.health = self.maxHealth
        else:
            self.health = curr_health

    def recover(self, recovery_amount):
        curr_recovery = self.stamina + recovery_amount
        if curr_recovery > self.maxStamina:
            self.stamina = self.maxStamina
        else:
            self.stamina = curr_recovery

    def check_if_item_exists(self, item):
        if self.items[item.name] >= 1:
            return True
        else:
            return False
