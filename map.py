'''
    Atividade Avaliativa: Agentes Inteligentes
    Grupo: Hélio Potelicki, Luis Felipe Zaguini e Pedro Henrique Roweder

'''

from collections import deque
from random import choice

defaultCleanMap = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1]]


class Map:
    def __init__(self, mapArg=defaultCleanMap):
        self.map = None
        self.dirt = deque()
        if (len(mapArg) < 4):
            print('Mapa deve ter no mínimo tamanho 4x4, usando mapa padrão')
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
            self.map = defaultCleanMap
            print('A matriz informada não é quadrada, usando mapa padrão')

    def dirtyingFloor(self):
        dirtyMap = self.getMap()

        for i in range(0, len(dirtyMap)):
            for j in range(0, len(dirtyMap)):
                if dirtyMap[i][j] == 0:
                    dirtyMap[i][j] = choice([0, 2])

        self.setDirt()
        self.setMap(dirtyMap)

    def checkTheDirt(self):
        map = self.getMap()
        for i in range(0, len(map)):
            if (2 in map[i]):
                return True

        return False

    def clear(self, posX, posY):
        map = self.getMap()

        if (map[posX][posY] != 1):
            map[posX][posY] = 0

        self.setMap(map)

    def getDirt(self):
        return self.dirt

    def setDirt(self):
        map = self.getMap()
        for i in range(0, len(map)):
            for j in range(0, len(map)):
                if (map[i][j] == 2):
                    self.dirt.append([i, j])