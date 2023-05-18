import pygame

# Options
RESOLUTIONS = [(800, 600), (1024, 768), (1280, 720), (1920, 1080)]
MASTER_VOLUME_OPTIONS = [0, 25, 50, 75, 100]
SFX_VOLUME_OPTIONS = [0, 25, 50, 75, 100]
MUSIC_VOLUME_OPTIONS = [0, 25, 50, 75, 100]

OPTIONS = [
    ("Resolution", RESOLUTIONS),
    ("Master Volume", MASTER_VOLUME_OPTIONS),
    ("SFX", SFX_VOLUME_OPTIONS),
    ("Music", MUSIC_VOLUME_OPTIONS)
]

def options_screen(screen, WIDTH, HEIGHT, clock):
    font = pygame.font.Font(None, 36)
    current_option = 0
    running = True

    while running:
        screen.fill((0, 0, 0))

        for index, option in enumerate(OPTIONS):
            if index == current_option:
                color = (255, 0, 0)
            else:
                color = (255, 255, 255)

            option_text = font.render(f"{option[0]}: {option[1][index]}", True, color)
            option_rect = option_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + index * 50))
            screen.blit(option_text, option_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                elif event.key == pygame.K_UP:
                    current_option = (current_option - 1) % len(OPTIONS)
                elif event.key == pygame.K_DOWN:
                    current_option = (current_option + 1) % len(OPTIONS)
                elif event.key == pygame.K_ESCAPE:
                    running = False

        clock.tick(60)

    return OPTIONS[0][1][current_option]  # Return the new resolution
