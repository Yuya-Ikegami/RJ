import tkinter as tk
import math
from car import Car
from cannon import Cannon

root = tk.Tk()
root.geometry("900x700")
color = "GREEN"

# Canvasの作成
canvas = tk.Canvas(root, bg="white")
# Canvasを配置
canvas.pack(fill=tk.BOTH, expand=True)

size = 3
color = "Blue"
direction = 1.5      # 右向き
car = Car(size, 100, 100, color)
car.create_car(canvas)

cannon = Cannon(380, 500, 340, 540, color, 400, 400)

cannon.create_cannon(canvas)
cannon.create_ball(canvas)
cannon.delete(canvas)

#root.mainloop()
balls = []

def key_event(e):
    #print("あ")
    key = e.keysym
    if key == "k":
        cannon = Cannon(380, 500, 340, 540, color, 400, 400)
        cannon.create_cannon(canvas)
        cannon.create_ball(canvas)
        balls.append(cannon)

root.bind("<KeyPress>", key_event)

while True:
    if car.x+100>=900:
        direction = -1.5
    elif car.x-50<=0:
        direction = 1.5

    car.move(canvas, direction, 0)

    for i in balls:
        #車の中心座標
        carx = car.x + 22.5
        cary = car.y + 37.5
        #ボールの中心座標
        ballx = i.x3 + 5
        bally = i.y3 + 5

        dist = math.sqrt(((carx - ballx) * (carx - ballx)) + ((cary - bally) * (cary - bally)))
        if 0 <= dist <= 10:
            car.move(canvas, -1 * car.x, 0)

        if i.y3 - 50 < 0:
            i.delete(canvas)
        else:
            yd = -1
            i.move_ball(canvas, 0, yd)

    root.update()