import tkinter as tk

import car
from car import Car
from cannon import Cannon

root = tk.Tk()
root.geometry("900x700")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

cannon = Cannon(340, 750, 300, 800, 'GREEN')
cannon.create_cannon(canvas)

root.mainloop()