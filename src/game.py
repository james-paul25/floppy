import pygame, sys, random
from src.bird import Bird
from src.pipe import Pipe
from src.base import Base
from src.utils import check_collision

WIDTH, HEIGHT = 400, 600
FPS = 60
PIPE_GAP = 150
PIPE_SPEED = 3
PIPE_SPAWN_INTERVAL = 1500 
GROUND_HEIGHT = 100
BG_COLOR = (135, 206, 235)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Floppy Bird- Clone")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)

        self.bird = Bird(80, HEIGHT // 2)
        self.pipes = []
        self.base = Base(HEIGHT - GROUND_HEIGHT)
        self.score = 0
        self.game_over = False

        self.last_pipe_time = pygame.time.get_ticks()

    def spawn_pipe(self):
        x = WIDTH
        height = random.randint(100, HEIGHT - GROUND_HEIGHT - PIPE_GAP - 50)
        top_pipe = Pipe(x, height, PIPE_GAP, HEIGHT - GROUND_HEIGHT, HEIGHT)
        self.pipes.append(top_pipe)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.game_over:
                        self.bird.jump()
                    else:
                        self.restart()

    def restart(self):
        self.bird = Bird(80, HEIGHT // 2)
        self.pipes.clear()
        self.score = 0
        self.game_over = False
        self.last_pipe_time = pygame.time.get_ticks()

    def update(self):
        if self.game_over:
            return

        self.bird.update()
        self.base.update()
        
        current_time = pygame.time.get_ticks()
        if current_time - self.last_pipe_time > PIPE_SPAWN_INTERVAL:
            self.spawn_pipe()
            self.last_pipe_time = current_time

        for pipe in self.pipes:
            pipe.update()

        self.pipes = [pipe for pipe in self.pipes if pipe.x + pipe.width > 0]

        # Collision detection
        if check_collision(self.bird, self.pipes, HEIGHT, GROUND_HEIGHT):
            self.game_over = True

        for pipe in self.pipes:
            if not pipe.passed and pipe.x + pipe.width < self.bird.x:
                pipe.passed = True
                self.score += 1

    def draw(self):
        self.screen.fill(BG_COLOR)

        for pipe in self.pipes:
            pipe.draw(self.screen)

        self.base.draw(self.screen)

        self.bird.draw(self.screen)

        score_text = self.font.render(str(self.score), True, (255, 255, 255))
        self.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 30))

        if self.game_over:
            text = self.font.render("GAME OVER - Press SPACE to restart", True, (255, 0, 0))
            self.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 20))

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
