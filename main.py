# Resolving import issues
import sys
from path import path
sys.path.append(path)

import pygame
from classes import Color, Car

# Initialize game window and car
def initGame():
    pygame.init()

    display_width = 400
    display_height = 300

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('RaceCar Game')
    clock = pygame.time.Clock()
    crashed = False

    carImg = pygame.image.load('resources/racecar.png')
    car = Car(display_width * 0.5, display_height * 0.75, carImg)
    return gameDisplay, clock, crashed, car, pygame

# Draw car at given position
def drawCar(car, gameDisplay):
    gameDisplay.blit(car.image, (car.x, car.y))

# Draw street movement
def loadStreet(gameDisplay, streetOffset):
    gameDisplay.fill(Color.GREY.value)
    centerLine = pygame.Surface((15, 40))
    centerLine.fill(Color.YELLOW.value)

    screenW = gameDisplay.get_rect().width
    lineW = centerLine.get_rect().width
    lineH = centerLine.get_rect().height
    screenH = gameDisplay.get_rect().height
    offset = 40
    numLines = int(screenH/(lineH + offset))

    for i in range(1, numLines + 1):
        line_position = int(screenH - (i * (streetOffset + lineH)))
        gameDisplay.blit(centerLine, (int((screenW - lineW) / 2), line_position))

# Handle key pressing events for movement
def handleEvents(car, pygame, crashed):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                car.move_x = 1.5  # Start moving right
            if event.key == pygame.K_LEFT:
                car.move_x = -1.5  # Start moving left
            if event.key == pygame.K_ESCAPE:
                return True

        if event.type == pygame.KEYUP and (event.key in [pygame.K_RIGHT, pygame.K_LEFT]):
                car.move_x = 0  # Stop moving when key is released
            
    return crashed

def main():
    gameDisplay, clock, crashed, car, pygame = initGame()
    streetOffset = gameDisplay.get_rect().height + 1

    # Main game loop
    while not crashed:
        crashed = handleEvents(car, pygame, crashed)

        car.move()

        streetOffset -= 5
        
        loadStreet(gameDisplay, streetOffset)

        drawCar(car, gameDisplay)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()