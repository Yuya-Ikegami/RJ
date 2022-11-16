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
#         canvas.create_rectangle(5*size+bai*yoko, 10*size+bai*tate, 20*size+bai*yoko, 15*size+bai*tate, fill = color)
# #
#         canvas.create_rectangle(10*size+bai*yoko, 7*size+bai*tate, 15*size+bai*yoko, 10*size+bai*tate, fill = color)
# # タイヤの描画
#         canvas.create_oval(9*size+bai*yoko, 15*size+bai*tate, 11*size+bai*yoko, 17*size+bai*tate, fill = "black")
#         canvas.create_oval(14*size+bai*yoko, 15*size+bai*tate, 16*size+bai*yoko, 17*size+bai*tate, fill = "black")
        car = Car(size, bai*yoko, bai*tate, color)
        car.create_car(canvas)

root.mainloop()


