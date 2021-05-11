from cyberbox.Common import *


class Node:
    def __init__(self, coord):
        self._incident = {}
        self.coord = coord
        self.type = Block.NOTHING
        self.directs = (Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT) 

    def add_incident(self, dir, node):
        self._incident.update({dir: node})
    
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