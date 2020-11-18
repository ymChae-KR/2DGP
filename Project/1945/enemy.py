from pico2d import *
import gfw
from gobj import *
import life_gauge
import effect
import math

class Enemy:
    SIZE = 24
    def __init__(self, x, speed, level, pX = 360):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, get_canvas_height() + Enemy.SIZE
        self.dx, self.dy = 0, speed
        self.level = level
        self.max_life = level * 100
        self.life = self.max_life
        self.image = gfw.image.load(RES_DIR + '/몬스터1.png')
        self.fidx = 0
        self.src_width = self.image.w // 11
        self.src_height = self.image.h
        self.time = 0
        #self.LR = 0 # 왼쪽으로 갈지 오른쪽으로 갈지. 1 Left, 2 Right
        self.Movement(pX)


    def draw(self):
        sx = self.fidx * self.src_width
        self.image.clip_draw(sx, 0, self.src_width, self.src_height, self.x, self.y)
        gy = self.y - Enemy.SIZE // 2
        rate = self.life / self.max_life
        life_gauge.draw(self.x, gy, Enemy.SIZE - 10, rate)

    def update(self):
        self.time += gfw.delta_time
        self.fidx = int(self.time * 10 + 0.5) % 11
        self.x += self.dx
        self.y += self.dy * gfw.delta_time

        if self.y < -Enemy.SIZE:
            self.remove()

    def remove(self):
        e = effect.paritcle(self.x,self.y)
        gfw.world.add(gfw.layer.particle, e)
        gfw.world.remove(self)

    def decrease_life(self, amount):
        self.life -= amount
        return self.life <= 0

    def score(self):
        return self.max_life

    def get_bb(self):
        half = Enemy.SIZE // 2 - 5
        return self.x - half, self.y - half, self.x + half, self.y + half

    def Movement(self, x):
        if self.x < x:
            self.dx = 2
        elif self.x > x:
            self.dx = -2
