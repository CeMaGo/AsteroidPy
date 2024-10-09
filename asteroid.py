import pygame
from circleshape import CircleShape

class Asteroid(CircleShape, pygame.sprite.Sprite):
    
    def __init__(self, x, y, radius):
        conatiners = None

        # Call the parent class constructor
        super().__init__(x, y, radius)

        # Initialize the velocity of the asteroid
        self.velocity = pygame.Vector2(1, 1) # can be adjusted to randomize

    def draw(self, screen):
        # Drae th asteroid as a circle on the screen
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        # Update the position by adding velocity * dt
        self.position += self.velocity * dt

