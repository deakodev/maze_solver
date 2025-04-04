import time
import random
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

        self._break_entrance_and_exit()

        # Initialize each cell's visited attribute to False.
        for row in self.__cells:
            for cell in row:
                cell.visited = False

        random.seed(None)
        rows = len(self.__cells)
        cols = len(self.__cells[0])
        start_row = random.randint(0, rows - 1)
        start_col = random.randint(0, cols - 1)
        self._break_walls(start_row, start_col)

    def get_cells(self):
        return self.__cells

    def _cells(self) -> list[list[Cell]]:
        cells = []
        for y in range(Maze.PADDING, self.__height, self.__cell_size):
            row = []
            for x in range(Maze.PADDING, self.__width, self.__cell_size):
                cell = self._draw_cell(x, y)
                row.append(cell)
            cells.append(row)
        return cells

    def _draw_cell(self, start_x, start_y) -> Cell:
        cell = Cell(
            Point(start_x, start_y),
            Point(start_x + self.__cell_size, start_y + self.__cell_size),
            window=self.__window
        )
        cell.draw()
        if self.__window:
            self._animate()
        return cell

    def _animate(self):
        if self.__window:
            self.__window.redraw()
            time.sleep(0.015)

    def _break_entrance_and_exit(self):
        entrance_cell = self.__cells[0][0]
        entrance_cell.draw_wall("top", False)
        if self.__window:
            self._animate()
        exit_cell = self.__cells[-1][-1]
        exit_cell.draw_wall("bottom", False)
        if self.__window:
            self._animate()

    def _break_walls(self, row: int, col: int):
        current = self.__cells[row][col]
        current.visited = True

        # Build a list of potential neighbor directions and corresponding coordinates.
        neighbors = []
        if row > 0 and not self.__cells[row - 1][col].visited:
            neighbors.append(("top", row - 1, col))
        if row < len(self.__cells) - 1 and not self.__cells[row + 1][col].visited:
            neighbors.append(("bottom", row + 1, col))
        if col > 0 and not self.__cells[row][col - 1].visited:
            neighbors.append(("left", row, col - 1))
        if col < len(self.__cells[0]) - 1 and not self.__cells[row][col + 1].visited:
            neighbors.append(("right", row, col + 1))

        # Randomize the order for maze variety.
        random.shuffle(neighbors)

        for direction, n_row, n_col in neighbors:
            neighbor = self.__cells[n_row][n_col]
            if not neighbor.visited:
                # Remove the wall between current cell and neighbor.
                current.draw_wall(direction, False)
                # Remove the opposite wall in the neighbor cell.
                opposite = {"top": "bottom", "bottom": "top", "left": "right", "right": "left"}
                neighbor.draw_wall(opposite[direction], False)

                # Animate after wall removal.
                if self.__window:
                    self._animate()

                # Recursively break walls from the neighbor.
                self._break_walls(n_row, n_col)

    def _reset_cells_visited(self):
        for row in self.__cells:
            for cell in row:
                cell.visited = False


    def _solve_r(self, row: int, col: int) -> bool:
        self._animate()
        current = self.__cells[row][col]
        current.visited = True

        # Goal check: bottom-right cell
        if current == self.__cells[-1][-1]:
            return True

        directions = {
            "top":    (-1, 0),
            "bottom": (1, 0),
            "left":   (0, -1),
            "right":  (0, 1)
        }

        for direction, (dr, dc) in directions.items():
            new_row, new_col = row + dr, col + dc

            # Check bounds
            if 0 <= new_row < len(self.__cells) and 0 <= new_col < len(self.__cells[0]):
                next_cell = self.__cells[new_row][new_col]

                # Check if there's no wall in the current direction and cell hasn't been visited
                if not current._Cell__visible_walls[direction] and not next_cell.visited:
                    current.draw_path(next_cell)
                    if self._solve_r(new_row, new_col):
                        return True
                    current.draw_path(next_cell, undo=True)

        return False
    
    def solve(self, row=0, col=0):
        self._reset_cells_visited() 
        return self._solve_r(row, col)

