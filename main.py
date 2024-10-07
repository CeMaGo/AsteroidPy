# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
    pygame.init() # pygame.init() -> (numpass, numfail)
    
    #display.set mode(), Set up display dimension
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set up colors
    BLACK = (0, 0, 0)

    # Test Print
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Start the Game loop
    running = True
    while running:
        # Check for any evnet, like closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with black color
        screen.fill(BLACK)

        # Update the display
        pygame.display.flip()

    # Quit Pygame when the loop ends
    pygame.quit()


if __name__ == "__main__":
    main()

