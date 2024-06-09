import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake settings
snake_size = 20
snake_speed = 15
snake = [(100, 50), (90, 50), (80, 50)]
direction = 'RIGHT'
change_to = direction

# Food settings
food_pos = [random.randrange(1, (width // snake_size)) * snake_size,
            random.randrange(1, (height // snake_size)) * snake_size]
food_spawn = True

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    # Update direction
    direction = change_to

    # Update snake position
    if direction == 'UP':
        snake.insert(0, (snake[0][0], snake[0][1] - snake_size))
    if direction == 'DOWN':
        snake.insert(0, (snake[0][0], snake[0][1] + snake_size))
    if direction == 'LEFT':
        snake.insert(0, (snake[0][0] - snake_size, snake[0][1]))
    if direction == 'RIGHT':
        snake.insert(0, (snake[0][0] + snake_size, snake[0][1]))

    # Snake eating food
    if snake[0] == tuple(food_pos):
        food_spawn = False
    else:
        snake.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (width // snake_size)) * snake_size,
                    random.randrange(1, (height // snake_size)) * snake_size]
    food_spawn = True

    # Game Over conditions
    if (snake[0][0] not in range(0, width) or
            snake[0][1] not in range(0, height)):
        running = False
    for block in snake[1:]:
        if snake[0] == block:
            running = False

    # Drawing
    screen.fill(black)
    for pos in snake:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], snake_size, snake_size))
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], snake_size, snake_size))

    pygame.display.flip()
    clock.tick(snake_speed)

pygame.quit()
sys.exit()
