'''
    Atividade Avaliativa: Agentes Inteligentes
    Grupo: Hélio Potelicki, Luis Felipe Zaguini e Pedro Henrique Roweder

'''

from cleaner import Cleaner
from map import Map
import pygame


def main(mapOBJ, cleanerOBJ):
    pygame.init()
    pygame.font.init()

    def generateMap():
        map = mapOBJ.getMap()

        for i in range(0, len(map)):
            for j in range(0, len(map)):
                insert = pygame.image.load(elements[map[i][j]])
                insert = pygame.transform.scale(insert,
                                                (widthFrame, heightFrame))
                if (i == 0 and j == 0):
                    window.blit(insert, (i, j))
                else:
                    window.blit(insert, (i * imageRes, j * imageRes))

        pygame.display.update()

    cleanerImg = 'images/cleaner.png'
    dirtImg = 'images/dirt.png'
    floorImg = 'images/floor.png'
    wallImg = 'images/wall.png'
    pointsImg = 'images/points.png'
    iconImg = 'images/icon.png'
    elements = {
        5: iconImg,
        4: pointsImg,
        3: cleanerImg,
        2: dirtImg,
        1: wallImg,
        0: floorImg
    }

    imageRes = 100
    delayDisplay = 500
    widthFrame = 100
    heightFrame = 100
    widthDisplay = len(mapOBJ.getMap()) * 100
    heightDisplay = len(mapOBJ.getMap()) * 100
    counter = 0
    printPoints = True
    finished = True
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    fontColor = (0, 0, 0)
    window = pygame.display.set_mode((widthDisplay, heightDisplay))

    icon = pygame.image.load(elements[5])
    pygame.display.set_caption('AAPA - Aspirador')
    pygame.display.set_icon(icon)

    quitGame = False
    stopCleaning = False

    generateMap()
    mapOBJ.dirtyingFloor()

    cleaner = pygame.image.load(elements[3])
    cleaner = pygame.transform.scale(cleaner, (widthFrame, heightFrame))
    points = pygame.image.load(elements[4])
    points = pygame.transform.scale(points, (widthFrame, heightFrame))

    position = cleanerOBJ.getPositionCleaner()

    window.blit(cleaner, (position[0], position[1]))
    pygame.display.update()

    while not quitGame:
        while not quitGame and not stopCleaning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitGame = True

            pygame.time.delay(delayDisplay)
            generateMap()

            perception = cleanerOBJ.simpleReactiveAgent(mapOBJ)
            resp = cleanerOBJ.objectiveAgent(perception, mapOBJ)
            counter += 1
            position = cleanerOBJ.getPositionCleaner()
            window.blit(cleaner, (position[0], position[1]))

            if (resp == 'NoOp'):
                stopCleaning = True

            pygame.display.update()

        if (finished):
            generateMap()
            finished = False

        position = cleanerOBJ.getPositionCleaner()
        window.blit(cleaner, (position[0], position[1]))
        pygame.display.update()

        if (printPoints):
            window.blit(points, (position[0] + 60, position[1] - 50))
            textsurface = myfont.render('Pontos', False, (fontColor))
            textpoints = myfont.render(f'{counter-1}', False, (fontColor))
            window.blit(textsurface, (position[0] + 80, position[1] - 40))
            window.blit(textpoints, (position[0] + 95, position[1] - 20))
            print(f'Pontos -> {counter-1}')
            printPoints = False

        pygame.display.update()


if __name__ == '__main__':
    # Caso queira alterar o mapa, basta passar map como argumento em Map()
    # mapa 6x6
    map1 = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]]

    # mapa 4x4
    map2 = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]]

    mapOBJ = Map()
    cleanerOBJ = Cleaner(mapOBJ, 100, 100)
    main(mapOBJ, cleanerOBJ)