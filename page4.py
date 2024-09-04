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
