#Importing stuff
import pygame
from pygame.locals import *
import time

#Initializing pygame and the game
pygame.init()
screen = pygame.display.set_mode([1024,768])
keep_going = True
pygame.display.set_caption("BoxMan")

#Loading Images
lvl1 = pygame.image.load("lvl1.png")
lvl2 = pygame.image.load("lvl2.png")
lvl3 = pygame.image.load("lvl3.png")
character = pygame.image.load("character.png")

pygame.display.set_icon(character)

#Variables
a = 0
b = 549
c = 0

WHITE = (255,255,255)
BLACK = (0,0,0)

x = 1024
y = 768

#Game Loop
while keep_going:
    screen.blit(lvl1, (0,0))
    screen.blit(character,(a,b))
    if c >= 810:
        if a >= 810:
            a = a - a
        screen.blit(lvl2,(0,0))
        screen.blit(character,(a,b))
        pygame.display.update()
        if a == 470:
            if b == 549:
                c = 810
                a = a - a  
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.blit(character,(a,549))
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(lvl1, (0,0))
            a += 10
            c +=10
            if c >= 810:
                if a >= 810:
                    a = a - a
                screen.blit(lvl2,(0,0))
                screen.blit(character,(a,b))
                pygame.display.update()
                if a == 470:
                    if b == 549:
                        c = 810
                        a = a - a
                        pygame.display.update()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                a = a - a
                c = c - c
                screen.blit(character,(a,b))
                pygame.display.update()
            if event.key == pygame.K_SPACE:
                b += 40
                screen.blit(character,(a,b))
                pygame.display.update()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               b -= 40
               screen.blit(character,(a,b))
               pygame.display.update()
            if event.key == pygame.K_LSHIFT:
                if c >= 810:
                    if a >= 810:
                        a = a - a
                    screen.blit(lvl2,(0,0))
                    screen.blit(character,(a,b))
                    pygame.display.update()
                if a == 470:
                    a = a - a
                    c = 810
                    pygame.display.update()
                a += 27
                if a >= 810:
                    a = a - a
                    pygame.display.update()

#Uninitializing pygame    
pygame.quit()
#I'm kinda sad about how the line above me was the 99th line so I decided to make some filler.
