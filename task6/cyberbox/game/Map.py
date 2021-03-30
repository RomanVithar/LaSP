from cyberbox.common.Block import Block
from cyberbox.game.blocks.Node import Node


class Map:
    def __init__(self):
        self._w = 17
        self._hero = ()
        self._h = 12
        self._map = {}
        for i in range(self._h):
            for j in range(self._w):
                new_node = Node((i, j))
                if i-1 != -1:
                    new_node.add_incident((i-1, j))
                if i+1 != self._h:
                    new_node.add_incident((i+1, j))
                if j-1 != -1:
                    new_node.add_incident((i, j-1))
                if j+1 != self._w:
                    new_node.add_incident((i, j+1))
                self._map[(i, j)] = new_node

    # TODO: можно будет заменить чтобы файл был удобный для считывания а
    # TODO: карты делать в конструкторе но в связи с сложностью написания конструктора переношу на потом
    def fill(self, file):
        for i in range(self._h):
            self._map[(i, 0)].type = Block.WALL
            self._map[(i, self._w-1)].type = Block.WALL
        for i in range(self._w):
            self._map[(0, i)].type = Block.WALL
            self._map[(self._h-1, i)].type = Block.WALL
        array = []
        for line in file:
            array.append(line.rstrip('\n').split(' '))
        for i in range(1, self._h-1):
            for j in range(1, self._w-1):
                if int(array[i-1][j-1]) == Block.HERO:
                    self._hero = (i-1,j-1)
                self._map[(i, j)].type = int(array[i-1][j-1])

    def get_hero(self):
        return self._hero

    def get_map_blocks(self):
        arr = []
        for i in range(self._h):
            row = []
            for j in range(self._w):
                row.append(self._map[(i, j)].type)
            arr.append(row)
        return arr
