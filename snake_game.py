import pygame
import random
import sys

# Setup for Trinket Pygame
pygame.init()
CELL_SIZE = 20
COLS, ROWS = 30, 20
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
BG = (30, 30, 30)
SNAKE_HEAD = (0, 255, 127)
SNAKE_BODY = (50, 205, 50)
WALL = (255, 182, 193)  # Pink Walls
TARGET = (255, 255, 0)  # Yellow Target (C)
TEXT = (255, 255, 255)

font = pygame.font.SysFont("Consolas", 16)

# Text-art style maze layout
maze_raw = [
    "##############################",
    "#           C            C   #",
    "#  #########  #######  ###   #",
    "#  #       #     C   #    C  #",
    "#  #  ###  #########  ####   #",
    "#     # C        #         C #",
    "#  #######  ##   #  #######  #",
    "#      C    ##   #     C     #",
    "#  ###########   #######  ####",
    "#                            #",
    "#   holbertonholberton      #",
    "#  #########   ##########   #",
    "#  #       # C        #     #",
    "#  #  ###  #######  ####### #",
    "#     #        C #     C    #",
    "#  #######  ##   #  ####### #",
    "#      C    ##   #     C    #",
    "#  ###########   #######  ###",
    "#           C            C  #",
    "##############################"
]

def parse_maze():
    walls = []
    targets = []
    for y, row in enumerate(maze_raw):
        for x, cell in enumerate(row):
            if cell == "#":
                walls.append((x, y))
            elif cell == "C":
                targets.append((x, y))
    return walls, targets

walls, targets = parse_maze()
snake = [(1, 1)]
direction = (1, 0)
score = 0

def draw_cell(x, y, color):
    pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_maze():
    for x, y in walls:
        draw_cell(x, y, WALL)
    for tx, ty in targets:
        text = font.render("C", True, TARGET)
        screen.blit(text, (tx * CELL_SIZE + 4, ty * CELL_SIZE + 2))
    for y, row in enumerate(maze_raw):
        for x, ch in enumerate(row):
            if ch in "holberton":
                text = font.render(ch, True, TEXT)
                screen.blit(text, (x * CELL_SIZE + 3, y * CELL_SIZE + 2))

def move_snake():
    global score
    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)
    if new_head in walls or new_head in snake:
        game_over()
    snake.insert(0, new_head)

    if new_head in targets:
        score += 1
        targets.remove(new_head)
    else:
        snake.pop()

def draw_snake():
    for i, (x, y) in enumerate(snake):
        color = SNAKE_HEAD if i == 0 else SNAKE_BODY
        draw_cell(x, y, color)

def game_over():
    msg = font.render("Game Over! Score: " + str(score), True, TEXT)
    screen.blit(msg, (WIDTH // 2 - 100, HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

clock = pygame.time.Clock()

# Game loop for Trinket
running = True
while running:
    screen.fill(BG)
    draw_maze()
    draw_snake()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    move_snake()
    pygame.display.update()
    clock.tick(7)

pygame.quit()

