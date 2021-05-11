from cyberbox.Common import *
from cyberbox.game.Node import Node
from cyberbox.game.Map import Map


class Game:
    def __init__(self):
        self._map = Map()
        self._hero = ()
        self._pushers = []
        self._switcher_type = {}
        self._block_with_dir = {}
        self._new_pusher = None

    @property
    def hero(self):
        return self._hero

    def get_map(self):
        return self._map.get_map_blocks()

    def restart(self, file):
        self._map.fill(file)
        self._hero = self._map.hero
        self._pushers = self._map.pushers

    def up(self):
        self._move(self._map.get_node(self._hero), Dir.UP)
        self._handle_pushers()

    def down(self):
        self._move(self._map.get_node(self._hero), Dir.DOWN)
        self._handle_pushers()

    def left(self):
        self._move(self._map.get_node(self._hero), Dir.LEFT)
        self._handle_pushers()

    def right(self):
        self._move(self._map.get_node(self._hero), Dir.RIGHT)
        self._handle_pushers()
    
    def _handle_pushers(self):
        new_pushers = []
        for pusher in self._pushers:
            crnt_pusher = pusher
            for i in range(20):
                self._new_pusher = crnt_pusher
                self._move(crnt_pusher, crnt_pusher.directs[0],is_pusher=True)
                crnt_pusher = self._new_pusher
            new_pushers.append(crnt_pusher) 
        self._pushers = new_pushers
            
    def _move(self, init_node, direct, is_pusher = False):
        if init_node.type == TypeBlock.NOTHING and init_node.get_incident(direct).type == TypeBlock.ZAPPER and not is_pusher:
            zapper = init_node.get_incident(direct)
            if direct in zapper.directs:
                inc_zapper = zapper.get_incident(direct)
                if inc_zapper.type == TypeBlock.NOTHING or inc_zapper.type == TypeBlock.SELECTOR_O:
                    self._tp_hero(inc_zapper.coord)
                    return
                else:
                    return
            else:
                return
        current = init_node
        while True:
            if direct in current.get_incident(direct).directs:
                current = current.get_incident(direct)
            else:
                return
            if self._hero == init_node.coord:
                if current.type == TypeBlock.SELECTOR_O and self._hero == current.get_revers_incident(direct).coord:
                    self._hero = current.coord
                    return
                if current.type == TypeBlock.SELECTOR_X and self._hero == current.get_revers_incident(direct).coord:
                    return
            if is_pusher:
                if current.coord == self._hero:
                    return
            if current.type == TypeBlock.NOTHING:
                self._move_row(init_node, current, direct, is_pusher)
                return
            
            if current.type == TypeBlock.WALL or current.type == TypeBlock.ZAPPER or current.type == TypeBlock.PUSHER:
                return
                
    def _move_row(self, start, finish, direct, is_pusher):
        current = finish
        while current.coord != start.coord:
            current.type = current.get_revers_incident(direct).type
            current.directs = current.get_revers_incident(direct).directs
            current = current.get_revers_incident(direct)

        if not is_pusher:
            self._hero = start.get_incident(direct).coord
        else:
            self._new_pusher = start.get_incident(direct)
            start.type = TypeBlock.NOTHING
            start.directs = (Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT)
        if current.type == TypeBlock.SELECTOR_O:
            current.get_incident(direct).type = TypeBlock.NOTHING
            
    def _tp_hero(self, to_coord):
        self._hero = to_coord