import pygame
WIDTH = 400

class Base:
    def __init__(self, y):
        self.y = y
        self.width = WIDTH
        self.height = 100
        self.x1 = 0
        self.x2 = self.width
        self.speed = 3

    def update(self):
        self.x1 -= self.speed
        self.x2 -= self.speed
        if self.x1 + self.width < 0:
            self.x1 = self.x2 + self.width
        if self.x2 + self.width < 0:
            self.x2 = self.x1 + self.width

    def draw(self, screen):
        pygame.draw.rect(screen, (222,184,135), (self.x1, self.y, self.width, self.height))
        pygame.draw.rect(screen, (222,184,135), (self.x2, self.y, self.width, self.height))
