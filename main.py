import pygame
import engine
import reader
import sys

State = "game"  # a state variable
MAXFPS = 60  # Maximum rate the loop will run at
CLOCK = pygame.time.Clock()  # Object used to restrict framerate of program

if __name__ == '__main__':
    pygame.init()
    display = pygame.display.set_mode((1024, 768))

    GameEngine = engine.Game()
    theMap = reader.Map()

    map_list, tile_list = theMap.read('test_map')

    looping = True
    while looping:  # Main loop
        # Manage logic
        if State == "game":
            GameEngine.on_loop(map_list, display)

        pygame.display.flip()  # Update the entire display
        CLOCK.tick(MAXFPS)  # Cap Framerate
