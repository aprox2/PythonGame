from Arena.subButtons import *


class Menu:

    def __init__(self):
        self.background = p.image.load("assets/menuBG.png")
        self.name = "Attack"
        self.xPos = 0
        self.yPos = 520

    def getPos(self):
        return self.xPos, self.yPos

    def getIMG(self):
        return self.background