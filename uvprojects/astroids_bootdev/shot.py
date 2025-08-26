import circleshape
import pygame
import constants

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius = constants.SHOT_RADIUS)
        

    def draw(self, screen):
        return pygame.draw.circle(screen, pygame.Color(255, 255, 255), (self.position.x, self.position.y), self.radius, width = 2)
    
    def update(self, dt):
        self.position += self.velocity * dt