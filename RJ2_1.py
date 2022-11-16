import tkinter as tk

root = tk.Tk()
root.geometry("500x400")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)
#
for num in range(3):
# 長方形の描画
    if num % 2 == 0:
        color = "Red"
    else:
        color = "Blue"
    canvas.create_rectangle(50*(num+1), 100*(num+1), 200*(num+1), 150*(num+1), fill = color)
#
    canvas.create_rectangle(100*(num+1), 70*(num+1), 150*(num+1), 100*(num+1), fill = color)
# タイヤの描画
    canvas.create_oval(90*(num+1), 150*(num+1), 110*(num+1), 170*(num+1), fill = "black")
    canvas.create_oval(140*(num+1), 150*(num+1), 160*(num+1), 170*(num+1), fill = "black")

root.mainloop()