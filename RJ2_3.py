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
result = 0

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

while result == 0:
    try:
        val = input("Where car do you hide? :")
        if int(val) >= 0 and int(val) <= 99:
            val1 = int(val) // 10
            val2 = int(val) % 10
            result = 1
        else:
            print('0~99の数値を入力してください.')
    except:
        print('0~99の数値を入力してください.')

cars[val1][val2].delete(canvas)

root.mainloop()


