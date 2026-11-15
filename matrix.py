class Matrix:
    def __init__(self, rows):
        self.rows = [list(row) for row in rows]

    @property
    def n_rows(self):
        return len(self.rows)

    @property
    def n_cols(self):
        if not self.rows:
            return 0
        return len(self.rows[0])

    def _check_index(self, i, j):
        """Вспомогательный метод для проверки границ индексов"""
        if not (0 <= i < self.n_rows and 0 <= j < self.n_cols):
            raise IndexError("Index out of range")

    def __getitem__(self, key):
        i, j = key
        self._check_index(i, j)
        return self.rows[i][j]

    def __setitem__(self, key, value):
        i, j = key
        self._check_index(i, j)
        self.rows[i][j] = value

    def __add__(self, other):
        if self.n_rows != other.n_rows or self.n_cols != other.n_cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        result_rows = [
            [self.rows[i][j] + other.rows[i][j] for j in range(self.n_cols)]
            for i in range(self.n_rows)
        ]
        return Matrix(result_rows)

    def __mul__(self, scalar):
        result_rows = [
            [self.rows[i][j] * scalar for j in range(self.n_cols)]
            for i in range(self.n_rows)
        ]
        return Matrix(result_rows)

    def __repr__(self):
        return "Matrix(" + repr(self.rows) + ")"