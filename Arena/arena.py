import random
import logic


class Arena:

    def __init__(self, hero, enemy):
        self.currentProgress = {
            "Victor" : None,
            "Turn" : None,
            "moreTurns": 0,
            "RanAway": False
        }
        self.Hero = hero
        self.Enemy = enemy

    def Start(self, enemy):
        # turn = bool(random.getrandbits(1))
        self.currentProgress["Turn"] = True
        if self.currentProgress["Turn"]:print("Hero goes first")
        else : print("Enemy goes first")
        fight = True
        while fight:
            if self.currentProgress["Turn"]:
                choice = logic.chooseAction()
                result = logic.parseChoice(self.Hero, self.Enemy, choice)
                if result:
                    self.currentProgress["RanAway"] = True
            else:
                x=2
            fight = self.nextTurn()

    def nextTurn(self):
        if not self.Enemy.checkAlive():
            self.currentProgress["Victor"] = True
        if self.Hero.health <= 0:
            self.currentProgress["Victor"] = False
        if self.currentProgress["moreTurns"] <= 0:
            self.switchTurn()
        else:
            self.currentProgress["moreTurns"]-=1
        if self.currentProgress["RanAway"]:
            return False
        elif not self.currentProgress["Victor"] == None:
            return False
        else:
            return True

    def switchTurn(self):
        if self.currentProgress["Turn"]:
            self.currentProgress["Turn"] = False
        else:
            self.currentProgress["Turn"] = True
