import pygame as p

class Number:

    def __init__(self,SCREEN,size, color, value, x, y):
        self.font = p.font.Font("assets/font/manaspc.ttf", size)
        self.SCREEN = SCREEN
        self.size = size
        self.value = value
        self.color = color
        self.x = x
        self.y = y
        self.draw()

    @property
    def label(self):
        return self.font.render(str(self.value), 1, self.color)

    def getValue(self):
        return str(self.value)


    def draw(self):
        self.SCREEN.blit(self.label, (self.x, self.y))

    def changeValue(self, value):
        self.value = value

    def changeColor(self, color):
        self.color = color