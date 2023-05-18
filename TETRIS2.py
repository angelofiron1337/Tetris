import pygame
import sys
import random
import copy
from tetrimino import Tetrimino, tetrimino_shapes, COLORS
from title_screen import title_screen

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 30
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

# Function to create an empty grid
def create_grid():
    return [[(0, 0, 0) for _ in range(COLS)] for _ in range(ROWS)]

# Function to check if a tetrimino move is valid
def valid_move(tetrimino, grid, dx=0, dy=0):
    for y, row in enumerate(tetrimino.shape):
        for x, cell in enumerate(row):
            if cell == 'O':
                if (tetrimino.x + x + dx < 0 or tetrimino.x + x + dx >= COLS or
                        tetrimino.y + y + dy >= ROWS or
                        grid[tetrimino.y + y + dy][tetrimino.x + x + dx] != (0, 0, 0)):
                    return False
    return True

# Function to add a tetrimino to the grid
def add_to_grid(tetrimino, grid):
    for y, row in enumerate(tetrimino.shape):
        for x, cell in enumerate(row):
            if cell == 'O':
                grid[tetrimino.y + y][tetrimino.x + x] = tetrimino.color

# Function to clear completed lines and return the number of lines cleared
def clear_lines(grid):
    full_rows = [i for i, row in enumerate(grid) if all(cell != (0, 0, 0) for cell in row)]
    if full_rows:
        for row in full_rows:
            del grid[row]
            grid.insert(0, [(0, 0, 0) for _ in range(COLS)])
        return len(full_rows)
    return 0

def draw_window(screen, grid, tetrimino=None):
    screen.fill(BLACK)

    # Draw the grid cells
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            pygame.draw.rect(screen, cell, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1))

    # Draw the tetrimino
    if tetrimino:
        for y, row in enumerate(tetrimino.shape):
            for x, cell in enumerate(row):
                if cell == 'O':
                    pygame.draw.rect(screen, tetrimino.color, ((tetrimino.x + x) * GRID_SIZE, (tetrimino.y + y) * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1))

    # Draw the grid lines on top
    line_width = 2
    for y in range(ROWS + 1):
        pygame.draw.line(screen, (128, 128, 128), (0, y * GRID_SIZE), (WIDTH, y * GRID_SIZE), line_width)
    for x in range(COLS + 1):
        pygame.draw.line(screen, (128, 128, 128), (x * GRID_SIZE, 0), (x * GRID_SIZE, HEIGHT), line_width)

    pygame.display.flip()







def handle_game_events(tetrimino, grid):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if valid_move(tetrimino, grid, dx=-1):
                    tetrimino.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                if valid_move(tetrimino, grid, dx=1):
                    tetrimino.move(1, 0)
            elif event.key == pygame.K_DOWN:
                if valid_move(tetrimino, grid, dy=1):
                    tetrimino.move(0, 1)
            elif event.key == pygame.K_SPACE:
                copy_tetrimino = copy.deepcopy(tetrimino)  # Make a copy of the current tetrimino
                copy_tetrimino.rotate()  # Rotate the copy
                if valid_move(copy_tetrimino, grid):  # Check if the rotated copy is valid
                    tetrimino.rotate()  # If it's valid, apply the rotation to the actual tetrimino


# Yield the next tetrimino
def get_next_tetrimino():
    tetrimino = random.choice(tetrimino_shapes)
    while True:
        yield tetrimino
        tetrimino = random.choice(tetrimino_shapes)

next_tetrimino = get_next_tetrimino()

def spawn_tetrimino():
    new_tetrimino = Tetrimino(5, 0, random.choice(tetrimino_shapes))
    new_tetrimino.update_shape()  # Make sure to call update_shape(), not update()
    return new_tetrimino

# Main game loop
def main():
    grid = create_grid()
    tetrimino = spawn_tetrimino()
    fall_time = 0
    fall_speed = 500  # Adjust for difficulty
    score = 0

    while True:
        delta_time = clock.tick(60)
        fall_time += delta_time

        if fall_time > fall_speed:
            fall_time = 0
            if valid_move(tetrimino, grid, dy=1):
                tetrimino.move(0, 1)
            else:
                add_to_grid(tetrimino, grid)
                score += clear_lines(grid)
                tetrimino = spawn_tetrimino()

                if not valid_move(tetrimino, grid):
                    break

        handle_game_events(tetrimino, grid)

        draw_window(screen, grid, tetrimino)

        pygame.display.flip()

# Start the game
if __name__ == "__main__":
    while True:
        title_screen(screen, WIDTH, HEIGHT, clock)
        main()

