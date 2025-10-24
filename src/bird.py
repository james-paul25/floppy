import pygame
GRAVITY = 0.5
JUMP_VELOCITY = -9
BIRD_RADIUS = 12

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 0

    def jump(self):
        self.vel = JUMP_VELOCITY

    def update(self):
        self.vel += GRAVITY
        self.y += self.vel

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (int(self.x), int(self.y)), BIRD_RADIUS)
