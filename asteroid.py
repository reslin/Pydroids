import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vel_1 = self.velocity.rotate(angle)
        vel_2 = self.velocity.rotate(-angle)
        self.radius -= ASTEROID_MIN_RADIUS
        ast_1 = Asteroid(self.position.x, self.position.y, self.radius)
        ast_2 = Asteroid(self.position.x, self.position.y, self.radius)
        ast_1.velocity = vel_1 * 1.2
        ast_2.velocity = vel_2 * 1.2