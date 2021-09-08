from random import randint


class Cleaner:
    def __init__(self, mapOBJ, posX=None, posY=None):
        self.posX = posX
        self.posY = posY
        self.mapOBJ = mapOBJ
        if (self.posX == None):
            max = len(self.mapOBJ.getMap()) - 2
            x = randint(1, max)
            y = randint(1, max)
            self.setCleaner(x, y)

    def clear(self, posX, posY):
        map = self.mapOBJ.getMap()

        if (map[posX][posY] != 1):
            map[posX][posY] = 0

        self.mapOBJ.setMap(map)

    def setCleaner(self, posX, posY):
        position = self.getPosition()
        if (not self.posX == None):
            self.clear(position[0], position[1])
        self.setPosition(posX, posY)

    def setPosition(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def getPosition(self):
        return ([self.posX, self.posY])

    def isWallOnFront(self):
        position = self.getPosition()

        if (self.mapOBJ.getMap()[position[0] + 1][position[1]] == 1):
            return True
        else:
            return False

    def isWallOnBack(self):
        position = self.getPosition()

        if (self.mapOBJ.getMap()[position[0] - 1][position[1]] == 1):
            return True
        else:
            return False

    def isWallOnUp(self):
        position = self.getPosition()

        if (self.mapOBJ.getMap()[position[0]][position[1] - 1] == 1):
            return True
        else:
            return False

    def isWallOnBottom(self):
        position = self.getPosition()

        if (self.mapOBJ.getMap()[position[0]][position[1] + 1] == 1):
            return True
        else:
            return False
