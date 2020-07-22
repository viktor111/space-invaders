import pygame

pygame.init()

icon = pygame.image.load("spaceship.png")
player_img = pygame.image.load("player.png")

WIDTH = 800
HIEGHT = 600

screen = pygame.display.set_mode((WIDTH, HIEGHT))
display = pygame.display

display.set_caption("Space Invaders")
display.set_icon(icon)

player_x = 370
player_y = 480

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
