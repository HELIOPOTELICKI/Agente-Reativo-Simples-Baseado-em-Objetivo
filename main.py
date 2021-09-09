from map import Map
from cleaner import Cleaner
import pygame


def main(mapOBJ, cleanerOBJ):
    pygame.init()

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

    def generateDirtyMap():
        map = mapOBJ.getMap()

        for i in range(0, len(map)):
            for j in range(0, len(map)):
                if (map[i][j] == 2):
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
    elements = {3: cleanerImg, 2: dirtImg, 1: wallImg, 0: floorImg}
    imageRes = 100
    delayDisplay = 500
    widthFrame = 100
    heightFrame = 100
    widthDisplay = len(mapOBJ.getMap()) * 100
    heightDisplay = len(mapOBJ.getMap()) * 100
    counter = 0
    printPoints = True
    window = pygame.display.set_mode((widthDisplay, heightDisplay))
    icon = pygame.image.load('images/icon.png')

    pygame.display.set_caption("AAPA - Aspirador")
    pygame.display.set_icon(icon)

    quitGame = False

    generateMap()

    mapOBJ.dirtyingFloor()

    generateDirtyMap()

    cleaner = pygame.image.load(elements[3])
    cleaner = pygame.transform.scale(cleaner, (widthFrame, heightFrame))
    position = cleanerOBJ.getPositionCleaner()

    window.blit(cleaner, (position[0], position[1]))
    pygame.display.update()

    while not quitGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame = True

        while mapOBJ.checkTheDirt():
            pygame.time.delay(delayDisplay)
            generateMap()
            generateDirtyMap()
            perception = cleanerOBJ.simpleReactiveAgent(mapOBJ)
            cleanerOBJ.objectiveAgent(perception, mapOBJ)
            counter += 1
            position = cleanerOBJ.getPositionCleaner()
            window.blit(cleaner, (position[0], position[1]))
            pygame.display.update()

        generateMap()
        position = cleanerOBJ.getPositionCleaner()
        window.blit(cleaner, (position[0], position[1]))
        RED = (255, 0, 0)
        pygame.display.update()

        if (printPoints):
            print(f'Pontos --> {counter}')
            pygame.draw.rect(window, RED, [55, 500, 10, 5], 0)
            printPoints = False


if __name__ == "__main__":
    # Caso queira alterar para um mapa 6x6, basta passalo como argumento em Map()
    map = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]]

    mapOBJ = Map()
    cleanerOBJ = Cleaner(mapOBJ)
    main(mapOBJ, cleanerOBJ)
