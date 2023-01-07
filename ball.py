import tkinter as tk

class Ball:

    def __init__(self, x3, y3):
        self.x3 = x3
        self.y3 = y3
        self.ball2 = None

    def create_ball2(self, canvas: tk.Canvas):
        self.ball2 = canvas.create_oval(self.x3, self.y3, self.x3+10, self.y3+10, fill = "BLACK")

    def move_ball2(self, canvas: tk.Canvas, x, y):
        self.y3 += y
        canvas.move(self.ball2, x, y)

    def ball_delete(self, canvas: tk.Canvas):
        canvas.delete(self.ball2)