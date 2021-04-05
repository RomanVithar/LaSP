from cyberbox.game.Node import Node
from cyberbox.common.Dir import Dir
from cyberbox.common.Block import Block


class Map:
    def __init__(self):
        self._w = 17
        self._h = 12
        self._hero = ()
        self._map = {}
        self._pushers = []
        for i in range(self._h):
            for j in range(self._w):
                self._map[(i, j)] = Node((i, j))
        for i in range(self._h):
           for j in range(self._w):
               if i-1 != -1:
                   self._map[(i, j)].add_incident(Dir.UP, self._map[(i-1,j)])
               if i+1 != self._h:
                   self._map[(i, j)].add_incident(Dir.DOWN, self._map[(i+1,j)])
               if j-1 != -1:
                   self._map[(i, j)].add_incident(Dir.LEFT, self._map[(i,j-1)])
               if j+1 != self._w:
                   self._map[(i, j)].add_incident(Dir.RIGHT, self._map[(i,j+1)])

    # TODO: можно будет заменить чтобы файл был удобный для считывания а
    # TODO: карты делать в конструкторе но в связи с сложностью написания конструктора переношу на потом
    def fill(self, file):
        self._hero = ()
        self._pushers = []
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
                    self._hero = (i-1, j-1)
                elif (int(array[i-1][j-1]) == Block.PUSHER_L or
                 int(array[i-1][j-1]) == Block.PUSHER_R or
                 int(array[i-1][j-1]) == Block.PUSHER_U or
                 int(array[i-1][j-1]) == Block.PUSHER_D): 
                    self._map[(i, j)].type = int(array[i-1][j-1])
                    self._pushers.append(self._map[(i,j)])
                else:
                    self._map[(i, j)].type = int(array[i-1][j-1])

    @property
    def hero(self):
        return (self._hero[0]+1,self._hero[1]+1) 
    
    @property 
    def pushers(self):
        return self._pushers

    def get_map_blocks(self):
        arr = []
        for i in range(self._h):
            row = []
            for j in range(self._w):
                row.append(self._map[(i, j)].type)
            arr.append(row)
        return arr

    def get_node(self, coord):
        return self._map[coord]