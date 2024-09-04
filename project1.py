import sys
import pygame
class alien_invasion:
    #overal lclass to  manage assest and behavioe.
     def init(self): # type: ignore
#initialize the game ,and create game resorse.
        pygame.init()
Self.screen=pygame.display.set__mode((1200,800)) #pygame.display.set caption("alienInvasion")# type: ignore
def run_game(self):
    #start the main loop for game.
    while True:
        #watch for keyboard and mouse event.
        for event in pygame.event.get():
            sys.exit()
    #makethe most recently drawn screen visible.
pygame.display.flip()
if_name_=="__main__": # type: ignore
#make a game instance ,and run the game.
ai.alienInvasion # type: ignore
ai.run_game(): # type: ignore


#--------------------------------------------

def_init_(self): # type: ignore
pygame.display.set_caption("alien invasion") # type: ignore
#set the background color.
self.bg_color=(230,230,230) # type: ignore
def run_game(self):
    for event in pygame.event .get(): # type: ignore
        if event.type==pygame.QUIT: # type: ignore
            sys.exit() # type: ignore
            #redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)
            #make the most recently drawn screen visible.
            pygame.display.flip() # type: ignore


#----------------------------------------------------

class setting:
    #a class to store all settingfor alienInvasion.
    def_init_(self): # type: ignore
    #initialize the game settings.
    #screeen setting
    self.screen_width=1200 # type: ignore
    self.screen_height=800 # type: ignore
    self.bg_color=(230,230,230) # type: ignore

    #--------------------------------------------------------

    import pygame
    from setting import setting # type: ignore
    class alienInvasion:
        #overall class to manage game assest and behaviour.
        def_init_(self): # type: ignore
        #intilize thegame,and create the resourses.
    
    pygame.init()
self.setting=setting() # type: ignore
self.screen=pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height)) # type: ignore
pygame.display.set_caption("alienInvasion")
def run_game_(self):
    #redraw the screen during each pass through the loop.
    self.screen.fill(self.setting.bg_color)
    #make the recently drawn screen visible.
    pygame.display.flip()


#-------------------------------------------

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






 
