import tkinter as tk

root = tk.Tk()
root.geometry("500x400")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)
#
# 長方形の描画
canvas.create_rectangle(50, 100, 200, 150, fill = "Black")
# 
canvas.create_rectangle(100, 70, 150, 100, fill = "Black")
#
canvas.create_oval(90, 150, 110, 170, fill = "Black")
canvas.create_oval(140, 150, 160, 170, fill = "Black")

canvas.create_text(120, 200, text="Yuya Ikegami", font=("", 20))

root.mainloop()
