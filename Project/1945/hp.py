from gobj import *

class hp:
    def __init__(self, life):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = -20, 850
        self.life = life
        self.image = gfw.image.load(RES_DIR + '/Heart.png')
        self.fidx = 0
        self.src_width = self.image.w
        self.src_height = self.image.h
        self.time = 0
        # self.LR = 0 # 왼쪽으로 갈지 오른쪽으로 갈지. 1 Left, 2 Right

    def draw(self):
        for i in range(1, self.life + 1):
            sx = self.fidx * self.src_width
            self.image.draw(self.x + self.src_width * i, self.y)

    def update(self):
        pass
