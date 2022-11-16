import tkinter as tk

class Car:
    
    def __init__(self, size, x, y, color):
        self.size = size
        self.x = x
        self.y = y
        self.color = color

        self.top = None
        self.bottom = None
        self.tire1 = None
        self.tire2 = None
        
    def create_car(self, canvas: tk.Canvas):
        self.top = canvas.create_rectangle(5 * self.size + self.x, 10 * self.size + self.y, 20 * self.size + self.x,
                                15 * self.size + self.y, fill=self.color)
        #
        self.bottom = canvas.create_rectangle(10 * self.size + self.x, 7 * self.size + self.y, 15 * self.size + self.x,
                                10 * self.size + self.y, fill=self.color)
        # タイヤの描画
        self.tire1 = canvas.create_oval(9 * self.size +self.x, 15 * self.size +self.y, 11 * self.size + self.x,
                           17 * self.size +self.y, fill="black")
        self.tire2 = canvas.create_oval(14 * self.size +self.x, 15 * self.size +self.y, 16 * self.size + self.x,
                           17 * self.size +self.y, fill="black")

    def delete(self, canvas: tk.Canvas):
        canvas.delete(self.top)
        canvas.delete(self.bottom)
        canvas.delete(self.tire1)
        canvas.delete(self.tire2)