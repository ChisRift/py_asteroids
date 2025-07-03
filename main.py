# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from asteroidfield import *
from player import Player
from asteroid import Asteroid
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # create groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # assign groups to classes
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)

    # instantiate variables
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    # game loop
    while(True):
        # check events for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # run update logic
        updateable.update(dt)

        # check for asteroid collisions
        # and exit game if found
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit(0)
        
        # fill screen with background color
        screen.fill(color="black")
        
        # draw objects to screen
        for item in drawable:
            item.draw(screen)
        
        # update the display screen
        pygame.display.flip()
        
        # keep a log of the delta
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()
