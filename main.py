import pygame

pygame.init()

icon = pygame.image.load("spaceship.png")
player_img = pygame.image.load("player.png")

screen = pygame.display.set_mode((1000, 800))
display = pygame.display

display.set_caption("Space Invaders")
display.set_icon(icon)

player_x = 480
player_y = 634

def player():
    screen.blit(player_img, (player_x, player_y))

running = True
while running:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    display.update()