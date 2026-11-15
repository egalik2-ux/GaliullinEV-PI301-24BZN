class Date:
    MONTH_LENGTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, month, day):
        self.month = month
        self.day = day

    def day_number(self):
        return sum(self.MONTH_LENGTHS[:self.month - 1]) + self.day

    def __sub__(self, other):
        return self.day_number() - other.day_number()
