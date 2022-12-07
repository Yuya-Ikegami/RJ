import tkinter as tk

class Cannon:
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

        self.top = None
        self.bottom = None

    def create_cannon(self, canvas: tk.Canvas):
        self.top = canvas.create_rectangle(self.x1, self.y1, self.x1+40, self.y1+50, fill=self.color)
        self.bottom = canvas.create_rectangle(self.x2, self.y2, self.x2+120, self.y2+50, fill=self.color)

    def create_ball(self, canvas: tk.Canvas):