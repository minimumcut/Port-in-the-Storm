# Import the pygame library and initialise the game engine
import pygame
import pytmx
from pytmx import load_pygame
from Game import Game
from Level import Level
from Level import LevelProperties

def main():
    pygame.init()

    size = (640, 480)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Port in a Storm")

    clock = pygame.time.Clock()

    levelProps = LevelProperties("Test level", 1)
    initialLevel = Level(levelProps, 30, 30, [], "test.tmx") # hardcoding rip
    game = Game(initialLevel)

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