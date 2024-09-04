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
