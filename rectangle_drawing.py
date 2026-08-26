import pygame
pygame.init()
screen = pygame.display.set_mode((400, 500))
screen.fill((6, 191, 213))
purple = (135, 0, 170)
pygame.draw.circle(screen, purple, (100, 300), 50)
pygame.draw.circle(screen, purple, (300, 300), 50, 3)
pygame.draw.rect(screen, (135, 0, 170), pygame.Rect(30, 30, 60, 60))
pygame.display.update()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



