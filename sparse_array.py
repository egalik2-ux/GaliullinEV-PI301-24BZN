class SparseArray:
    def __init__(self):
        self._data = {}

    def __getitem__(self, index):
        return self._data.get(index, 0)

    def __setitem__(self, index, value):
        if value == 0:
            self._data.pop(index, None)
        else:
            self._data[index] = value
