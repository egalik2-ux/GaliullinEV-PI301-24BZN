class Sequence:
    def sum(self, n: int) -> int | float:
        return n * (n + 1) // 2


class ArithmeticSequence(Sequence):
    def __init__(self, a1, d):
        self.a1 = a1
        self.d = d

    def sum(self, n: int) -> float:
        return (2 * self.a1 + (n - 1) * self.d) * n / 2


class GeometricSequence(Sequence):
    def __init__(self, b1, q):
        self.b1 = b1
        self.q = q

    def sum(self, n: int) -> float:
        if self.q == 1:
            return self.b1 * n
        return self.b1 * (self.q ** n - 1) / (self.q - 1)


class SquareSequence(Sequence):
    def sum(self, n: int) -> int:
        return n * (n + 1) * (2 * n + 1) // 6
