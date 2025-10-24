# main.py
import pygame, sys, random

FPS = 60
WIDTH, HEIGHT = 400, 600
GROUND_HEIGHT = 100
PIPE_WIDTH = 70
PIPE_GAP = 150
PIPE_SPACING = 160 
BIRD_RADIUS = 12

GRAVITY = 0.5
JUMP_VELOCITY = -9
PIPE_SPEED = 3

# --- Init ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# --- Game objects ---
class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 0
        self.alive = True
    def jump(self):
        self.vel = JUMP_VELOCITY
    def update(self):
        self.vel += GRAVITY
        self.y += self.vel
    def draw(self, surf):
        pygame.draw.circle(surf, (255, 255, 0), (int(self.x), int(self.y)), BIRD_RADIUS)

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(80, HEIGHT - GROUND_HEIGHT - PIPE_GAP - 80)
        self.passed = False
    def update(self):
        self.x -= PIPE_SPEED
    def draw(self, surf):
        # top pipe
        pygame.draw.rect(surf, (34,139,34), (self.x, 0, PIPE_WIDTH, self.height))
        # bottom pipe
        bottom_y = self.height + PIPE_GAP
        pygame.draw.rect(surf, (34,139,34), (self.x, bottom_y, PIPE_WIDTH, HEIGHT - GROUND_HEIGHT - bottom_y))

def check_collision(bird, pipes):
    # ground & ceiling
    if bird.y - BIRD_RADIUS <= 0 or bird.y + BIRD_RADIUS >= HEIGHT - GROUND_HEIGHT:
        return True
    # pipes
    for p in pipes:
        # pipe rects
        top_rect = pygame.Rect(p.x, 0, PIPE_WIDTH, p.height)
        bot_rect = pygame.Rect(p.x, p.height + PIPE_GAP, PIPE_WIDTH, HEIGHT - GROUND_HEIGHT - (p.height + PIPE_GAP))
        bird_rect = pygame.Rect(bird.x - BIRD_RADIUS, bird.y - BIRD_RADIUS, BIRD_RADIUS*2, BIRD_RADIUS*2)
        if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bot_rect):
            return True
    return False

def draw_ground(surf):
    pygame.draw.rect(surf, (222, 184, 135), (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))

# --- Game loop variables ---
bird = Bird(80, HEIGHT//2)
pipes = [Pipe(WIDTH + i * PIPE_SPACING) for i in range(3)]
score = 0
running = True
game_over = False

# --- Main loop ---
while running:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_over:
                    bird.jump()
                else:
                    # restart
                    bird = Bird(80, HEIGHT//2)
                    pipes = [Pipe(WIDTH + i * PIPE_SPACING) for i in range(3)]
                    score = 0
                    game_over = False

    if not game_over:
        bird.update()
        # update pipes, spawn new ones
        for p in pipes:
            p.update()
            # score when bird passes
            if not p.passed and p.x + PIPE_WIDTH < bird.x:
                p.passed = True
                score += 1
        # remove off-screen pipes and append new
        if pipes and pipes[0].x + PIPE_WIDTH < -50:
            pipes.pop(0)
            pipes.append(Pipe(pipes[-1].x + PIPE_SPACING))
        # collisions
        if check_collision(bird, pipes):
            game_over = True

    # --- Draw ---
    screen.fill((135, 206, 235))  # sky
    # draw pipes
    for p in pipes:
        p.draw(screen)
    # draw ground
    draw_ground(screen)
    # draw bird
    bird.draw(screen)

    # score
    score_surf = font.render(str(score), True, (255,255,255))
    screen.blit(score_surf, (WIDTH//2 - score_surf.get_width()//2, 30))

    if game_over:
        go = font.render("GAME OVER - Press SPACE to restart", True, (255,0,0))
        screen.blit(go, (WIDTH//2 - go.get_width()//2, HEIGHT//2 - 20))

    pygame.display.flip()

pygame.quit()
sys.exit()
