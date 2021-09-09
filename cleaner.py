from random import randint, choice


class Cleaner:
    def __init__(self, mapOBJ, posX=None, posY=None):
        self.posXMap = posX
        self.posYMap = posY
        self.posXCleaner = posX
        self.posYCleaner = posY
        self.mapOBJ = mapOBJ
        if (self.posXMap == None):
            max = len(self.mapOBJ.getMap()) - 2
            x = randint(1, max)
            y = randint(1, max)
            self.setPositionMap(x, y)
            self.setPositionCleaner(x * 100, y * 100)

    def setPositionMap(self, posXMap, posYMap):
        self.posXMap = posXMap
        self.posYMap = posYMap

    def setPositionCleaner(self, posXCleaner, posYCleaner):
        self.posXCleaner = posXCleaner
        self.posYCleaner = posYCleaner

    def getPositionCleaner(self):
        return ([self.posXCleaner, self.posYCleaner])

    def getPositionMap(self):
        return ([self.posXMap, self.posYMap])

    def isWallOnFront(self):
        X = int(self.getPositionCleaner()[0] / 100)
        Y = int(self.getPositionCleaner()[1] / 100)
        position = [X, Y]

        if (self.mapOBJ.getMap()[position[0] + 1][position[1]] == 1):
            return True
        else:
            return False

    def isWallOnBack(self):
        X = int(self.getPositionCleaner()[0] / 100)
        Y = int(self.getPositionCleaner()[1] / 100)
        position = [X, Y]

        if (self.mapOBJ.getMap()[position[0] - 1][position[1]] == 1):
            return True
        else:
            return False

    def isWallOnUp(self):
        X = int(self.getPositionCleaner()[0] / 100)
        Y = int(self.getPositionCleaner()[1] / 100)
        position = [X, Y]

        if (self.mapOBJ.getMap()[position[0]][position[1] - 1] == 1):
            return True
        else:
            return False

    def isWallOnBottom(self):
        X = int(self.getPositionCleaner()[0] / 100)
        Y = int(self.getPositionCleaner()[1] / 100)
        position = [X, Y]

        if (self.mapOBJ.getMap()[position[0]][position[1] + 1] == 1):
            return True
        else:
            return False

    def simpleReactiveAgent(self, mapOBJ):
        map = mapOBJ.getMap()
        posXMap = int(self.getPositionCleaner()[0] / 100)
        posYMap = int(self.getPositionCleaner()[1] / 100)
        directions = ["abaixo", "acima", "direita", "esquerda"]

        if map[posXMap][posYMap] == 2:
            return "aspirar"
        else:
            if self.isWallOnFront():
                directions.remove("direita")
            elif map[posXMap + 1][posYMap] == 2:
                return "direita"
            if self.isWallOnBack():
                directions.remove("esquerda")
            elif map[posXMap - 1][posYMap] == 2:
                return "esquerda"
            if self.isWallOnBottom():
                directions.remove("abaixo")
            elif map[posXMap][posYMap + 1] == 2:
                return "abaixo"
            if self.isWallOnUp():
                directions.remove("acima")
            elif map[posXMap][posYMap - 1] == 2:
                return "acima"

            if (mapOBJ.checkTheDirt()):
                return choice(directions)
            else:
                return "NoOp"

    def objectiveAgent(self, perception, mapOBJ):
        posXCleaner = self.getPositionCleaner()[0]
        posYCleaner = self.getPositionCleaner()[1]
        posXRemove = int(self.getPositionCleaner()[0] / 100)
        posYRemove = int(self.getPositionCleaner()[1] / 100)

        print(f"Ação: '{perception}'")
        if perception == "direita":
            self.setPositionCleaner(posXCleaner + 100, posYCleaner)
        elif perception == "esquerda":
            self.setPositionCleaner(posXCleaner - 100, posYCleaner)
        elif perception == "acima":
            self.setPositionCleaner(posXCleaner, posYCleaner - 100)
        elif perception == "abaixo":
            self.setPositionCleaner(posXCleaner, posYCleaner + 100)
        elif perception == "aspirar":
            mapOBJ.clear(posXRemove, posYRemove)
        elif perception == "NoOp":
            return