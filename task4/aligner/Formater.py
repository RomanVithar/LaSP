# выполнить только комментарии остальное должно робит
class Formater:
    def __init__(self, str, width):
        self.str = str
        self.width = width

    def __iter__(self):
        self.splitter = Splitter(self.str)
        self.was_n = True
        self.buffer = '' 
        return self

    def package(self, list):
        pass

    def __next__(self):
        list_words= list() 
        free_space = self.width 
        # пояснение: если длина слова в буфере больше ширины закинуть кусок в строку и оставить оставшийся в буфере
        if self.buffer != '':
            if len(self.buffer) > self.width:
                t =  self.buffer[:self.width]
                self.buffer = self.buffer[self.width:len(self.buffer)]
                return t 
            else:
                list_words.append(self.buffer) 
                free_space -= len(self.buffer) +1
                self.buffer = ''
        if self.was_n:
            self.was_n = False
            if self.width<6:
                self.buffer += ' ' * (6- self.width)
                return ' '* self.width
            else:
                list_words.append('      ')
                free_space -= 6
        try:
            word, symbol = next(self.splitter)
            while free_space - len(word) > 0:
                if symbol == '\n':
                    self.was_n = True
                    list_words.append(word)
                    # упаковать лист слов
                    # вернуть строку 
                list_words.append(word)
                free_space += len(word) + 1
                word, symbol = next(self.splitter)
            else:
                if symbol == '\n':
                    self.was_n = True
                # упаковать лист слов
                self.buffer += word
                # вернуть строку
        except StopIteration:
            # упаковать строку
            # вернуть строку 
            # сделать следующий вызов стопитератион