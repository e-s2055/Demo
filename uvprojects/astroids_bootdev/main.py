import sys
import pygame
import constants
import circleshape 
import player
import asteroidfield
import asteroid
import shot
from constants import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    shot.Shot.containers = (shots, updatable, drawable)
    player.Player.containers = (updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable, )
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    player1 = player.Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = asteroidfield.AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), rect=None, special_flags=0)        
        for group_object in drawable:
            group_object.draw(screen)
        updatable.update(dt)
        for one_asteroid in asteroids:
            if player1.collision(one_asteroid) is True:
                raise SystemExit (sys.exit("Game Over!"))
        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
