from hero import Hero


class Item:

    def __init__(self):
        self.attributes = {
            "Damage": 0,
            "Heal": 0,
            "Stamina": 0
        }
        self.name = ""

    def returnName(self):
        return self.name

    def returnAttributes(self):
        return self.attributes

class Bomb(Item):

    def __init__(self):
        super().__init__()
        self.name = "Bomb"
        self.attributes["Damage"] = 50



class HealingPotion(Item):

    def __init__(self):
        super().__init__()
        self.name = "Healing Potion"
        self.attributes["Heal"] = 50


class StaminaPotion(Item):

    def __init__(self):
        super().__init__()
        self.name = "Stamina Potion"
        self.attributes["Stamina"] = 50

