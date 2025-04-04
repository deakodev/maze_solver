import unittest
from maze import Maze
from cell import Cell
from line import Point

# Minimal dummy window to allow drawing methods to update internal state.
class DummyWindow:
    def draw_line(self, line, color):
        pass  # Do nothing

    def redraw(self):
        pass  # Do nothing

class TestMazeAndCellFunctions(unittest.TestCase):
    def test_maze_cells_count(self):
        """Verify that Maze.get_cells() returns the correct number of cells."""
        width = 800
        height = 600
        cell_size = 50
        # For this test, the window does not affect the cell count logic.
        maze = Maze(width, height, cell_size, window=None)
        cells = maze.get_cells()

        expected_rows = len(range(Maze.PADDING, height - Maze.PADDING, cell_size))
        expected_cols = len(range(Maze.PADDING, width - Maze.PADDING, cell_size))
        expected_cells = expected_rows * expected_cols
        self.assertEqual(len(cells), expected_cells)

    def test_hide_wall_updates_visible_walls(self):
        """Verify that hide_wall() correctly updates the internal visible walls flag."""
        dummy_window = DummyWindow()
        cell = Cell(Point(0, 0), Point(50, 50), window=dummy_window)
        # Initially, all walls should be visible.
        self.assertTrue(cell._Cell__visible_walls["left"])
        self.assertTrue(cell._Cell__visible_walls["right"])
        self.assertTrue(cell._Cell__visible_walls["top"])
        self.assertTrue(cell._Cell__visible_walls["bottom"])

        # Hide the left wall.
        cell.hide_wall("left")
        self.assertFalse(cell._Cell__visible_walls["left"])

    def test_entrance_and_exit_wall_break(self):
        """
        Verify that the Maze breaks the entrance and exit walls by updating
        the first cell's "top" wall and the last cell's "bottom" wall.
        """
        dummy_window = DummyWindow()
        width = 800
        height = 600
        cell_size = 50
        maze = Maze(width, height, cell_size, window=dummy_window)
        cells = maze.get_cells()

        # The entrance cell (first cell) should have its "top" wall hidden.
        self.assertFalse(cells[0]._Cell__visible_walls["top"])
        # The exit cell (last cell) should have its "bottom" wall hidden.
        self.assertFalse(cells[-1]._Cell__visible_walls["bottom"])

    def test_draw_path_no_state_change(self):
        """
        Verify that draw_path() does not change the internal state (visible walls)
        of a Cell.
        """
        dummy_window = DummyWindow()
        cell1 = Cell(Point(0, 0), Point(50, 50), window=dummy_window)
        cell2 = Cell(Point(50, 50), Point(100, 100), window=dummy_window)

        # Copy the initial state of visible walls.
        initial_walls = cell1._Cell__visible_walls.copy()

        # Calling draw_path should not alter the visible walls.
        cell1.draw_path(cell2, undo=False)
        self.assertEqual(cell1._Cell__visible_walls, initial_walls)

        cell1.draw_path(cell2, undo=True)
        self.assertEqual(cell1._Cell__visible_walls, initial_walls)

if __name__ == '__main__':
    unittest.main()
