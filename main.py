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
    car = Car(display_width * 0.4, display_height * 0.75, carImg)
    return gameDisplay, clock, crashed, car, pygame

# Draw car at given position
def drawCar(car, gameDisplay):
    gameDisplay.blit(car.image, (car.x, car.y))


# Handle key pressing events for movement
def handleEvents(car, pygame, crashed):
    keys=pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                car.moveX(1)
            if event.key == pygame.K_LEFT:
                car.moveX(-1)
            if event.key == pygame.K_ESCAPE:
                return True
    return crashed

def main():
    gameDisplay, clock, crashed, car, pygame = initGame()

    # Main game loop
    while not crashed:
        crashed = handleEvents(car, pygame, crashed)

        gameDisplay.fill(Color.GREY.value)
        drawCar(car, gameDisplay)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()