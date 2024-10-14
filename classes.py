from enum import Enum
import pygame

class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    PINK = (255, 192, 203)
    GREY = (60, 60, 60)

class ObstacleType(Enum):
    HOLE = pygame.transform.scale(pygame.image.load('resources/hole.png'), (80, 80)) 
    CAR = pygame.image.load('resources/redCar.png')

class Car:
    def __init__(self, x, y, image):
        """
        Initializes a Car instance.

        :param x: The x-coordinate of the car.
        :param y: The y-coordinate of the car.
        :param image: The image representing the car (file path or URL).
        """
        self.x = x
        self.y = y
        self.image = image
        self.move_x = 0  # Movement direction: negative for left, positive for right, 0 for no movement
        self.health = 100
        self.nitro = False

    def move(self):
        """
        Moves the car by move_x.
        """
        self.x += self.move_x
    
    def damage(self, damage):
        self.health -= damage

class Obstacle:
    """
        Initializes a Obstacle instance.

        :param x: The x-coordinate of the car.
        :param y: The y-coordinate of the car.
        :param image: The image representing the car (file path or URL).
        """
    def __init__(self, image, x, y):
        self.x = x
        self.y = y
        self.image = image
        self.hit = False