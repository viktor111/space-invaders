import pygame

pygame.init()

icon = pygame.image.load("spaceship.png")

screen = pygame.display.set_mode((1000, 700))
display = pygame.display

display.set_caption("Space Invaders")
display.set_icon(icon)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,0,0))
    display.update()