import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('First Game!')

WHITE = (255, 255, 255)

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 5, 4

BLUE_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('C:\python\pygame', 'BLUE_spaceship.png'))
BLUE_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(BLUE_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('C:\python\pygame', 'RED_spaceship.png'))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

def draw_window() :
    WIN.fill(WHITE)
    WIN.blit(BLUE_SPACESHIP_IMAGE, (300,100))
    pygame.display.update()


def main() :
    clock = pygame.time.Clock()
    run = True
    while run :
        clock.tick(FPS)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
        
        draw_window()
     

    pygame.quit()

if __name__ == '__main__' :
    main()