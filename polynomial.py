class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = list(coeffs)

    def __call__(self, x):
        result = 0
        for power, coeff in enumerate(self.coeffs):
            result += coeff * (x ** power)
        return result

    @staticmethod
    def _align_lengths(c1, c2):
        max_len = max(len(c1), len(c2))
        c1_aligned = c1 + [0] * (max_len - len(c1))
        c2_aligned = c2 + [0] * (max_len - len(c2))
        return c1_aligned, c2_aligned

    def __add__(self, other):
        c1, c2 = self._align_lengths(self.coeffs, other.coeffs)
        new_coeffs = [a + b for a, b in zip(c1, c2)]
        return Polynomial(new_coeffs)

    def __sub__(self, other):
        c1, c2 = self._align_lengths(self.coeffs, other.coeffs)
        new_coeffs = [a - b for a, b in zip(c1, c2)]
        return Polynomial(new_coeffs)
