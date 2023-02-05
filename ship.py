import pygame
from settings import Settings
from pygame.sprite import Sprite

class Ship(Sprite):
    #A class to manage ship

    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings=ai_game.settings

        #load the ship to get its rect
        self.image=pygame.image.load('rocket.bmp')
        self.rect=self.image.get_rect()

        #start each new ship at the center of buttom of screen
        self.rect.midbottom=self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x=float(self.rect.x)
        #movement flag
        self.moving_right=False
        self.moving_left=False

    def update(self):
        #update the ship's x value rather than rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x-=self.settings.ship_speed  
        #update rect object from self.x
        self.rect.x=self.x      

    def blitme(self):
        #draw ship at curent location
        self.screen.blit(self.image,self.rect) 

    def center_ship(self):
        #center the ship on the screen
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)     
