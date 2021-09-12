from random import randint


class Cleaner:
    def __init__(self, mapOBJ, posX=None, posY=None):
        self.posXCleaner = posX
        self.posYCleaner = posY
        self.mapOBJ = mapOBJ
        if (self.posXCleaner == None):
            max = len(self.mapOBJ.getMap()) - 2
            x = randint(1, max)
            y = randint(1, max)
            self.setPositionCleaner(x * 100, y * 100)

    def setPositionCleaner(self, posXCleaner, posYCleaner):
        self.posXCleaner = posXCleaner
        self.posYCleaner = posYCleaner

    def getPositionCleaner(self):
        return ([self.posXCleaner, self.posYCleaner])

    def isWallOnRight(self):
        X = int(self.getPositionCleaner()[0] / 100)
        Y = int(self.getPositionCleaner()[1] / 100)
        position = [X, Y]

        if (self.mapOBJ.getMap()[position[0] + 1][position[1]] == 1):
            return True
        else:
            return False

    def isWallOnLeft(self):
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
        dirtF = mapOBJ.getDirt().copy()

        if (len(dirtF) >= 1):
            dirtF = dirtF.popleft()

        if map[posXMap][posYMap] == 2:
            mapOBJ.getDirt().remove([posXMap, posYMap])
            return 'aspirar'

        else:
            if (len(dirtF) >= 1):
                if self.isWallOnBottom():
                    pass
                elif ((posXMap == dirtF[0]) and (posYMap < dirtF[1])):
                    return 'abaixo'

                if self.isWallOnRight():
                    pass
                elif ((posXMap != dirtF[0])):
                    return 'direita'

                if self.isWallOnUp():
                    pass
                elif ((posXMap == dirtF[0]) and (posYMap > dirtF[1])):
                    return 'acima'
            else:
                return 'NoOp'

    def objectiveAgent(self, perception, mapOBJ):
        posXCleaner = self.getPositionCleaner()[0]
        posYCleaner = self.getPositionCleaner()[1]
        posXRemove = int(self.getPositionCleaner()[0] / 100)
        posYRemove = int(self.getPositionCleaner()[1] / 100)

        print(f'Ação: "{perception}"')
        if perception == 'direita':
            self.setPositionCleaner(posXCleaner + 100, posYCleaner)
        elif perception == 'esquerda':
            self.setPositionCleaner(posXCleaner - 100, posYCleaner)
        elif perception == 'acima':
            self.setPositionCleaner(posXCleaner, posYCleaner - 100)
        elif perception == 'abaixo':
            self.setPositionCleaner(posXCleaner, posYCleaner + 100)
        elif perception == 'aspirar':
            mapOBJ.clear(posXRemove, posYRemove)
        elif perception == 'NoOp':
            print('FIM')
            return 'NoOp'