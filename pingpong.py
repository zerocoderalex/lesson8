import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-Понг")

# Классы
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)

    def move(self, dy):
        self.rect.y += dy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 15, 15)
        self.speed_x = random.choice([-5, 5])
        self.speed_y = random.choice([-5, 5])

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Отскок от верхней и нижней границ
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

# Создание объектов
player = Paddle(50, HEIGHT // 2 - 50)
opponent = Paddle(WIDTH - 60, HEIGHT // 2 - 50)
ball = Ball()

# Счет
player_score = 0
opponent_score = 0

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move(-10)
    if keys[pygame.K_DOWN]:
        player.move(10)

    # Логика для противника
    if opponent.rect.centery < ball.rect.centery:
        opponent.move(5)
    elif opponent.rect.centery > ball.rect.centery:
        opponent.move(-5)

    # Движение мяча
    ball.move()

    # Проверка на столкновение с ракетками
    if ball.rect.colliderect(player.rect) or ball.rect.colliderect(opponent.rect):
        ball.speed_x *= -1

    # Проверка выхода мяча за границы
    if ball.rect.left <= 0:
        opponent_score += 1  # Противник набирает очко
        ball.rect.x = WIDTH // 2
        ball.rect.y = HEIGHT // 2
        ball.speed_x *= random.choice([-1, 1])
        ball.speed_y *= random.choice([-1, 1])
    elif ball.rect.right >= WIDTH:
        player_score += 1  # Игрок набирает очко
        ball.rect.x = WIDTH // 2
        ball.rect.y = HEIGHT // 2
        ball.speed_x *= random.choice([-1, 1])
        ball.speed_y *= random.choice([-1, 1])

    # Отрисовка
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, player.rect)
    pygame.draw.rect(screen, BLACK, opponent.rect)
    pygame.draw.ellipse(screen, BLACK, ball.rect)

    # Отображение счета
    font = pygame.font.Font(None, 74)
    text = font.render(f"{player_score}  {opponent_score}", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 10))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()