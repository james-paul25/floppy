import pygame

class Pipe:
    def __init__(self, x, height, gap, ground_height, screen_height):
        self.x = x
        self.height = height
        self.gap = gap
        self.width = 70
        self.speed = 3
        self.ground_height = ground_height
        self.screen_height = screen_height
        self.passed = False

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        # top pipe
        pygame.draw.rect(screen, (34,139,34), (self.x, 0, self.width, self.height))
        # bottom pipe
        bottom_y = self.height + self.gap
        bottom_height = self.screen_height - self.ground_height - bottom_y
        pygame.draw.rect(screen, (34,139,34), (self.x, bottom_y, self.width, bottom_height))
