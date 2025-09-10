import pygame 
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    
    game_timer = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) #group objects come after class container asignment
    
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (drawables, updatables)

    asteroid_field = AsteroidField()

    while True: #game loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                return
            
        updatables.update(dt)
        for asteroid in asteroids:
            if player.collisions(asteroid):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for obj in drawables: #iterate through drawables
            obj.draw(screen)

        pygame.display.flip()

        dt = game_timer.tick(60)/1000


if __name__ == "__main__":
    main()
