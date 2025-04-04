from maze import Maze
from window import Window

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 50

def main():
    window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
    maze = Maze(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE, window=window)
    maze.solve()
    window.wait_for_close()

if __name__ == "__main__":
    main()