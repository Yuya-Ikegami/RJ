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
cannon.delete(canvas)

#root.mainloop()
balls = []

def key_event(e):
    print("あ")
    key = e.keysym
    if key == "k":
        cannon = Cannon(380, 500, 340, 540, color, 400, 400)
        cannon.create_cannon(canvas)
        cannon.create_ball(canvas)
        balls.append(cannon)

root.bind("<KeyPress>", key_event)
while True:
    for i in balls:
        if i.y3 - 50 < 0:
            i.delete(canvas)
        else:
            yd = -1
            i.move_ball(canvas, 0, yd)

    root.update()