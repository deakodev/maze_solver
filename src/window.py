from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__running = False
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        print(f"Initializing window... ({width}, {height})")

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self) -> None:
        self.__running = False
        print(f"Closing window...")

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.__canvas, fill_color)