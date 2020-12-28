import pygame
import sys
#ventana
ventana = pygame.display.set_mode((800,600))


game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    


    #Dibujar el jugador
    pygame.draw.rect(ventana, ())