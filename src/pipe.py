import pygame
import random
from src.constants import HEIGHT, GROUND_HEIGHT, PIPE_GAP, PIPE_WIDTH, PIPE_SPEED

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(80, HEIGHT - GROUND_HEIGHT - PIPE_GAP - 80)
        self.width = PIPE_WIDTH 
        self.passed = False
        self.gap = PIPE_GAP
        
        #pipe_image = pygame.image.load("assets/pipe.png").convert_alpha()
    
        #self.image_top = pygame.transform.scale(pipe_image, (self.width, self.height))
        #bottom_height = HEIGHT - GROUND_HEIGHT - (self.height + PIPE_GAP)
        #self.image_bottom = pygame.transform.scale(pipe_image, (self.width, bottom_height))
        #self.image_bottom = pygame.transform.flip(self.image_bottom, False, True)
        
        #self.top_rect = self.top_image.get_rect(bottom=self.height)
        #self.bottom_rect = self.image_bottom.get_rect(top=self.height + self.gap)

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self, surf):
        pygame.draw.rect(surf, (34, 139, 34), (self.x, 0, PIPE_WIDTH, self.height))

        bottom_y = self.height + PIPE_GAP
        bottom_height = HEIGHT - GROUND_HEIGHT - bottom_y
        if bottom_height > 0:
            pygame.draw.rect(surf, (34, 139, 34), (self.x, bottom_y, PIPE_WIDTH, bottom_height))
