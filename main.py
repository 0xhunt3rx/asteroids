import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots     = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    asteroidField = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        player.timer -= dt
        
        for asteroid in asteroids:
            if player.isCollided(asteroid):
                sys.exit(1)

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick() / 1000

if __name__ == "__main__":
    main()
