from EnemyPackage.Enemies import *
from hero import Hero
import arena

def main():
    print("Starting...")
    run = True
    hero = Hero()
    spider = Spider()
    while run:
        Arena = arena.Arena(hero, spider)
        Arena.Start(hero, spider)
        break

if __name__ == "__main__":
    main()