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
        self.bodies.append(Body(300, 200, 10, 10, color = (255, 255, 255)))
        self.bodies.append(Body(400, 200, 10, 10, color = (255, 255, 255)))

        self.mainLoop()

    def mainLoop(self):
        while (self.running):
            self.handle_events() # determines if the program should be terminated or not
            self.update() # updates the physics of the program
            self.render() # draws the updated physics
            self.clock.tick(60)
        self.quit()
    
    def handle_events(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                self.running = False
    
    def update(self): # updates the physics of the program
        for body in self.bodies:
            body.update()

    def render(self): # draw the updated physics
        self.screen.fill((0, 0, 0))
        for body in self.bodies:
            body.draw(self.screen)
        pg.display.flip()

    def quit(self):
        pg.quit()