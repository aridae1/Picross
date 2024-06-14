#import the pygame module
import pygame

#Initialize pygame
pygame.init()

#Set the window size and assign that to the variable "window"
width = 800
height = 600
window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
#Set the header of the window to be "Pycross"
pygame.display.set_caption('Pycross')

#Set the window icon to be picross.jpg
picross_icon = pygame.image.load("picross.jpg")
pygame.display.set_icon(picross_icon)

'''Set the variable "open" equal to True and begin the main while loop that continues as long as open 
continues to be True'''
open = True
while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False

    window.fill((0, 0, 0))
    width, height = window.get_size()
    grid_width = width-400
    grid_height = height-200
    grid = pygame.Surface((grid_width,grid_height))
    grid.fill((255, 255, 255))
    '''Get the center of the screen by taking the width of the window and subtracting it by the width of the 
    rectangle and dividing all of that by 2. Do the same with the height.'''
    center = ((width - grid.get_width()) / 2, (height - grid.get_height()) / 2)
    window.blit(grid, center)



    pygame.display.update()

pygame.quit()
