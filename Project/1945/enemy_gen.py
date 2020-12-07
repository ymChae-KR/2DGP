import random
import gfw
from pico2d import *
from enemy import Enemy
from enemy import middleEnemy
from enemy import *

GEN_X = [ 50, 150, 250, 350, 450, 550, 650 ]
GEN_X2 =[ 100, 200, 300, 400, 500, 600, 700]
next_wave = 0
wave_index = 0

def update():
    global next_wave
    next_wave -= gfw.delta_time
    if next_wave < 0:
        generate_wave()

def generate_wave():
    global wave_index, next_wave
    for x in GEN_X:
        level = enemy_level()
        speed = -(100 + 5 * wave_index)

    for i in range(0,int(wave_index * 1.5)):
        x = random.uniform(0,700)
        speed = -(100 + 5 * wave_index)
        e = redEnemy(x, speed, level)
        gfw.world.add(gfw.layer.enemy, e)
        e = Enemy(x, speed, level)
        me = middleEnemy(x, speed, level)
        gfw.world.add(gfw.layer.enemy, e)
        gfw.world.add(gfw.layer.enemy, me)

        if wave_index % 3 == 0:
            semiB = SemiBoss(x, speed, level)
            gfw.world.add(gfw.layer.enemy, semiB)

    if wave_index == 0:
        b = Boss(x, speed, level)
        #gfw.world.add(gfw.layer.enemy, b)

    wave_index += 1
    next_wave = random.uniform(5, 10)

LEVEL_ADJUST_PERCENTS = [ 10, 15, 15, 40, 15, 5 ] # -3 ~ 2
def enemy_level():
    level = (wave_index - 5) // 10 - 3;
    percent = random.randrange(100)
    pl = level
    pp = percent
    for p in LEVEL_ADJUST_PERCENTS:
        if percent < p: break
        percent -= p
        level += 1
    # print(pl, '->', level, ', ', pp, '->', percent)
    if level < 1: level = 1
    if level > 20: level = 20
    return level

