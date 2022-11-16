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

cars = []

for tate in range(10):
    c = []
    for yoko in range(10):
# 長方形の描画
        if (yoko+tate) % 2 == 0:
            color = "Red"
        else:
            color = "Blue"
        car = Car(size, bai * yoko, bai * tate, color)
        car.create_car(canvas)
        c.append(car)
    cars.append(c)

print("消したい車の位置を入力して下さい")
cars[4][5].delete(canvas)

root.mainloop()


