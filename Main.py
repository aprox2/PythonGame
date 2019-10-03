from EnemyPackage.Enemies import *
from hero import Hero
from Arena import arena, subButtons, menu
import pygame as p
import render
from Common.number import Number

def pySetup():
    global SCREEN, CLOCK
    p.init()
    SCREEN = p.display.set_mode((1600, 900))
    CLOCK = p.time.Clock()

def main():

    print("Starting...")
    run = True
    blue = True
    hero = Hero()
    spider = Spider()
    button = subButtons.Attack()
    menuIMG = p.image.load("assets/menuBG.png")
    SCREEN.blit(menuIMG, (0, 520))
    renderScr = render.Render(SCREEN, hero, spider)

    while run:
        SCREEN.fill((0, 0, 0))
        renderScr.renderMenu()
        renderScr.checkHoover()
        renderScr.renderHealth(SCREEN)
        # Deal with events
        for e in p.event.get():
            if e.type == p.QUIT:
                run = False
            if e.type == p.MOUSEBUTTONUP:
                renderScr.checkClicked()
            if e.type == p.KEYDOWN and e.key == p.K_ESCAPE:
                run = False

        p.display.flip() #Updates display
        CLOCK.tick(60) #Framerate
        # Arena = arena.Arena(hero, spider)
        # Arena.Start(hero, spider)


if __name__ == "__main__":
    pySetup()
    main()
