from Splitter import Splitter


class Formater:
    def __init__(self, str, width):
        self.str = str
        self.width = width
        self.splitter = Splitter(self.str)
        self.was_n = True
        self.buffer = ''
        self.stop_iter = False

    def __iter__(self):
        return self

    def add_spaces(self, list, free_space):
        if list[0] == '      ':
            if len(list) == 1:
                return list[0]
            else:
                list[0] += list[1]
                del list[1]
        if len(list) == 1:
            return list[0]
        in_every = free_space // (len(list) - 1)
        last_word = free_space % (len(list) - 1)
        outcome = ''
        for i in range(len(list)-last_word-1):
            outcome += list[i] + ' '*(in_every+1)
        for i in range(len(list)-last_word-1, len(list)-1):
            outcome += list[i] + ' '*(in_every+2)
        outcome += list[len(list)-1]
        return outcome

    def __next__(self):
        if self.stop_iter and not self.buffer:
            raise StopIteration
        list_words = list()
        free_space = self.width
        if self.buffer:
            if len(self.buffer) > self.width:
                t = self.buffer[:self.width]
                self.buffer = self.buffer[self.width:len(self.buffer)]
                return t
            else:
                list_words.append(self.buffer)
                free_space -= len(self.buffer) + 1
                self.buffer = ''
        if self.was_n:
            if len(list_words) != 0:
                return list_words[0]
            self.was_n = False
            if self.width < 6:
                self.buffer += ' ' * (6 - self.width)
                return ' ' * self.width
            else:
                list_words.append('      ')
                free_space -= 6
        try:
            word, symbol = next(self.splitter)
            while free_space - len(word) > 0:
                if symbol == '\n':
                    self.was_n = True
                    list_words.append(word)
                    return self.add_spaces(list_words, 0)
                list_words.append(word)
                free_space -= len(word) + 1
                word, symbol = next(self.splitter)
            else:
                if symbol == '\n':
                    self.was_n = True
                self.buffer += word
                return self.add_spaces(list_words, free_space+1)
        except StopIteration:
            self.stop_iter = True
            return self.add_spaces(list_words, free_space)
