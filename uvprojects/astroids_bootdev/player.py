import pygame
import circleshape
import constants
import shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        return pygame.draw.polygon(screen, pygame.Color(255, 255, 255), self.triangle(), width = 2)

    def rotate(self, dt):
        return constants.PLAYER_TURN_SPEED * dt
    
    def move(self, dt, direction=1):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt * direction
        return self.position

    def shoot(self):
        if self.timer > 0:
            return
        self.timer = constants.PLAYER_SHOOT_COOLDOWN
        bullet = shot.Shot(self.position.x, self.position.y)
        vector = pygame.Vector2(0, 1)
        bullet.velocity = vector.rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED            

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()  
        if keys[pygame.K_a]:
            self.rotation += self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotation -= self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt, -1)
        if keys[pygame.K_SPACE]:
            self.shoot()
