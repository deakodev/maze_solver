

import time
from cell import Cell
from line import Point


class Maze:
    PADDING = 50
    def __init__(self, width, height, cell_size, window=None):
        self.__window = window
        self.__width = width - Maze.PADDING
        self.__height = height - Maze.PADDING
        self.__cell_size = cell_size
        self.__cells = self._cells()

    def get_cells(self):
        return self.__cells

    def _cells(self) -> list[Cell]:
        cells = []
        for y in range(Maze.PADDING, self.__height, self.__cell_size):
            for x in range(Maze.PADDING, self.__width, self.__cell_size):
                cell = self._draw_cell(x, y)
                cells.append(cell)
        return cells

    def _draw_cell(self, start_x, start_y) -> Cell:
        cell = Cell(Point(start_x, start_y), Point(start_x + self.__cell_size, start_y + self.__cell_size), window=self.__window)
        cell.draw()
        if self.__window:
            self._animate()
        return cell
        
    def _animate(self):
        self.__window.redraw()
        time.sleep(0.015)
