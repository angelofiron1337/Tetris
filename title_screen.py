import pygame
import sys
import settings

options_screen = settings.options_screen

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_title_screen(screen, title_pos, instructions_pos, options_pos, font_size):
    font = pygame.font.Font(None, font_size)

    title = font.render("Tetris", True, WHITE)
    title_rect = title.get_rect(center=title_pos)
    screen.blit(title, title_rect)

    instructions = font.render("Press ENTER to start", True, WHITE)
    instructions_rect = instructions.get_rect(center=instructions_pos)
    screen.blit(instructions, instructions_rect)

    options = font.render("Press O for options", True, WHITE)  # Updated text
    options_rect = options.get_rect(center=options_pos)
    screen.blit(options, options_rect)

def title_screen(screen, WIDTH, HEIGHT, clock):
    running = True
    while running:
        screen.fill(BLACK)

        title_pos = (WIDTH // 2, HEIGHT // 2 - 50)
        instructions_pos = (WIDTH // 2, HEIGHT // 2)
        options_pos = (WIDTH // 2, HEIGHT // 2 + 50)
        font_size = 36

        draw_title_screen(screen, title_pos, instructions_pos, options_pos, font_size)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_o:  # Keybind for the Options screen
                    new_size = options_screen(screen, WIDTH, HEIGHT, clock)
                    if new_size != (WIDTH, HEIGHT):
                        screen = pygame.display.set_mode(new_size)  # Update the resolution
                        WIDTH, HEIGHT = new_size  # Update the width and height

        clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    title_screen(screen, WIDTH, HEIGHT, clock)
