#go this site https//pixabay.com and import image.


#creating the ship image

import pygame
class ship:
    #a class to mannnage the ship.
def_init_(self,ai_game): # type: ignore
#initialize the ship and set itsstarting position

self.screen=ai_game.screen # type: ignore
self.screen_rect=ai_game.screen.get_rect() # type: ignore
#load the ship impend get it rect.
self.image =pygame.image.load("images/ship.bmp") # type: ignore
self.rect=self.image.get_rect() # type: ignore
#start each new .ship at the bottomcenter or the screen.
self.rect.midbottom=self.screen_rect.midbottom # type: ignore
def.blitme(self): # type: ignore
#draw the shipat this current location.
self.screen blit(self.image,self.rect) # type: ignore