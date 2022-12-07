import tkinter as tk
from car import Car

root = tk.Tk()
root.geometry("700x700")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)
#
bai = 50
size = 3
yoko = 0
tate = 300
color = "Blue"
direction = 1      # 右向き
car = Car(size, 100, 100, color)
car.create_car(canvas)

def key_event(e):
    key = e.keysym
    x, y = 0, 0
    if key == "Up":
        y = -10
    if key == "Down":
        y = 10
    if key == "Left":
        x = -10
    if key == "Right":
        x = 10

    car.move(canvas, x, y)
root.bind("<KeyPress>", key_event)

root.mainloop()
    #root.update()