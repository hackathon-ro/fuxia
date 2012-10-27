def init_matrix(value=0):
    state = []
    for i in xrange(10):
        state.append([value] * 10)
    return state

class Board(object):

    @classmethod
    def from_file(cls, filename):
        """Load a board from a filename."""
        matrix = []
        with open(filename, 'r') as f:
            for line in f:
                row = [int(x) for x in line.split()]
                matrix.append(row)
        # Initialize an empty board, use fill to add all read values.
        board = Board()
        for i in xrange(9):
            for j in xrange(9):
                board.fill(i, j, matrix[i][j])
        return board

    def __init__(self):
        """Initializes an empty Board."""
        self._board = init_matrix()
        # Initialize _possibilities: for each empty cell, store a list of all
        # possible values that can be filled there.
        self._possibilities = {}
        for i in xrange(9):
            for j in xrange(9):
                self._possibilities[(i,j)] = range(1, 10)

    def get(self, i, j):
        return self._board[i][j]

    def fill(self, i, j, value):
        """Fills in an empty cell with value."""
        if self._board[i][j] != 0:
            raise ValueError('Call is not empty.')

        self._board[i][j] = value

        for k in xrange(9):
            # This is O(N), but acceptable for now.
            if value in self._possibilities[(i,k)]:
                self._possibilities[(i,k)].remove(value)
            if value in self._possibilities[(k,j)]:
                self._possibilities[(k,j)].remove(value)
            # Remove value from all cells within the same block as (i,j).
            bi = i / 3 + k / 3
            bj = j / 3 + k % 3
            if value in self._possibilities[(bi,bj)]:
                self._possibilities[(bi,bj)].remove(value)

    def get_possibilities(self, i, j):
        if self._board[i][j] != 0:
            raise ValueError('Call is not empty.')

        if self._possibilities[(i,j)]:
            return self._possibilities[(i,j)]
        else:
            # This cell cannot be filled in with any values.
            return None

    def __repr__(self):
        string = ''
        for row in self._board:
            row_string = ' '.join(map(str, row))
            string += '%s\n' % row_string
        return string
