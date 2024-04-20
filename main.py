import pygame
pygame.init()

from classes import Player_left, Player_right, Enemy

def game():
    win.fill((100, 100, 160))
    player_left.move()
    player_left.reset()
    player_right.move()
    player_right.reset()

def end_game():
    pass

win = pygame.display.set_mode((800, 600))
win.fill((25, 120, 22))
pygame.display.set_caption('                                                                                                            *__Ping-Pong__*')

player_left = Player_left('rocet11.png',750, 220, 25, 180, 10, win)
player_right = Player_right('rocet22.png',15, 220, 25, 180, 10, win)

run = True
finish = False
clock = pygame.time.Clock()

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    if not finish:
        game()
    else:
        end_game()

    pygame.display.update()
    clock.tick(120)