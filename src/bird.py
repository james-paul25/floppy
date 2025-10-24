import pygame
GRAVITY = 0.5
JUMP_VELOCITY = -9
BIRD_RADIUS = 12

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 0
        self.image = pygame.image.load("assets/ghost.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (48, 48))
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def jump(self):
        self.vel = JUMP_VELOCITY

    def update(self):
        self.vel += GRAVITY
        self.y += self.vel
        self.rect.centery = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)