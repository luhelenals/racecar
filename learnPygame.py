import sys
sys.path.append('C:/Users/Luiza.Lima/AppData/Local/Programs/Python/Python311-32/Lib/site-packages')

import pygame

pygame.init()

display_width = 400
display_height = 300

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('idk')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.4)
y = (display_height * 0.75)

while not crashed:
    keys=pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x += 1
            if event.key == pygame.K_LEFT:
                x -= 1
            if event.key == pygame.K_ESCAPE:
                crashed == True

    gameDisplay.fill(black)
    car(x,y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()