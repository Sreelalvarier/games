import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
PLAYER_COLOR = (0, 128, 255)
OBSTACLE_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
FPS = 60
OBSTACLE_SPEED = 5
PLAYER_SPEED = 10
SCORE_COLOR = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simple Endless Runner')

# Player setup
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - PLAYER_HEIGHT - 10
player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)

# Obstacle setup
obstacles = []

# Score setup
score = 0
font = pygame.font.Font(None, 36)


def create_obstacle():
    x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
    y = -OBSTACLE_HEIGHT
    rect = pygame.Rect(x, y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
    obstacles.append(rect)


def move_obstacles():
    for obstacle in obstacles:
        obstacle.y += OBSTACLE_SPEED


def check_collision():
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            return True
    return False


def remove_offscreen_obstacles():
    global obstacles
    obstacles = [obstacle for obstacle in obstacles if obstacle.y < SCREEN_HEIGHT]


def draw_score(score):
    score_text = font.render(f"Score: {score}", True, SCORE_COLOR)
    screen.blit(score_text, (10, 10))


# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.x - PLAYER_SPEED >= 0:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_rect.x + PLAYER_SPEED <= SCREEN_WIDTH - PLAYER_WIDTH:
        player_rect.x += PLAYER_SPEED

    if random.randint(1, 100) <= 10:  # 10% chance to create a new obstacle each frame
        create_obstacle()

    move_obstacles()
    remove_offscreen_obstacles()

    if check_collision():
        print(f"Game Over! Final Score: {score}")
        running = False

    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)
    for obstacle in obstacles:
        pygame.draw.rect(screen, OBSTACLE_COLOR, obstacle)

    score += 1  # Increment score each frame
    draw_score(score)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
