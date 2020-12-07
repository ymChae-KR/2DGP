from gobj import *

class paritcle:
    def __init__(self, x, y, iX = 30, iY = 27 ):
        self.x, self.y = x, y
        self.image = gfw.image.load(RES_DIR + '/Effect1-1-cutout1.png')
        self.width = self.image.w // 12
        self.height = self.image.h
        self.fidx = 0
        self.time = 0
        self.timer = 0

    def draw(self):
        sx = self.fidx * self.width
        self.image.clip_draw(sx, 0, self.width, self.height, self.x, self.y)

    def update(self):
        self.time += gfw.delta_time
        self.timer += 1
        self.fidx = int(self.time * 10 + 0.5) % 12
        #self.x += self.dx
        #self.y += self.dy * gfw.delta_time

        if self.timer == 80:
            self.remove()

    def remove(self):
        gfw.world.remove(self)
