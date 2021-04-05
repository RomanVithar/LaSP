from cyberbox.common.Block import Block
from cyberbox.common.Dir import Dir


class Node:
    def __init__(self, coord):
        self._coord = coord
        self._incident = {}
        self._type = Block.NOTHING

    def add_incident(self, dir, node):
        self._incident.update({dir: node})

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def coord(self):
        return self._coord

    @coord.setter
    def coord(self, coord):
        self._coord = coord

    def get_incident(self, dir):
        return self._incident[dir]

    def get_revers_incident(self, dir):
        if dir == Dir.UP:
            return self._incident[Dir.DOWN]
        elif dir == Dir.DOWN:
            return self._incident[Dir.UP]
        elif dir == Dir.LEFT:
            return self._incident[Dir.RIGHT]
        else:
            return self._incident[Dir.LEFT]