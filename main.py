import pygame
from constants import *
from player import Player

def main():
    pygame.init() # pygame.init() -> (numpass, numfail)
    
    #display.set mode(), Set up display dimension
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set up colors
    BLACK = (0, 0, 0)

    # Create the title of the Window
    pygame.display.set_caption("Asteroids Game")

    # Create a clcok object to control the FPS
    clock = pygame.time.Clock()
    # Initialize delta time
    dt = 0

    # Instantiate the Player object at the center of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # ========= Start the Game loop ===============>>>

    running = True
    while running:
        # Fill the screen with black color
        screen.fill(BLACK)

        # Update the player (including rotation) with the delta time
        player.update(dt)

        # Draw the player on the screen
        player.draw(screen)

        # Refresh the display
        pygame.display.flip()

        # Cap the FPS at 60 and get the time passes since last tick
        dt = clock.tick(60) / 1000 # Convert milliseconds to seconds
     
        # Check for any evnet, like closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    # Quit Pygame when the loop ends
    pygame.quit()


if __name__ == "__main__":
    main()

