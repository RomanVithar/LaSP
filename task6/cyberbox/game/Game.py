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
        self._live_number = 8
        self._level_number = 1
        self._new_pusher = None
        self._list_levels = [
            'task6/resources/levels/level09',           
            'task6/resources/levels/level02',           
            'task6/resources/levels/level03',           
            'task6/resources/levels/level04',           
            'task6/resources/levels/level05',           
            'task6/resources/levels/level06',           
            'task6/resources/levels/level07',           
            'task6/resources/levels/level08',           
            'task6/resources/levels/level09'           
        ]
        self._level_names = {
            1:'The lobby.',
            2:'No problem.',
            3:'Think ahead.',
            4:'Choices, choices.',
            5:'You can do it!',
            6:'Chain reaction.',
            7:'Don\'t get zapped!',
            8:'Show that.',
            9:'Ok).'
        }
        self._loader = self._level_loader()
        self._current_lvl = next(self._loader)
        

    @property
    def hero(self):
        return self._hero


    def get_map(self):
        return self._map.get_map_blocks()


    def restart(self):
        if self._live_number == 0:
            self._loader = self._level_loader()
            self._current_lvl = next(self._loader)      
            self._live_number = 8
        self._map.fill(open(self._current_lvl, 'r'))
        self._live_number -=1
        self._hero = self._map.hero
        self._pushers = self._map.pushers


    def up(self):
        self._move(self._map.get_node(self._hero), Dir.UP)
        self._handle_pushers()
        self._handle_finish()

    def down(self):
        self._move(self._map.get_node(self._hero), Dir.DOWN)
        self._handle_pushers()
        self._handle_finish()

    def left(self):
        self._move(self._map.get_node(self._hero), Dir.LEFT)
        self._handle_pushers()
        self._handle_finish()


    def right(self):
        self._move(self._map.get_node(self._hero), Dir.RIGHT)
        self._handle_pushers()
        self._handle_finish()


    @property
    def live_number(self):
        return self._live_number


    @property
    def level_number(self):
        return (self._level_number, self._level_names[self._level_number])


    def _handle_pushers(self):
        for j in range(3):
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


    def _level_loader(self):
        i = 0
        while i < len(self._list_levels):
            yield self._list_levels[i]
            i+=1


    def _handle_finish(self):
        if self._hero == (1,8):
            self._current_lvl = next(self._loader)
            self._level_number += 1
            self._live_number+=1
            self.restart()