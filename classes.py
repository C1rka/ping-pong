import pygame
pygame.init()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, w , h,  player_speed, win):
        super().__init__()
        self.win = win
        self.image = pygame.transform.scale(pygame.image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        self.win.blit(self.image, (self.rect.x, self.rect.y))

class Player_left(GameSprite):
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[pygame.K_s] and self.rect.x < width - size:
            self.rect.x += self.speed

class Player_right(GameSprite):
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[pygame.K_DOWN] and self.rect.x < width - size:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed