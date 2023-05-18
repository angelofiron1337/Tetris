import pygame
import sys
import random
from tetrimino import Tetrimino, tetrimino_shapes, COLORS
from title_screen import title_screen

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 30
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class GameEngine:
    # Initialize the game engine with a screen to draw on
    def __init__(self, screen):
        self.screen = screen
        self.grid = self.create_grid()
        self.tetrimino = self.spawn_tetrimino()
        self.fall_time = 0
        self.fall_speed = 500
        self.score = 0
        self.next_tetrimino = self.get_next_tetrimino()

    # Other methods go here...

    # Spawn a new tetrimino at the top of the grid
    def spawn_tetrimino(self):
        new_tetrimino = Tetrimino(5, 0, random.choice(tetrimino_shapes))
        new_tetrimino.update_shape()
        return new_tetrimino

    # Main game loop
    def run_game(self):
        clock = pygame.time.Clock()

        while True:
            delta_time = clock.tick(60)
            self.fall_time += delta_time

            if self.fall_time > self.fall_speed:
                self.fall_time = 0
                if self.valid_move(self.tetrimino, dy=1):
                    self.tetrimino.move(0, 1)
                else:
                    self.add_to_grid(self.tetrimino)
                    self.score += self.clear_lines()
                    self.tetrimino = self.spawn_tetrimino()

                    # Check if the spawned tetrimino is colliding with the grid, which indicates game over
                    if not self.valid_move(self.tetrimino):
                        break

            self.handle_game_events()

            self.draw_window(self.tetrimino)

            pygame.display.flip()

    # Draw the current state of the game, including the tetrimino
    def draw(self):
        self.draw_window(self.tetrimino)

    def create_grid(self):
        pass
