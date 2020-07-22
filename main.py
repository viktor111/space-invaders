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

player_change_x = 0

def player(x, y):
    screen.blit(player_img, (x, y))

running = True
while running:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change_x = -2.7
                print("<")

            if event.key == pygame.K_RIGHT:
                player_change_x = 2.7
                print(">")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
               print("release key") 

    player_x += player_change_x
    player(player_x, player_y)
    display.update()
