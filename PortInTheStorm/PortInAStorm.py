# Import the pygame library and initialise the game engine
import pygame
import pytmx

from Constants import RESOLUTION_X, RESOLUTION_Y
from Game import Game
from Level import Level
from Level import LevelProperties
from pytmx import load_pygame

def GameEntry():
    pygame.init()

    size = (RESOLUTION_X, RESOLUTION_Y)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Port in a Storm")

    clock = pygame.time.Clock()

    levelProps = LevelProperties("Test level", 1)
    initialLevel = Level(levelProps, 15, 11, [], "levels/level1.tmx", "dialog/dialog_test.txt", "dialog/dialog_test_end.txt") # hardcoding rip

    levelProps2 = LevelProperties("Test level", 1)
    initialLevel2 = Level(levelProps2, 15, 11, [], "levels/level2.tmx", "dialog/dialog_test.txt", "dialog/dialog_test_end.txt") # hardcoding rip

    levelProps3 = LevelProperties("Test level", 1)
    initialLevel3 = Level(levelProps3, 15, 11, [], "levels/level3.tmx", "dialog/dialog_test.txt", "dialog/dialog_test_end.txt") # hardcoding rip

    levelProps4 = LevelProperties("Test level", 1)
    initialLevel4 = Level(levelProps4, 15, 11, [], "levels/001.tmx", "dialog/dialog_test.txt", "dialog/dialog_test_end.txt") # hardcoding rip

    # levelProps5 = LevelProperties("Test level", 1)
    # initialLevel5 = Level(levelProps5, 15, 11, [], "levels/002.tmx", "dialog/dialog_test.txt", "dialog/dialog_test_end.txt") # hardcoding rip

    # levelProps6 = LevelProperties("Test level", 1)
    # initialLevel6 = Level(levelProps6, 15, 11, [], "levels/003.tmx", "dialog/dialog_test.txt", "dialog/dialog_test_end.txt") # hardcoding rip

    game = Game([initialLevel, initialLevel2, initialLevel3, initialLevel4])

    # --- Main event loop
    while True:
        if not game.HandleInputEvents():
            break

        game.GameTick()
        game.Render(screen)
        
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()