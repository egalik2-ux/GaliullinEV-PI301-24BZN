class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def end(self):
        if not self.words:
            return

        lines = []
        current_line = []
        current_len = 0

        for word in self.words:
            add_len = len(word) if not current_line else len(word) + 1
            if current_len + add_len <= self.width:
                current_line.append(word)
                current_len += add_len
            else:
                lines.append(" ".join(current_line))
                current_line = [word]
                current_len = len(word)

        if current_line:
            lines.append(" ".join(current_line))

        for line in lines:
            print(line)

        self.words = []


class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def end(self):
        if not self.words:
            return

        lines = []
        current_line = []
        current_len = 0

        for word in self.words:
            add_len = len(word) if not current_line else len(word) + 1
            if current_len + add_len <= self.width:
                current_line.append(word)
                current_len += add_len
            else:
                lines.append(" ".join(current_line))
                current_line = [word]
                current_len = len(word)

        if current_line:
            lines.append(" ".join(current_line))

        for line in lines:
            padding = " " * (self.width - len(line))
            print(padding + line)

        self.words = []
