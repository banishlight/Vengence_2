import pygame
import sys

class Game:

    def on_loop(self,screen ,map_list):
        # get input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        # manage logic


        # draw to screen



        return


class Tile:
    background = (True, None)
    foreground = (False, None)
    prop = (False, None)
    collision = (False, None)

    def __init__(self, b, f, p, c):
        self.background = b
        self.foreground = f
        self.prop = p
        self.collision = c
        return
