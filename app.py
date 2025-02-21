import pygame as pg

class App:

    def __init__(self, width, height, title="N-Body Simulator"):
        pg.init()
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.running = True
        self.mainLoop()

    def mainLoop(self):
        while (self.running):
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
        self.quit()
    
    def handle_events(self):
        for event in pg.event.get():
            if(event.type == pg.QUIT):
                self.running = False
    
    def update(self):
        # update physics + game logic
        pass

    def render(self):
        self.screen.fill((0, 0, 0))
        pg.display.flip()

    def quit(self):
        pg.quit()