from line import Line, Point

WALL_MAP = {
    "left":   lambda ul, lr: (ul, Point(ul.x, lr.y)),
    "right":  lambda ul, lr: (lr, Point(lr.x, ul.y)),
    "top":    lambda ul, lr: (ul, Point(lr.x, ul.y)),
    "bottom": lambda ul, lr: (lr, Point(ul.x, lr.y)),  
}

class Cell:
    def __init__(self, upper_left: Point, lower_right: Point, window = None) -> None:
        self.__window = window
        self.__upper_left = upper_left
        self.__lower_right = lower_right
        self.__visible_walls = { "left": True, "right": True, "top": True, "bottom": True }
        self.visited = False

    def draw(self):
        if self.__window is None:
            return
        for wall in WALL_MAP.keys():
            self.draw_wall(wall, True)

    def draw_path(self, to_cell: "Cell", undo = False):
        if to_cell is None or self.__window is None:
            return
        start = Point((self.__upper_left.x + self.__lower_right.x) // 2, (self.__upper_left.y + self.__lower_right.y) // 2)
        end = Point((to_cell.__upper_left.x + to_cell.__lower_right.x) // 2, (to_cell.__upper_left.y + to_cell.__lower_right.y) // 2)
        line = Line(start, end)
        self.__window.draw_line(line, "red" if undo else "gray")

    def draw_wall(self, wall, visible):
        if self.__window is None:
            return
        coord_fn = WALL_MAP[wall]
        start, end = coord_fn(self.__upper_left, self.__lower_right)
        color = "black" if visible else "white"
        self.__window.draw_line(Line(start, end), color)
        self.__visible_walls[wall] = True if visible else False