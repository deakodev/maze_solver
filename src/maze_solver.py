from cell import Cell, Wall
from line import Line, Point
from window import Window

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 50

def main():
    win = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

    for i in range(1, WINDOW_WIDTH, CELL_SIZE):
        for j in range(1, WINDOW_HEIGHT, CELL_SIZE):
            cell = Cell(win, Point(i, j), Point(i + CELL_SIZE, j + CELL_SIZE))
            cell.draw()

    win.wait_for_close()

if __name__ == "__main__":
    main()