import tkinter as tk

root = tk.Tk()
root.geometry("500x400")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

# 長方形の描画
canvas.create_rectangle(100, 80, 400, 320, fill = "Black", width = 5)

root.mainloop()
