from enum import Enum

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

class Car:
    def __init__(self, x, y, image):
        """
        Initializes a Car instance.

        :param x: The x-coordinate of the car.
        :param y: The y-coordinate of the car.
        :param image: The image representing the car (can be a file path or URL).
        """
        self.x = x
        self.y = y
        self.image = image

    def moveX(self, delta_x):
        """
        Moves the car by delta_x and delta_y.

        :param delta_x: The change in the x-coordinate.
        :param delta_y: The change in the y-coordinate.
        """
        self.x += delta_x