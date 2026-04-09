import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    # Initialize pygame
    pygame.init()

    # Create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        # Log game state
        log_state()

        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draw (fill screen black)
        screen.fill("black")

        # Refresh display (MUST be last)
        pygame.display.flip()


if __name__ == "__main__":
    main()