class Table:
    def __init__(self, rows, cols):
        # Создаём таблицу размера rows x cols, заполненную None
        self.table = [[None for _ in range(cols)] for _ in range(rows)]
        self._rows = rows
        self._cols = cols

    def set_value(self, row, col, value):
        # Проверка границ: меняем только если индексы в пределах таблицы
        if 0 <= row < self._rows and 0 <= col < self._cols:
            self.table[row][col] = value

    def get_value(self, row, col):
        # Если за пределами — возвращаем None, иначе — значение ячейки
        if 0 <= row < self._rows and 0 <= col < self._cols:
            return self.table[row][col]
        return None

    def n_rows(self):
        return self._rows

    def n_cols(self):
        return self._cols
