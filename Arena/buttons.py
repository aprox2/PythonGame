import pygame as p


class Buttons:
    def __init__(self):
        self.name = "Fallback"
        self.fallBack = "assets/errorIMG.png"
        self.buttDOWN = None
        self.buttUP = None
        self.xPos = -1
        self.yPos = -1

    def getName(self):
        return self.name

    def getNotPressed(self):
        if self.buttUP == None:
            return p.image.load(self.fallBack)
        else:
            return self.buttUP

    def getPressed(self):
        if self.buttDOWN == None:
            return p.image.load(self.fallBack)
        else:
            return self.buttDOWN

    def getPos(self):
        if self.xPos == -1 or self.yPos == -1:
            print("image is outside the screen, image name == \"{}\"".format(self.name))
            return [-1, -1]
        else:
            return self.xPos, self.yPos

    def getX(self):
        return int(self.xPos)

    def getY(self):
        return int(self.yPos)