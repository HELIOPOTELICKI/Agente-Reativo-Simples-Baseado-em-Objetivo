from map import Map
from cleaner import Cleaner
import pygame


def main(mapOBJ, cleanerOBJ):
    def generateMap():
        pygame.time.delay(delayDisplay)

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

    pygame.init()

    dirt = 'images/dirt.png'
    floor = 'images/floor.png'
    wall = 'images/wall.png'
    imageRes = 100
    delayDisplay = 500
    widthFrame = 100
    heightFrame = 100
    widthDisplay = len(mapOBJ.getMap()) * 100
    heightDisplay = len(mapOBJ.getMap()) * 100

    elements = {2: dirt, 1: wall, 0: floor}

    window = pygame.display.set_mode((widthDisplay, heightDisplay))
    icon = pygame.image.load('images/icon.png')

    pygame.display.set_caption("AAPA - Aspirador")
    pygame.display.set_icon(icon)

    quitGame = False

    map = mapOBJ.getMap()
    generateMap()
    mapOBJ.dirtyingFloor()

    while not quitGame:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame = True

    pygame.quit()


if __name__ == "__main__":
    mapOBJ = Map()
    cleanerOBJ = Cleaner(mapOBJ)
    main(mapOBJ, cleanerOBJ)
