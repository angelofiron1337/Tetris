import pygame
from game_engine import GameEngine

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

def main():
    game_engine = GameEngine(screen)
    
    while True:
        game_engine.handle_events()
        game_engine.update()
        game_engine.draw()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
