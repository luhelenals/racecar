import pygame
from classes import Color, Car

# Initialize game window and car
def initGame():
    pygame.init()

    display_width = 800
    display_height = 600

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('RaceCar Game')
    clock = pygame.time.Clock()
    crashed = False

    carImg = pygame.image.load('resources/racecar.png')
    carImg = pygame.transform.scale(carImg, (carImg.get_rect().width * 0.06, carImg.get_rect().height * 0.06))
    x = (display_width - carImg.get_rect().width) / 2
    car = Car(x, display_height * 0.75, carImg)
    return gameDisplay, clock, crashed, car, pygame

# Draw car at given position
def drawCar(car, gameDisplay):
    gameDisplay.blit(car.image, (car.x, car.y))

# Draw street movement
def loadStreet(gameDisplay, streetOffset):
    gameDisplay.fill(Color.GREY.value)
    centerLine = pygame.Surface((15, 40))  # Width: 15, Height: 40
    centerLine.fill(Color.YELLOW.value)

    screenW = gameDisplay.get_rect().width
    lineW = centerLine.get_rect().width
    lineH = centerLine.get_rect().height
    screenH = gameDisplay.get_rect().height
    offset = 40  # Gap between each line
    
    # Calculate how many lines should be visible at once
    numLines = int(screenH / (lineH + offset)) + 1  # Extra lines for smooth wrap-around

    for i in range(numLines):
        # Calculate each line's position with streetOffset
        line_position = (i * (lineH + offset)) - streetOffset

        # Reset line position to the top once it's off the bottom
        if line_position >= screenH:
            line_position -= (screenH + lineH + offset)

        # Draw the center line at the calculated position
        gameDisplay.blit(centerLine, (int((screenW - lineW) / 2), line_position))

# Handle key pressing events for movement
def handleEvents(car, pygame):
    keys = pygame.key.get_pressed()  # Get the state of all keys
    if keys[pygame.K_RIGHT]:
        car.move_x = 5  # Move right
    elif keys[pygame.K_LEFT]:
        car.move_x = -5  # Move left
    else:
        car.move_x = 0  # Stop moving when no keys are pressed

    # Check for quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            return True

    return False

# Update car position, ensuring it stays within screen bounds
def updateCarPosition(car, screenW):
    car.x += car.move_x  # Update position based on movement
    # Ensure the car stays within screen boundaries
    if car.x < 0:
        car.x = 0
    elif car.x > screenW - car.image.get_rect().width:
        car.x = screenW - car.image.get_rect().width

def getObstacles(gameDisplay):
    #gameDisplay.blit
    return 0

def main():
    gameDisplay, clock, crashed, car, pygame = initGame()
    streetOffset = 0  # Start with zero offset

    # Main game loop
    while not crashed:
        crashed = handleEvents(car, pygame)

        # Update the car's position within the screen boundaries
        screenW = gameDisplay.get_rect().width
        updateCarPosition(car, screenW)

        # Move the street
        streetOffset -= 5  # Move the street lines up instead of down
        if streetOffset <= -80:  # line height + offset
            streetOffset = 0  # Reset to avoid overflow

        # Draw everything
        loadStreet(gameDisplay, streetOffset)
        getObstacles(gameDisplay)
        drawCar(car, gameDisplay)

        # Update the display
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
