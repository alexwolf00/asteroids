import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH


class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        nose = self.position + forward * self.radius
        left_wing = self.position - forward * self.radius - right
        right_wing = self.position - forward * self.radius + right
        return [nose, left_wing, right_wing]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
