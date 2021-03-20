class Splitter:
    def __init__(self, str):
        self.str = str
        self.index = 0
        self.pervious_index = 0
        self.stop_iter = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.stop_iter:
            raise StopIteration
        split_char = self.str[self.index]
        while split_char != ' ' and split_char != '\n':
            self.index += 1
            if self.index == len(self.str):
                self.stop_iter = True
                split_char = 'e'
                break
            split_char = self.str[self.index]
        word = self.str[self.pervious_index:self.index]
        self.index += 1
        self.pervious_index = self.index
        return word, split_char
