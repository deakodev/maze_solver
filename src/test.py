import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_cells(self):
        width = 800
        height = 600
        cell_size = 50
        cells = Maze(width, height, cell_size).get_cells()

        # Expected number of cells based on Maze's logic
        expected_rows = len(range(Maze.PADDING, height - Maze.PADDING, cell_size))
        expected_cols = len(range(Maze.PADDING, width - Maze.PADDING, cell_size))
        expected_cells = expected_rows * expected_cols

        self.assertEqual(len(cells), expected_cells)

if __name__ == "__main__":
    unittest.main()
