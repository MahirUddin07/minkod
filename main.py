import pygame

pygame.init()

#Fixar window screen.
screen_width = 1280
screen_height = 660
screen = pygame.display.set_mode((screen_width, screen_height))

#Namn för spelet.
pygame.display.set_caption('2players Game')
clock = pygame.time.Clock()

#Positioner.
player1_x, player1_y = 50, 250
player2_x, player2_y = 1090, 250

def wrap_around(value, size): #Bestämmer gränsen för x och y.
    return value % size

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

#Hur man rör sig. Gäller för player1.
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player1_x -= 5
    if keys[pygame.K_d]:
        player1_x += 5
    if keys[pygame.K_w]:
        player1_y -= 5
    if keys[pygame.K_s]:
        player1_y += 5

# Hur man rör sig. Gäller för player2.
    if keys[pygame.K_LEFT]:
        player2_x -= 5
    if keys[pygame.K_RIGHT]:
        player2_x += 5
    if keys[pygame.K_UP]:
        player2_y -= 5
    if keys[pygame.K_DOWN]:
        player2_y += 5

#Gränsen.
    player1_x = wrap_around(player1_x, screen_width)
    player1_y = wrap_around(player1_y, screen_height)
    player2_x = wrap_around(player2_x, screen_width)
    player2_y = wrap_around(player2_y, screen_height)

#Bakrunden för spelet.
    screen.fill('white')

#En rektangel som är runt spelarna. Hjälper koden kollision.
    player1_rect = pygame.Rect(player1_x, player1_y, 150, 150)
    player2_rect = pygame.Rect(player2_x, player2_y, 150, 150)

#Player 1
    player1_surface = pygame.image.load('player1.png')
    player1 = pygame.transform.scale(player1_surface, (150, 150))
    screen.blit(player1, (player1_x, player1_y))

#Player 2
    player2_surface = pygame.image.load('player2.png')
    player2_surface = pygame.transform.flip(player2_surface, True, False)
    player2 = pygame.transform.scale(player2_surface, (150, 150))
    screen.blit(player2, (player2_x, player2_y))

#Kollision
    if player1_rect.colliderect(player2_rect):
        break

    pygame.display.update()
    clock.tick(90)

