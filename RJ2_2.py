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
for tate in range(10):
    for yoko in range(10):
# 長方形の描画
        if (yoko+tate) % 2 == 0:
            color = "Red"
        else:
            color = "Blue"
        car = Car(size, bai*yoko, bai*tate, color)
        car.create_car(canvas)

root.mainloop()


