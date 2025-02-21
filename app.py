import pygame as pg
from body import Body

class App:

    def __init__(self, width, height, title="N-Body Simulator"):
        pg.init()
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.running = True

        self.bodies = []
        self.bodies.append(Body(200, 200, mass=10, radius=10, velocity_x=1, velocity_y=1, color=(255, 0, 0)))

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
            if (event.type == pg.QUIT):
                self.running = False
    
    def update(self):
        for body in self.bodies:
            body.update()

    def render(self):
        self.screen.fill((0, 0, 0))
        for body in self.bodies:
            body.draw(self.screen)
        pg.display.flip()

    def quit(self):
        pg.quit()