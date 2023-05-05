import pygame, sys, math, random
from Ball import*

size=[900,700]
screen=pygame.display.set_mode(size)
clock = pygame.time.Clock();

ball=Ball([4,4], [450,350])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    ball.move()
    ball.wallcollide(size)
            
    screen.fill([0,0,0])
    screen.blit(ball.image,ball.rect)
    pygame.display.flip()
    clock.tick(60)
