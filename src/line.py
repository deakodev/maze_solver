from tkinter import Canvas

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start: Point, end: Point):
        self.__start = start
        self.__end = end

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.__start.x, self.__start.y,
            self.__end.x, self.__end.y,
            fill=fill_color, width=2.5
        )
