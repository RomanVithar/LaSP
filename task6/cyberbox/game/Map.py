from cyberbox.Common import *
from cyberbox.game.Node import Node


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
                    self._map[(i, j)].add_incident(Dir.UP, self._map[(i-1, j)])
                if i+1 != self._h:
                    self._map[(i, j)].add_incident(
                        Dir.DOWN, self._map[(i+1, j)])
                if j-1 != -1:
                    self._map[(i, j)].add_incident(
                        Dir.LEFT, self._map[(i, j-1)])
                if j+1 != self._w:
                    self._map[(i, j)].add_incident(
                        Dir.RIGHT, self._map[(i, j+1)])
        self._translater_type = {
            Block.NOTHING: (TypeBlock.NOTHING, (Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT)),
            Block.WALL: (TypeBlock.WALL, (0,)),
            Block.SLIDER_VERTICAL: (TypeBlock.SLIDER, (Dir.UP, Dir.DOWN)),
            Block.SLIDER_HORIZONTAL: (TypeBlock.SLIDER, (Dir.LEFT, Dir.RIGHT)),
            Block.SLIDER_ALL: (TypeBlock.SLIDER, (Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT)),
            Block.PUSHER_U: (TypeBlock.PUSHER, (Dir.UP,)),
            Block.PUSHER_D: (TypeBlock.PUSHER, (Dir.DOWN,)),
            Block.PUSHER_R: (TypeBlock.PUSHER, (Dir.RIGHT,)),
            Block.PUSHER_L: (TypeBlock.PUSHER, (Dir.LEFT,)),
            Block.ZAPPER_U: (TypeBlock.ZAPPER, (Dir.UP,)),
            Block.ZAPPER_D: (TypeBlock.ZAPPER, (Dir.DOWN,)),
            Block.ZAPPER_R: (TypeBlock.ZAPPER, (Dir.RIGHT,)),
            Block.ZAPPER_L: (TypeBlock.ZAPPER, (Dir.LEFT,)),
            Block.SELECTOR_O: (TypeBlock.SELECTOR_O, (Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT)),
            Block.SELECTOR_X: (TypeBlock.SELECTOR_X, (Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT)),
            Block.HERO: (TypeBlock.NOTHING, (0,))
        }
        self._retranslater_type = {
            (TypeBlock.NOTHING, (Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT)): Block.NOTHING,
            (TypeBlock.WALL, (0,)): Block.WALL,
            (TypeBlock.SLIDER, (Dir.UP, Dir.DOWN)): Block.SLIDER_VERTICAL,
            (TypeBlock.SLIDER, (Dir.LEFT, Dir.RIGHT)): Block.SLIDER_HORIZONTAL,
            (TypeBlock.SLIDER, (Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT)): Block.SLIDER_ALL,
            (TypeBlock.PUSHER, (Dir.UP,)): Block.PUSHER_U,
            (TypeBlock.PUSHER, (Dir.DOWN,)): Block.PUSHER_D,
            (TypeBlock.PUSHER, (Dir.RIGHT,)): Block.PUSHER_R,
            (TypeBlock.PUSHER, (Dir.LEFT,)): Block.PUSHER_L,
            (TypeBlock.ZAPPER, (Dir.UP,)): Block.ZAPPER_U,
            (TypeBlock.ZAPPER, (Dir.DOWN,)): Block.ZAPPER_D,
            (TypeBlock.ZAPPER, (Dir.RIGHT,)): Block.ZAPPER_R,
            (TypeBlock.ZAPPER, (Dir.LEFT,)): Block.ZAPPER_L,
            (TypeBlock.SELECTOR_X, (Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT)): Block.SELECTOR_X,
            (TypeBlock.SELECTOR_O, (Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT)): Block.SELECTOR_O
        }

    def fill(self, file):
        self._hero = ()
        self._pushers = []
        for i in range(self._h):
            self._map[(i, 0)].type = TypeBlock.WALL
            self._map[(i, 0)].directs = (0,)
            self._map[(i, self._w-1)].type = TypeBlock.WALL
            self._map[(i, self._w-1)].directs = (0,)
        for i in range(self._w):
            self._map[(0, i)].type = TypeBlock.WALL
            self._map[(0, i)].directs = (0,)
            self._map[(self._h-1, i)].type = TypeBlock.WALL
            self._map[(self._h-1, i)].directs = (0,)
        array = []
        for line in file:
            array.append(line.rstrip('\n').split(' '))
        for i in range(1, self._h-1):
            for j in range(1, self._w-1):
                type, directs = self._translater_type[int(array[i-1][j-1])]
                if int(array[i-1][j-1]) == TypeBlock.HERO:
                    self._hero = (i-1, j-1)
                    self._map[(i, j)].type = TypeBlock.NOTHING
                elif (type == TypeBlock.PUSHER):
                    self._map[(i, j)].type = type
                    self._map[(i, j)].directs = directs
                    self._pushers.append(self._map[(i, j)])
                else:
                    self._map[(i, j)].type = type
                    self._map[(i, j)].directs = directs

    @property
    def hero(self):
        return (self._hero[0]+1, self._hero[1]+1)

    @property
    def pushers(self):
        return self._pushers

    def get_map_blocks(self):
        arr = []
        for i in range(self._h):
            row = []
            for j in range(self._w):
                row.append(self._retranslater_type[(self._map[(i, j)].type, self._map[(i, j)].directs)])
            arr.append(row)
        return arr

    def get_node(self, coord):
        return self._map[coord]
