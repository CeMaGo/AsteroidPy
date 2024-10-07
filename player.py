import pygame
from circleshape import CircleShape
from constants import * 

WHITE = (255, 255, 255)
lw = 2

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        # Call the parent class (CircleShape) constructor, passing x, y, and PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)

        # Initialize the rotation field to 0
        self.rotation = 0

         # Rotate method to modify the player's rotation based on turn speed
    def rotate(self, dt):
            self.rotation += PLAYER_TURN_SPEED * dt

    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), lw)


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys [pygame.K_a]:
            self.rotate(-dt) # Rotate left by inverting dt

        if keys [pygame.K_d]:
            self.rotate(dt)

     # Method to generate the triangle shape (given in the prompt)
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b,c]
