import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)

    asteroid = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print(player.containers)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")


        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)

        # updates entire screen
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
