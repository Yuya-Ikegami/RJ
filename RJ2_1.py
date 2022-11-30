import tkinter as tk
from car import Car

root = tk.Tk()
root.geometry("500x400")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)
#
bai = 50
size = 3

for num in range(2):
# 長方形の描画
    if num % 2 == 0:
        color = "Red"
    else:
        color = "Blue"
    car = Car(size, bai * num, bai * num, color)
    car.create_car(canvas)
    size = size * 2

root.mainloop()