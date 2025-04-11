import pygame
import sys
import config # Import the config Module
import random
import shapes


def init_game():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constanst from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True


def draw_text(screen,text,x,y,font_size,font_color,font_name = None,bold = False, italic = False):
    
    font = pygame.font.SysFont(None,font_size)
    image = font.render(text,True, font_color)
    screen.blit(image,(x,y))
    

def draw_rectangle(screen, color, x, y, width, height):
    pygame.draw.rect(screen,color,[x,y,width,height])

def main():
    screen = init_game()
    running = True
    clock = pygame.time.Clock() # Initialize the clock her
    color = config.PURPLE
    square_x = 10
    square_y = 20

    square_change_x = 1
    square_change_y = 1

    square_x = square_x + square_change_x
    square_y = square_y + square_change_y
    
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config
        text1 = "Abraham Lincoln"
        x1 = 75
        y1 = 100
        font_size1 = 48

        text2 = "Career Tech"
        x2 = 75
        y2 = 150
        font_size2 = 48

        text3 = "Animated Shape Ver 1.0"
        x3 = 75
        y3 = 200
        font_size3 = 48

        square_x = square_x + square_change_x
        square_y = square_y + square_change_y

        draw_text(screen, text1,x1,y1,font_size1,config.BLUE)
        draw_text(screen, text2,x2,y2,font_size2,config.RED)
        draw_text(screen, text3,x3,y3,font_size3,config.GREEN)
        draw_rectangle(screen,color,square_x,square_y, config.SQUARE_WIDTH,config.SQUARE_HEIGHT)

        pygame.display.flip()

        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()