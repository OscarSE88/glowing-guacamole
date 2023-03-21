
import pygame
from sys import exit 
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

sky_surface = pygame.Surface((800,300))
sky_surface.fill('Blue')
ground_surface = pygame.Surface((800,100))
ground_surface.fill('Green')

char_surface = pygame.Surface((50,50))
char_surface.fill('Yellow')
char_x_pos = 600
char_y_pos = 250



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            pygame.key.set_repeat(K_d, K_a)
            pygame.key.set_repeat(K_s, K_w)             
            if event.key in [K_w]:
                char_y_pos -=20
                
            if event.key in [K_a]:
                char_x_pos -=20
                
            if event.key in [K_s]:
                char_y_pos +=20
                
            if event.key in [K_d]:
                char_x_pos +=20
           
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and keys[pygame.K_d]:
                char_y_pos -=10
                char_x_pos +=10
            if keys[pygame.K_w] and keys[pygame.K_a]:
                char_y_pos -=10
                char_x_pos -=10
            if keys[pygame.K_s] and keys[pygame.K_d]:
                char_y_pos +=10
                char_x_pos +=10
            if keys[pygame.K_s] and keys[pygame.K_a]:
                char_y_pos +=10
                char_x_pos -=10
        
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(char_surface,(char_x_pos,char_y_pos))
    
    pygame.display.update()
    clock.tick(60)
