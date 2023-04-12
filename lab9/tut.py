import pygame, sys, random
from pygame.locals import *
pygame.init()
white = (255, 255, 255)
FPS = 60
fpsClock = pygame.time.Clock()
We = 600
HE = 800
WINDOW = pygame.display.set_mode((We, HE))
pygame.display.set_caption("My Game!")
def main():
    a = True
    while a:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        WINDOW.fill(white)
        pygame.display.update()
        fpsClock.tick(FPS)
main()
