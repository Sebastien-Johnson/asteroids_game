import pygame 
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    
    game_timer = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    
    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) #group objects come after class container asignment
    

    while True: #game loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                return
            
        updatables.update(dt)
        screen.fill("black")

        for obj in drawables: #iterate through drawables
            obj.draw(screen)

        pygame.display.flip()

        dt = game_timer.tick(60)/1000


if __name__ == "__main__":
    main()
