import pygame
import random
from classes import *

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

def getObstacles(gameDisplay, car, elapsedTime, lastHoleTime, holeObstacle, obstacles):
    # Time-based generation of new hole obstacle every 5 seconds
    if elapsedTime - lastHoleTime >= 1:
        try:
            holeObstacle = pygame.image.load('resources/hole.png')  # Load the obstacle image
            holeObstacle = pygame.transform.scale(holeObstacle, (80, 80))  # Resize it to fit the street
        except pygame.error as e:
            print(f"Failed to load hole image: {e}")
            return lastHoleTime  # Exit early if image loading fails

        holeSize = holeObstacle.get_rect()

        # Generate random x position for the hole within street bounds
        screenSize = gameDisplay.get_rect()
        x = random.randint(0, int(screenSize.width - holeSize.width))
        y = -holeSize.height  # Start the hole just above the screen, so it moves down into view

        # Add the new hole to the obstacles list
        obstacles.append(Obstacle(holeObstacle, x, y))

        # Reset the lastHoleTime to the current elapsedTime
        lastHoleTime = elapsedTime

    # Move the obstacles down and blit them on the screen
    for obstacle in obstacles[:]:
        obstacle.y += 5  # Move the hole down by 5 pixels per frame

        # Remove the hole if it goes off the screen
        if obstacle.y > gameDisplay.get_rect().height:
            obstacles.remove(obstacle)  # Remove obstacle if it moves out of screen
        else:
            # Update the obstacle's position in the list
            obstacles[obstacles.index(obstacle)] = obstacle
            
            # Blit the hole to the screen at its new position
            gameDisplay.blit(obstacle.image, (obstacle.x, obstacle.y))
        
        if checkCollision(car, obstacle):
            car.damage(10)
            print('you lost a life')

    return lastHoleTime

def checkCollision(car, obstacle):
    # Get the car's bounding rectangle
    carRect = pygame.Rect(car.x, car.y, car.image.get_width(), car.image.get_height())

    # Check for collision with each obstacle (hole) in the obstacles list
    holeRect = pygame.Rect(obstacle.x, obstacle.y, obstacle.image.get_width(), obstacle.image.get_height())

    # Check if the car's rect collides with the hole's rect
    if carRect.colliderect(holeRect):
        return True  # Collision occurred

    return False  # No collision

def main():
    gameDisplay, clock, crashed, car, pygame = initGame()
    streetOffset = 0  # Start with zero offset

    lastHoleTime = 0  # To track when the last hole was generated
    holeObstacle = None  # Placeholder for the hole image
    obstacles = []  # List to store active obstacles

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

        # Calculate elapsed time
        elapsedTime = pygame.time.get_ticks() / 1000  # Convert milliseconds to seconds

        # Draw everything
        loadStreet(gameDisplay, streetOffset)
        
        # Get and display obstacles
        lastHoleTime = getObstacles(gameDisplay, car, elapsedTime, lastHoleTime, holeObstacle, obstacles)
        
        drawCar(car, gameDisplay)

        # Update the display
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()