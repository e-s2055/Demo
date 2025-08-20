import pygame, constants
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while True:
        screen.fill((0,0,0), rect=None, special_flags=0)
        pygame.display.flip()

if __name__ == "__main__":
    main()
