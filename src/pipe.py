import pygame
import random
from src.constants import HEIGHT, GROUND_HEIGHT, PIPE_GAP, PIPE_WIDTH, PIPE_SPEED

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(80, HEIGHT - GROUND_HEIGHT - PIPE_GAP - 80)
        self.passed = False

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self, surf):
        # Top pipe
        pygame.draw.rect(surf, (34, 139, 34), (self.x, 0, PIPE_WIDTH, self.height))

        # Bottom pipe
        bottom_y = self.height + PIPE_GAP
        bottom_height = HEIGHT - GROUND_HEIGHT - bottom_y
        if bottom_height > 0:
            pygame.draw.rect(surf, (34, 139, 34), (self.x, bottom_y, PIPE_WIDTH, bottom_height))
