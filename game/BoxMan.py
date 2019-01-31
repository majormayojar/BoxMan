import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode([1024,768])
keep_going = True
pygame.display.set_caption("BoxMan")


redpad = pygame.image.load("redpad.bmp")
lvl1 = pygame.image.load("lvl1.bmp")
lvl2 = pygame.image.load("lvl2.bmp")
character = pygame.image.load("character.bmp")
pygame.display.set_icon(character)

a = 0
b = 549
c = 0

WHITE = (255,255,255)
BLACK = (0,0,0)

x = 1024
y = 768


while keep_going:
    screen.blit(lvl1, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.blit(character,(a,549))
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            a += 10
            b += 10
            c +=10
            if c >= 810:
                if a == 810:
                    a = a - a
                screen.blit(lvl2,(0,0))
                screen.blit(character,(a,549))
                pygame.display.update()
                if a == 467:
                    a = a - a
                    screen.blit(character,(a,549))
                    pygame.display.update()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                a = a - a
                c = c - c
                screen.blit(character,(a,549))
                pygame.display.update()


    
pygame.quit()
