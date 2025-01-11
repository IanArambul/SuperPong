# import pygame to actually make our game
import pygame

# initialize our game
pygame.init()

# set screen dimensions, will possibly make this resizeable later
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# create player's character
player = pygame.Rect((250, 200, 50, 50))

# create game loop to keep game running continuously
running = True
while running:

    # set a screen color to keep refreshing background
    screen.fill((0, 0, 0))

    # set our player within the game, this will be updated to multiplayer later, with constraints
    pygame.draw.rect(screen, (0, 255, 0), player)

    # set up keys to move player
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] == True:
        player.move_ip(0, -10)
    elif key[pygame.K_DOWN] == True:
        player.move_ip(0, 10)
    

    # loop for event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # refresh game window
    pygame.display.update()

# close window if loop is ended by user closing exiting window
pygame.quit()            


# set framerate
clock = pygame.time.Clock()
