import pygame
from pygame.locals import *
from classe import *
from constantes import *

# Affichage premier ecran


pygame.init()

win = pygame.display.set_mode((640, 480), RESIZABLE)

welcome = pygame.image.load('structures.png')

win.blit(welcome, (0,0))
pygame.display.set_caption('accueil')

pygame.display.flip()

continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    # Affichage labyrinthe du jeu
    labyrinthe = Labyrinthe('labyrinthe.txt')
    labyrinthe.show(win)
    pygame.display.flip()
    # Lancement du jeu    
    

    perso = Macgayver(labyrinthe)
    
    while start_game:
    
    #Deplacement
        
        if event.type == QUIT:
            continuer = 0
            start_game = 0
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                start_game = 0
            elif event.key == K_RIGHT:
                perso.move('right')
            elif event.key == K_LEFT:
                perso.move('left')
            elif event.key == K_UP:
                perso.move('up')
            elif event.key == K_DOWN:
                perso.move('down')  
            
# Nouvelle position
        
    # arrivée
if labyrinthe.structure[perso.case_y][perso.case_x] == [14,14]:
    start_game = 0
    pygame.quit()
