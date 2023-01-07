import tkinter as tk

class Cannon:

    def __init__(self, x1, y1, x2, y2, color, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.x3 = x3
        self.y3 = y3

        self.top2 = None
        self.bottom2 = None
        self.ball2 = None

    def create_cannon(self, canvas: tk.Canvas):
        self.top2 = canvas.create_rectangle(self.x1, self.y1, self.x1+50, self.y1+40, fill = "GREEN")
        self.bottom2 = canvas.create_rectangle(self.x2, self.y2, self.x2+130, self.y2+40, fill = "GREEN")

    def create_ball(self, canvas: tk.Canvas):
        self.ball2 = canvas.create_oval(self.x3, self.y3, self.x3+10, self.y3+10, fill = "BLACK")

    def move_ball(self, canvas: tk.Canvas, x, y):
        self.y3 += y
        canvas.move(self.ball2, x, y)

    def delete(self, canvas: tk.Canvas):
        canvas.delete(self.ball2)

"""
class Ball:

    def __init__(self, x3, y3):
        self.x3 = x3
        self.y3 = y3
        self.ball2 = None

    def create_ball(self, canvas: tk.Canvas):
        self.ball2 = canvas.create_oval(self.x3, self.y3, self.x3+10, self.y3+10, fill = "BLACK")

    def move_ball(self, canvas: tk.Canvas, x, y):
        self.y3 += y
        canvas.move(self.ball2, x, y)
"""