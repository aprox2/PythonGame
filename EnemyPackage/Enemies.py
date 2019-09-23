from EnemyClass import Enemy

class Bat(Enemy):


    def __init__(self):
        super().__init__()
        self.health = 20
        self.armor = 3
        self.strength = 4
        self.maxHealth = 20
        self.expDrop = 10

class Spider(Enemy):

    def __init__(self):
        super().__init__()
        self.health = 60
        self.armor = 2
        self.strength = 6
        self.maxHealth = 60
        self.expDrop = 50

    def special(self):
        print("The spider is healing")
        self.health+=20


class Skeleton(Enemy):

    def __init__(self):
        super().__init__()
        self.health = 130
        self.armor = 10
        self.strength = 20
        self.maxHealth = 130
        self.expDrop = 125

    def special(self):
        print("The skeleton has double damage now")
        self.strength*=2

    # def specialAttack(self):
    #     return 1