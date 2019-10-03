class Enemy:

    def __init__(self):
        self.health = -1
        self.armor = -1
        self.strength = -1
        self.expDrop = 0
        self.specialAttack = 0
        self.maxHealth = -1


    def attack(self):
        return self.strength

    def getHealth(self):
        return self.health

    def hit(self, recievedDamage):
        self.health-= recievedDamage*(100/(100+self.armor))


    def printStats(self):
        print("Stats")
        print(str(self.health) + "  " + str(self.armor) + "  " + str(self.strength))

    def checkAlive(self):
        if self.health <= 0:
            return False
        else:
            return True

    def heal(self, healAmount):
        currHealth = self.health + healAmount
        if currHealth > self.maxHealth:
            self.health = self.maxHealth
        else:
            self.health = currHealth
