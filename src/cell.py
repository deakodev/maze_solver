from enum import Enum
from line import Line, Point
from window import Window

class Wall(Enum):
    Left = "left"
    Right = "right"
    Top = "top"
    Bottom = "bottom"

def default_walls() -> set[Wall]:
    return set([Wall.Left, Wall.Right, Wall.Top, Wall.Bottom])

class Cell:
    def __init__(self, window: Window, upper_left: Point, lower_right: Point, walls: set[Wall] = default_walls()) -> None:
        self.__window = window
        self.__upper_left = upper_left
        self.__lower_right = lower_right
        self.walls = walls

    def draw(self):
        for wall in self.walls:
            match wall:
                case Wall.Left:
                    start = self.__upper_left
                    end = Point(self.__upper_left.x, self.__lower_right.y)
                case wall.Right:
                    start = self.__lower_right
                    end = Point(self.__lower_right.x, self.__upper_left.y)
                case Wall.Top:
                    start = self.__upper_left
                    end = Point(self.__lower_right.x, self.__upper_left.y)
                case Wall.Bottom:
                    start = self.__lower_right
                    end = Point(self.__upper_left.x, self.__lower_right.y)
            line = Line(start, end)
            self.__window.draw_line(line, "black")

    def draw_path(self, to_cell, undo=False):
        if to_cell is None:
            return
        start = Point((self.__upper_left.x + self.__lower_right.x) / 2, (self.__upper_left.y + self.__lower_right.y) / 2)
        end = Point((to_cell.__upper_left.x + to_cell.__lower_right.x) / 2, (to_cell.__upper_left.y + to_cell.__lower_right.y) / 2)
        line = Line(start, end)
        self.__window.draw_line(line, "red" if undo else "gray")