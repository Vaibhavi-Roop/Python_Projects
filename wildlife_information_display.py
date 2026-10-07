import pygame 
pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tiger Information Display') 
background = pygame.transform.scale(pygame.image.load('background.jpg').convert(),(screen_width, screen_height))
tiger = pygame.transform.scale(pygame.image.load('tiger.jpg').convert_alpha(),(220, 220))
tiger_position = tiger.get_rect(center=(screen_width // 2, screen_height // 2 - 30))
heading_font = pygame.font.Font('freesansbold.ttf', 42)
heading_text = heading_font.render("Wildlife Spotlight Tiger", True, pygame.Color('black'))
heading_text_postion = heading_text.get_rect(center=(screen_width // 2, 45))
information_font =  pygame.font.Font('freesansbold.ttf', 26)
information_text = information_font.render("Tigers are the largest cats in the world!", True, pygame.Color('black'))
information_text_position = information_text.get_rect(center=(screen_width // 2, 420))
def game_loop():
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background, (0, 0))
        screen.blit(tiger, tiger_position)
        screen.blit(heading_text, heading_text_postion)
        screen.blit(information_text, information_text_position)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == "__main__":
    game_loop()