from generateMap import Map
import pygame


def main(mapOBJ):
    pygame.init()
    map = mapOBJ.getMap()
    cleaner = 'images/cleaner.png'
    dirt = 'images/dirt.png'
    floor = 'images/floor.png'
    wall = 'images/wall.png'
    widthFrame = 100
    heightFrame = 100
    widthDisplay = len(mapOBJ.getMap()) * 100
    heightDisplay = len(mapOBJ.getMap()) * 100

    elements = {3: cleaner, 2: dirt, 1: wall, 0: floor}

    window = pygame.display.set_mode((widthDisplay, heightDisplay))
    icon = pygame.image.load('images/icon.png')

    pygame.display.set_caption("AAPA - Aspirador")
    pygame.display.set_icon(icon)

    quitGame = False

    while not quitGame:

        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame = True

        for i in range(0, len(map)):
            for j in range(0, len(map)):
                if (i == 0 and j == 0):
                    insert = pygame.image.load(elements[map[i][j]])
                    insert = pygame.transform.scale(insert,
                                                    (widthFrame, heightFrame))
                    window.blit(insert, (i, j))
                else:
                    insert = pygame.image.load(elements[map[i][j]])
                    insert = pygame.transform.scale(insert,
                                                    (widthFrame, heightFrame))
                    window.blit(insert, (i * 100, j * 100))

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    mapOBJ = Map()
    main(mapOBJ)