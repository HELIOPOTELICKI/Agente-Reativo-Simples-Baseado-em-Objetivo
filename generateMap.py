import random

defaultCleanMap = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1]]


class Map:
    def __init__(self, mapArg=defaultCleanMap):
        self.map = None
        if (len(mapArg) < 2):
            print('Mapa deve ter no mínimo tamanho 2x2, usando mapa padrão')
            mapArg = defaultCleanMap
        self.setMap(mapArg)

    def getMap(self):
        return self.map

    def setMap(self, map):
        length = 0
        for i in range(0, len(map)):
            length += len(map[i])

        if (len(map) == (length / len(map))):
            self.map = map
        else:
            print('A matriz informada não é quadrada')

    def setMapCoo(self, value, posX, posY):
        map = self.getMap()
        map[posX][posY] = value
        self.setMap(map)

    def dirtyingFloor(self):
        dirtyMap = self.getMap()

        for i in range(0, len(dirtyMap)):
            for j in range(0, len(dirtyMap)):
                if dirtyMap[i][j] == 0:
                    dirtyMap[i][j] = random.choice([0, 2])

        self.setMap(dirtyMap)