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

val = input("Where car do you hide? [1] :")
val1 = int(val)
val = input("Where car do you hide? [2] :")
val2 = int(val)
cars[val1][val2].delete(canvas)

root.mainloop()


