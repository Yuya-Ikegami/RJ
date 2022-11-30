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
# root.update()
# root.mainloop()

while True:
    if car.x+100>=700:
        direction = -1
    elif car.x-50<=0:
        direction = 1
    # if direction == 0:
    #     car.x = car.x + 10
    # else:
    #     car.x = car.x - 10
    car.move(canvas, direction*10, 0)

    root.update()

