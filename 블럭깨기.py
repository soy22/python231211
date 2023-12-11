import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블록깨기 게임")

# 색깔 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 패들 설정
paddle_width, paddle_height = 100, 10
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - 20

# 공 설정
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5 * random.choice([1, -1])
ball_speed_y = -5

# 블록 설정
block_width, block_height = 50, 20
blocks = []
for row in range(5):
    for col in range(WIDTH // block_width):
        block = pygame.Rect(col * block_width, row * block_height, block_width, block_height)
        blocks.append(block)

# 게임 루프
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 5
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += 5

    # 움직이는 부분
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 벽과 충돌
    if ball_x <= 0 or ball_x >= WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y

    # 패들과 충돌
    if (
        paddle_x < ball_x < paddle_x + paddle_width
        and paddle_y < ball_y < paddle_y + paddle_height
    ):
        ball_speed_y = -ball_speed_y

    # 블록과 충돌
    for block in blocks:
        if block.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)):
            ball_speed_y = -ball_speed_y
            blocks.remove(block)

    # 그리기
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)

    for block in blocks:
        pygame.draw.rect(screen, WHITE, block)

    pygame.display.flip()
    clock.tick(60)
