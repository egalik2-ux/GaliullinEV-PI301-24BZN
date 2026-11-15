class Table:
    def __init__(self, rows, cols):
        self.table = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_value(self, row, col, value):
        if 0 <= row < len(self.table) and 0 <= col < len(self.table[0]):
            self.table[row][col] = value

    def get_value(self, row, col):
        if 0 <= row < len(self.table) and 0 <= col < len(self.table[0]):
            return self.table[row][col]
        return None

    def n_rows(self):
        return len(self.table)

    def n_cols(self):
        return len(self.table[0])

    def delete_row(self, row):
        self.table.pop(row)

    def delete_col(self, col):
        for line in self.table:
            line.pop(col)

    def add_row(self, row):
        self.table.insert(row, [0 for _ in range(self.n_cols())])

    def add_col(self, col):
        for line in self.table:
            line.insert(col, 0)
