import random
import logic


class Arena:

    def __init__(self):
        self.currentProgress = {
            "Victor" : 0,
            "Turn" : None,
            "moreTurns": 0
        }


    def Start(self, hero, enemy):
        # turn = bool(random.getrandbits(1))
        self.currentProgress["Turn"] = True
        if self.currentProgress["Turn"]:print("Hero goes first")
        else : print("Enemy goes first")

        fight = True
        while fight:
            if self.currentProgress["Turn"]:
                print(enemy.health)
                choice = logic.chooseAction()
                print(enemy.health)
                logic.parseChoice(hero, enemy, choice)
                print(enemy.health)
                if self.currentProgress["moreTurns"] <= 0:
                    self.switchTurn()
                else:
                    print(enemy.health)
                    continue
            else:
                x=2



    def switchTurn(self):
        if self.currentProgress["Turn"]:
            self.currentProgress["Turn"] = False
        else:
            self.currentProgress["Turn"] = True
