import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    try:
        while True:
            log_state()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            player.update(dt)

            screen.fill("black")
            player.draw(screen)
            pygame.display.flip()

            # limit the framerate to 60 FPS
            dt = clock.tick(60) / 1000

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        sys.exit(1)


if __name__ == "__main__":
    main()
