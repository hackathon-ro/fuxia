import unittest
import cloud

from las_vegas import generate_terminal_pattern

# Initiate the picloud simulator (localhost only) to speed up tests.
cloud.start_simulator()

class TestLasVegas(unittest.TestCase):
    """Testing the Las Vegas algorithm, the returned board must be a valid
    final configuration."""

    def test_las_vegas(self):
        board = generate_terminal_pattern()

        # Test the generated board is valid.
        self.assertIsNotNone(board)
        self.assertTrue(board.is_valid())

        # Test board doesn't have any empty cells.
        for i in xrange(0,9):
            for j in xrange(0,9):
                self.assertTrue(board.get(i, j) != 0)
