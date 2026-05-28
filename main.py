import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    try:
        while True:
            log_state()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            screen.fill("black")
            pygame.display.flip()
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        sys.exit(1)


if __name__ == "__main__":
    main()
