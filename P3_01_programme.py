import pygame


# Affichage premier ecran





# Affichage du labyrynthe
def show_lab():

    labyrinthe = ['d00mmmmm0m00mmm', '0m00000m0mm0m00', '00mm0m000m0000m', 'm000mmmm000mmmm', '000m00000mmm00m', 'mm0mmmm0mm000mm',
    '000mmm0000mmmmm', '0m000mm0m0mm00m', '0mm0m000m000mmm', 'mmm00mmmm0mmmmm', 'mmm0mm0m00mm00m', 'm000m00m0mm00mm', '00mm00m00000mmm',
    'mmmmm0mm0mm0mmm', 'm0000mmm00m000a']
    
    level_lab = []
    for level in labyrinthe:
        level_line = []

        for sprite in level:
            if sprite != '\n':
                level_line.append(sprite)

                'print(level_line)'
        level_lab.append(level_line)
        print(level_lab)

show_lab()
