import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import * 

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

    # Create groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable) 
    
    AsteroidField.containers = (updatable,)

    asteroid_field = AsteroidField()

    # Example: Add asteroid to the group
    asteroid = Asteroid(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 50) # Example radius of 50
    asteroids.add(asteroid)

    #Add player to both groups
    updatable.add(player)
    drawable.add(player)


    # ========= Start the Game loop ===============>>>

    running = True
    while running:

        # Update the player (including rotation) with the delta time
       # player.update(dt)

        # Draw the player on the screen
       # player.draw(screen)

        # Cap the FPS at 60 and get the time passes since last tick
        dt = clock.tick(60) / 1000 # Convert milliseconds to seconds
     
        # Check for any evnet, like closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get all keys pressed
        keys = pygame.key.get_pressed()

        # Update all objects in the updatable group
        for obj in updatable:
            obj.update(dt)

        #Fill the screen Black
        screen.fill(BLACK)

        # Update all objects in the drawable group
        for obj in drawable:
            obj.draw(screen)

        # Update asteroid
        asteroid.update(dt)

        # Draw asteroids
        for asteroid in asteroids:
            asteroid.draw(screen)

        # Refrech display
        pygame.display.flip()

    # Quit Pygame when the loop ends
    pygame.quit()


if __name__ == "__main__":
    main()

