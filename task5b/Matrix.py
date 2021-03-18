class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __iter__(self):
        self.indent = 0
        self.i = 0
        self.j = 1
        self.di = 0
        self.dj = 1
        self.exit_count = len(self.matrix) * len(self.matrix[0])
        return self

    def __next__(self):
        if self.exit_count < 2:
            raise StopIteration
        m_val = self.matrix[self.i][self.j]
        if self.dj > 0 and self.j == len(self.matrix) - self.indent-1:
            self.dj = 0
            self.di = 1
        if self.di > 0 and self.i == len(self.matrix) - self.indent-1:
            self.di = 0
            self.dj = -1
        if self.dj < 0 and self.j == self.indent:
            self.dj = 0
            self.di = -1
        if self.di < 0 and self.i == self.indent+1:
            self.di = 0
            self.dj = 1
            self.indent +=1
        self.i+=self.di
        self.j+=self.dj
        self.exit_count-=1
        return m_val 
