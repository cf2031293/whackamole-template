import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        # grid is 16x20
        mole_image = pygame.transform.scale(pygame.image.load("mole.png"), (35, 35))
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_rect = mole_image.get_rect(topleft=(0, 0))

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill("light green")

            indv_width = screen.get_width() / 20
            indv_height = screen.get_height() / 16

            screen.blit(mole_image, mole_rect)

            for x in range(1, 21):
                pygame.draw.line(screen, (0, 0, 0), (x * indv_width, 0), (x * indv_width, screen.get_height()))

            for y in range(1, 17):
                pygame.draw.line(screen, (0, 0, 0), (0, y * indv_height), (screen.get_width(), y * indv_height))

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                # print("Mouse clicked at:", mouse_pos)

                if (mole_rect.x <= mouse_pos[0] <= mole_rect.x + indv_width and mole_rect.y <= mouse_pos[1] <=
                        mole_rect.y + indv_height):
                    x_position = random.randrange(0, 20)
                    y_position = random.randrange(0, 16)
                    mole_rect = mole_image.get_rect(topleft=(x_position * indv_width, y_position * indv_height))

            pygame.display.flip()
            clock.tick(30)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
