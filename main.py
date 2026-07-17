import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state, log_event


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    try:
        while True:
            log_state()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            updatable.update(dt)

            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    log_event("player_hit")
                    print("Game over!")
                    sys.exit()

            screen.fill("black")
            for obj in drawable:
                obj.draw(screen)
            pygame.display.flip()

            # 1. get the delta time
            # pygame.time.Clock.tick(framerate=0) -> milliseconds
            # computes how many miliseconds have passed since previous call; by dividing the result by 1000, you get the seconds
            # in this loop .tick() is called once per frame to get the delta time between each frame
            # 2. limit the framerate to 60 FPS
            # by passing it the framerate, the function will delay to keep the game running slower than the given ticks/frames per second
            dt = clock.tick(60) / 1000

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        sys.exit(1)


if __name__ == "__main__":
    main()
