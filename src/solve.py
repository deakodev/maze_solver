from cell import Cell, Wall
from line import Line, Point
from maze import Maze
from window import Window

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 50

def main():
    window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
    Maze(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE, window=window)
    window.wait_for_close()

if __name__ == "__main__":
    main()