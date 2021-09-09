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

            position = cleanerOBJ.getPositionCleaner()
            window.blit(cleaner, (position[0], position[1]))
            pygame.display.update()


if __name__ == "__main__":
    mapOBJ = Map()
    cleanerOBJ = Cleaner(mapOBJ)
    main(mapOBJ, cleanerOBJ)
