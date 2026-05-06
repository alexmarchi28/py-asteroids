import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT),
        pygame.FULLSCREEN | pygame.SCALED,
    )
    pygame.mouse.set_visible(False)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)

    asteroid = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            screen.fill("black")


            for thing in updatable:
                thing.update(dt)

            for asteroid in asteroids:

                if asteroid.collides(player):
                    print("Game Over!")
                    return

                for shot in shots:
                    if asteroid.collides(shot):
                        asteroid.split()
                        shot.kill()

            for thing in drawable:
                thing.draw(screen)

            # updates entire screen
            pygame.display.flip()
            dt = clock.tick(60) / 1000
    finally:
        pygame.mouse.set_visible(True)
        pygame.quit()


if __name__ == "__main__":
    main()
