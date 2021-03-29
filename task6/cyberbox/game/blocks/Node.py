from cyberbox.common.Block import Block


class Node:
    def __init__(self,coord):
        self._coord = coord
        self._incident = list();
        self._type = Block.NOTHING


    def add_incident(self, coord):
        self._incident.append(coord)
    
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type
