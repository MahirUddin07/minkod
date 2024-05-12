import pygame
import sys

pygame.init()

# Fixar window screen.
screen_width = 1280
screen_height = 660
screen = pygame.display.set_mode((screen_width, screen_height))

# Namn för spelet.
pygame.display.set_caption('2players Game')
clock = pygame.time.Clock()

# Positioner.
player1_x, player1_y = 50, 250
player2_x, player2_y = 1090, 250


def wrap_around(value, size):
    return value % size

def game_over_screen():
    game_over_font = pygame.font.Font(None, 64)
    game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
    screen.blit(game_over_text, (screen_width // 2 - 150, screen_height // 2 - 50))

    instruction_font = pygame.font.Font(None, 36)
    instruction_text = instruction_font.render("Press 'C' to play again or 'Q' to quit", True, (0, 0, 0))
    screen.blit(instruction_text, (screen_width // 2 - 250, screen_height // 2 + 50))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return True  # Play again

                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


def game_over():
    global player1_x, player1_y, player2_x, player2_y

    while True:
        if game_over_screen():
            # Reset player positions
            player1_x, player1_y = 50, 250
            player2_x, player2_y = 1090, 250
            return  # Play again
        else:
            pygame.quit()
            sys.exit()  # Quit


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # How to move. Applies to player1.
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player1_x -= 5
    if keys[pygame.K_d]:
        player1_x += 5
    if keys[pygame.K_w]:
        player1_y -= 5
    if keys[pygame.K_s]:
        player1_y += 5

    # How to move. Applies to player2.
    if keys[pygame.K_LEFT]:
        player2_x -= 5
    if keys[pygame.K_RIGHT]:
        player2_x += 5
    if keys[pygame.K_UP]:
        player2_y -= 5
    if keys[pygame.K_DOWN]:
        player2_y += 5

    # Keeping players within bounds.
    player1_x = wrap_around(player1_x, screen_width)
    player1_y = wrap_around(player1_y, screen_height)
    player2_x = wrap_around(player2_x, screen_width)
    player2_y = wrap_around(player2_y, screen_height)

    # Background for the game.
    screen.fill('white')

    # A rectangle around the players. Helps with collision detection.
    player1_rect = pygame.Rect(player1_x, player1_y, 150, 150)
    player2_rect = pygame.Rect(player2_x, player2_y, 150, 150)

    # Player 1
    player1_surface = pygame.image.load('player1.png')
    player1 = pygame.transform.scale(player1_surface, (150, 150))
    screen.blit(player1, (player1_x, player1_y))

    # Player 2
    player2_surface = pygame.image.load('player2.png')
    player2_surface = pygame.transform.flip(player2_surface, True, False)
    player2 = pygame.transform.scale(player2_surface, (150, 150))
    screen.blit(player2, (player2_x, player2_y))

    # Collision
    if player1_rect.colliderect(player2_rect):
        game_over()

    pygame.display.update()
    clock.tick(90)
