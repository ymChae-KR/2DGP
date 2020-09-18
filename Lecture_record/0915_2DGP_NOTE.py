from pico2d import *

def handle_events():
    global running
    global dx
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dx += 1

            elif event.key == SDLK_LEFT:
                dx -= 1

            elif event.key == SDLK_ESCAPE:
                running = False

            elif event.type == SDL_MOUSEMOTION:
                x, y = event.x, event.y

open_canvas()
gra = load_image('grass.png')
ch = load_image('character.png')
running = True
x = 400
dx = 0
fidx = 0

while running:
    clear_canvas()
    gra.draw(400, 30)
    update_canvas()
    handle_events()
    # frame = (frame+1) % 8

## 중간고사 시험문제 --
## 인캡슐레이션. 객체의 속성과 행위를 묶는 것.
## 객체르 찍어내는 과정을 Object instantication 이라 함. PDF에 있음