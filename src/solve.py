from cell import Cell, Wall
from line import Line, Point
from maze import Maze
from window import Window

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 50

def main():
    win = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
    Maze(win, WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
    win.wait_for_close()

if __name__ == "__main__":
    main()