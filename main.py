import pygame
import random

pygame.init()

icon = pygame.image.load("spaceship.png")
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("alien.png")
background_img = pygame.image.load("background.png")
bullet_img = pygame.image.load("bullet.png")

WIDTH = 800
HIEGHT = 600

screen = pygame.display.set_mode((WIDTH, HIEGHT))
display = pygame.display

display.set_caption("Space Invaders")
display.set_icon(icon)

enemy_x = random.randint(0, 800) 
enemy_y = random.randint(45, 150)
enemy_change_x = 2 
enemy_change_y = 4

bullet_x = 0
bullet_y = 480
bullet_change_x = 0 
bullet_change_y = 10
bullet_state = "ready"

player_x = 370
player_y = 480
player_change_x = 0

def fire_bullet(x,y):
    global bullet_state 
    bullet_state = "fire"
    screen.blit(bullet_img,(x+16, y + 10))

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y):
    screen.blit(enemy_img, (x, y))

running = True
while running:

    screen.fill((0,0,0))
    screen.blit(background_img, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change_x = -3.5
                print("<")
            if event.key == pygame.K_SPACE:
                print("space")
                fire_bullet(player_x, bullet_y)

            if event.key == pygame.K_RIGHT:
                player_change_x = 3.5
                print(">")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                print("release key") 
                player_change_x = 0
                
    player_x += player_change_x
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    enemy_x += enemy_change_x
    if enemy_x <= 0:
        enemy_y += enemy_change_y
        enemy_change_x = 2
    elif enemy_x >= 736:
        enemy_y += enemy_change_y
        enemy_change_x = -2

    if bullet_state is "fire":
        fire_bullet(player_x,bullet_y)
        bullet_y -= bullet_change_y
        
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    display.update()
