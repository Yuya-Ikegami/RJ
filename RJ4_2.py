import tkinter as tk
from cannon import Cannon

root = tk.Tk()
root.geometry("900x700")
color = "GREEN"

# Canvasの作成
canvas = tk.Canvas(root, bg="white")
# Canvasを配置
canvas.pack(fill=tk.BOTH, expand=True)

#cannon = Cannon(340, 750, 300, 800, color, 400, 400)
cannon = Cannon(380, 500, 340, 540, color, 400, 400)

cannon.create_cannon(canvas)
cannon.create_ball(canvas)

#root.mainloop()
balls = []

def key_event(e):
    key = e.keysym
    if key == "k":
        y = -10

while True:
    if cannon.y3-50 < 0:
        yd = 350
    else :
        yd = -1
    cannon.move_ball(canvas, 0, yd)
    root.bind("<KeyPress>", key_event)

    root.update()