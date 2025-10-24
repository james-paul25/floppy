import pygame, sys, random
from src.bird import Bird
from src.pipe import Pipe
from src.base import Base
from src.utils import check_collision
from src.constants import WIDTH, HEIGHT, FPS, PIPE_GAP, PIPE_WIDTH, PIPE_SPEED, PIPE_SPAWN_INTERVAL, GROUND_HEIGHT
from src.constants import RED, WHITE, BLACK
from src.score import load_high_score, save_high_score

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Floppy Bird- Clone")
        self.clock = pygame.time.Clock()
        self.scoreFont = pygame.font.SysFont(None, 36)
        self.infoFont = pygame.font.SysFont(None, 24)
        
        self.bg_image = pygame.image.load("assets/bg.jpg").convert()
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH, HEIGHT))

        self.bird = Bird(80, HEIGHT // 2)
        self.pipes = []
        self.base = Base(HEIGHT - GROUND_HEIGHT)
        self.score = 0
        self.game_over = False
        self.high_score = load_high_score()

        self.last_pipe_time = pygame.time.get_ticks()
        pygame.mouse.set_visible(False)

    def spawn_pipe(self):
        x = WIDTH
        top_pipe = Pipe(x)
        self.pipes.append(top_pipe)


    def handle_events(self, running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                running = False
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.game_over:
                        self.bird.jump()
                    else:
                        self.restart()
        return running
    
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

        if check_collision(self.bird, self.pipes, HEIGHT, GROUND_HEIGHT):
            self.game_over = True
            if self.score > self.high_score:
                self.high_score = self.score
                save_high_score(self.high_score)

        for pipe in self.pipes:
            if not pipe.passed and pipe.x + pipe.width < self.bird.x:
                pipe.passed = True
                self.score += 1

    def draw(self):
        self.screen.blit(self.bg_image, (0,0))

        for pipe in self.pipes:
            pipe.draw(self.screen)

        self.base.draw(self.screen)

        self.bird.draw(self.screen)

        score_text = self.scoreFont.render(str(self.score), True, BLACK)
        self.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 30))
        
        high_score_text = self.infoFont.render(f"High Score: {self.high_score}", True, BLACK)
        self.screen.blit(high_score_text, (10, 10))

        if self.game_over:
            gameOverText = self.infoFont.render("GAME OVER - Press SPACE to restart", True, RED)
            self.screen.blit(gameOverText, (WIDTH // 2 - gameOverText.get_width() // 2, HEIGHT // 2 - 20))
            
            quitText = self.infoFont.render("Press Q to Quit", True, RED)
            self.screen.blit(quitText, (WIDTH // 2 - quitText.get_width() // 2, HEIGHT // 2 + 10))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            running = self.handle_events(running)
            self.update()
            self.draw()
            self.clock.tick(FPS)
