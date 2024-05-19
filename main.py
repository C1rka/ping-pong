import pygame
pygame.init()

from classes import Player_left, Player_right, Enemy

def game():
    win.fill((100, 100, 160))
    player_left.move()
    player_left.reset()
    player_right.move()
    player_right.reset()
    enemy.reset()

def end_game():
    pass

win = pygame.display.set_mode((800, 600))
win.fill((25, 120, 22))
pygame.display.set_caption('                                                                                                            *__Ping-Pong__*')

player_left = Player_left('rocet11.png',750, 220, 25, 180, 10, win)
player_right = Player_right('rocet22.png',15, 220, 25, 180, 10, win)
enemy = Enemy('rocet11.png',400, 400, 25, 25, 7, win)
font1 = pygame.font.SysFont('arial', 35)
lose1 = font1.render('Player Left lose, Player Right Win', True, (255,0,0))
lose2 = font1.render('Player Right lose, Player Left Win', True, (0,255,0))

run = True
finish = False
clock = pygame.time.Clock()
enemy_x = 3
enemy_y = 3

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    if not finish:
        game()
        enemy.rect.x += enemy_x
        enemy.rect.y += enemy_y
        if enemy.rect.y >= 575:
            enemy_y *= -1
        if enemy.rect.y <= 0:
            enemy_y *= -1
        if pygame.sprite.collide_rect(player_left, enemy) or pygame.sprite.collide_rect(player_right, enemy):
            enemy_x *= -1
        if enemy.rect.x >= 775:
            win.blit(lose2, (200, 300))
            finish = True
        if enemy.rect.x <= 0:
            win.blit(lose1, (200, 300))
            finish = True
    else:
        end_game()

    pygame.display.update()
    clock.tick(120)
