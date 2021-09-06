posInit = 1


class Cleaner:
    def __init__(self, mapOBJ):
        self.cleaner = 3
        self.posX = None
        self.posY = None
        self.mapOBJ = mapOBJ
        self.setCleaner(posInit, posInit)

    def clear(self, posX, posY):
        map = self.mapOBJ.getMap()

        if (map[posX][posY] != 1):
            map[posX][posY] = 0

        self.mapOBJ.setMap(map)

    def setCleaner(self, posX, posY):
        map = self.mapOBJ.getMap()
        map[posX][posY] = self.cleaner
        self.setPosition(posX, posY)
        self.mapOBJ.setMap(map)

    def setPosition(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def getPosition(self):
        return (f'[{self.posX}][{self.posY}]')

    def cleaning(self):
        pass