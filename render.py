import Main
import pygame as p
from Arena.menu import Menu
from Arena.subButtons import *

class Render:

    def __init__(self, SCREEN):
        self.SCREEN = SCREEN
        self.menuObj = Menu()
        self.buttonObjs = [Attack(), UseItem(), Run()]

    def renderMenu(self):
        self.SCREEN.blit(self.menuObj.getIMG(), self.menuObj.getPos())
        for buttons in self.buttonObjs:
            self.SCREEN.blit(buttons.getNotPressed(), buttons.getPos())

    def checkHoover(self):
        mousePOS = p.mouse.get_pos()
        for button in self.buttonObjs:
            if button.getX() + 300 > mousePOS[0] > button.getX() and button.getY() + 100 >\
                    mousePOS[1] > button.getY():
                self.SCREEN.blit(button.getPressed(), button.getPos())
            else:
                self.SCREEN.blit(button.getNotPressed(), button.getPos())