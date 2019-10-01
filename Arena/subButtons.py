from Arena.buttons import Buttons
import pygame as p


class Attack(Buttons):
    def __init__(self):
        super().__init__()
        self.name = "Attack"
        self.buttDOWN = p.image.load("assets/attackDOWN.png")
        self.buttUP = p.image.load("assets/attackUP.png")
        self.xPos = 27
        self.yPos = 538


class UseItem(Buttons):
    def __init__(self):
        super().__init__()
        self.name = "UseItem"
        self.buttDOWN = p.image.load("assets/InventoryDOWN.png")
        self.buttUP = p.image.load("assets/InventoryUP.png")
        self.xPos = 27
        self.yPos = 660


class Run(Buttons):
    def __init__(self):
        super().__init__()
        self.name = "Run"
        self.buttDOWN = p.image.load("assets/runDOWN.png")
        self.buttUP = p.image.load("assets/runUP.png")
        self.xPos = 27
        self.yPos = 779
