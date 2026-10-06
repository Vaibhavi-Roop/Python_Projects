import pygame
def main():
    pygame.init()
    screen_height, screen_width = (400, 500)
    screen = pygame.display.set_mode((screen_height, screen_width))
    pygame.display.set_caption("Rectangle Bounce")
    x, y = 50, 50
    sprite_width, sprite_height = 60, 60
    speed = 4
    PINK = (225, 153, 225)
    PURPLE = (178, 102, 225)    
    BLUE = (0, 204, 204)
    GREEN = (153, 225, 153)
    WHITE = (225, 225, 225)
    BLACK = (0,0,0 )
    current_colour = BLACK
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pressed = pygame.key.get_pressed()  
        if pressed [pygame.K_LEFT]:
            x -= speed
        if pressed [pygame.K_RIGHT]:
            x += speed
        if pressed [pygame.K_UP]:
            y -= speed
        if pressed [pygame.K_DOWN]:
            y += speed
        x = min(max(0, x), screen_width - sprite_width)            
        y = min(max(0, y), screen_height - sprite_height)            
        if x == 0:                                                          
            current_colour = PINK
        elif x == screen_width - sprite_width:
            current_colour = GREEN
        elif y == screen_height-sprite_height:
            current_colour = PURPLE
        elif y == 0:
            current_colour = BLUE
        else:
            current_sprite_colour = WHITE
        
        screen.fill(BLACK)
        rectangle = pygame.Rect(x, y, sprite_width, sprite_height)
        pygame.draw.rect(screen, current_colour, rectangle)
        pygame.display.flip()
        clock.tick(60)      
    pygame.quit()
if __name__ == "__main__":
    main()