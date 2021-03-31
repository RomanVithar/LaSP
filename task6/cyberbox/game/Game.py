from typing import Mapping


class Game:
    def __init__(self):
        self._map = Mapping()
        self._hero = ()

    def load_level(self, file):
        self._map.fill(file)
        self._hero = self._map.get_hero()

    def get_map(self):
        return self._map.get_map_blocks()

    def up(self):
        pass
 
    def down(self):
        pass
    
    def left(self):
        pass
 
    def right(self):
        pass
 
    def restart(self):
        pass