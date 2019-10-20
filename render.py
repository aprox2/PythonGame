import Main
import pygame as p
from Arena.menu import Menu
from Arena.subButtons import *
from Common.number import Number
import actions

class Render:

    def __init__(self, SCREEN, hero, enemy):
        self.SCREEN = SCREEN
        self.menuObj = Menu()
        self.buttonObjs = [Attack(), UseItem(), Run()]
        self.currentButt = None
        self.hero = hero
        self.enemy = enemy


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
                self.currentButt = button
                break
            else:
                self.SCREEN.blit(button.getNotPressed(), button.getPos())
        else:
            self.currentButt = None

    def checkClicked(self):
        mousePOS = p.mouse.get_pos()
        if self.currentButt != None:
            if self.currentButt.getName() == "Attack":
                actions.attack(self.hero, self.enemy, True)


    def renderHealth(self,SCREEN):
        heroHP = Number(SCREEN, 40, (255, 255, 255), self.hero.get_health(), 300, 300)
        enemyHP = Number(SCREEN, 40, (255, 255, 255), self.enemy.getHealth(), 600, 300)
        values = (heroHP, enemyHP)              #Uzmanigi, varētu nemainities, jo tuple
        for hps in values:
            hps.draw()
