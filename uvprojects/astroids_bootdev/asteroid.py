import pygame
import constants
import circleshape
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, pygame.Color(255, 255, 255), (self.position.x, self.position.y), self.radius, width = 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        velocity_one = self.velocity.rotate(random_angle) 
        velocity_two = self.velocity.rotate(-random_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        old_velocity = self.velocity
        Split_Asteroid_One = Asteroid(self.position.x, 
                                      self.position.y, 
                                      new_radius)
        Split_Asteroid_One.velocity = velocity_one * 1.2
        Split_Asteroid_Two = Asteroid(self.position.x, 
                                      self.position.y, 
                                      new_radius)
        Split_Asteroid_Two.velocity = velocity_two * 1.2

