from cyberbox.common.Block import Block
from cyberbox.game.Node import Node
from cyberbox.common.Dir import Dir
from cyberbox.game.Map import Map


class Game:
    def __init__(self):
        self._map = Map()
        self._hero = ()
        self._pushers = []
        self._switcher_type = {}
        self._zapper_dir = {}
        self._init_switchers()

    def _init_switchers(self):
        self._switcher_type = {
            Block.NOTHING: self._do_nothing,
            Block.WALL: self._do_wall,
            Block.SLIDER_VERTICAL: self._do_slider_v,
            Block.SLIDER_HORIZONTAL: self._do_slider_h,
            Block.SLIDER_ALL: self._do_slider_a,
            Block.PUSHER_U: self._do_wall,  # doing that only where not hero push that
            Block.PUSHER_D: self._do_wall,
            Block.PUSHER_R: self._do_wall,
            Block.PUSHER_L: self._do_wall,
            Block.ZAPPER_U: self._do_wall,
            Block.ZAPPER_D: self._do_wall,
            Block.ZAPPER_R: self._do_wall,
            Block.ZAPPER_L: self._do_wall,
            Block.SELECTOR_X: self._do_selector_x,
            Block.SELECTOR_O: self._do_selector_o
        }
        self._zapper_dir = {
            Block.ZAPPER_U: Dir.UP, 
            Block.ZAPPER_D: Dir.DOWN,
            Block.ZAPPER_R: Dir.RIGHT,
            Block.ZAPPER_L: Dir.LEFT
        }

    @property
    def hero(self):
        return self._hero

    def load_level(self, file):
        self._map.fill(file)
        self._hero = self._map.hero
        self._pushers = self._map.pushers

    def get_map(self):
        return self._map.get_map_blocks()

    def restart(self):
        pass

    def up(self):
        self.move(self._map.get_node(self._hero), Dir.UP)

    def down(self):
        self.move(self._map.get_node(self._hero), Dir.DOWN)

    def left(self):
        self.move(self._map.get_node(self._hero), Dir.LEFT)

    def right(self):
        self.move(self._map.get_node(self._hero), Dir.RIGHT)

    def move(self, current, dir):
        new_node = current.get_incident(dir)
        #handler on zappers for hero
        if self._zapper_dir.get(new_node.type) == dir and new_node.get_incident(dir).type == Block.NOTHING:
            self._hero = new_node.get_incident(dir).coord
        else:
            # TODO: in adding there elif and write handler for other unusual blocks
            if new_node.type == Block.SELECTOR_O:
                self._hero = new_node.coord
                return
            if current.type == Block.SELECTOR_O and new_node.type == Block.NOTHING:
                #это кастыль и перемещение ряда неправильное попробуй толкнуть блок из селектора_о 
                self._hero = new_node.coord
                return
            curr = new_node
            while True:
                handler = self._switcher_type[curr.type]
                curr = handler(curr, dir)
                if curr.type == Block.WALL:
                    return
                if curr.type == Block.NOTHING:
                    self._move_row(current, curr, dir)
                    return
    

    def _move_row(self, start, finish, dir):
        current = start
        memory_type = current.type
        current.type = Block.NOTHING
        self._hero = current.get_incident(dir).coord
        while current != finish:
            temp = current.get_incident(dir).type
            current.get_incident(dir).type =  memory_type
            memory_type = temp
            current = current.get_incident(dir)

    def _do_nothing(self, init_block, dir):
        return init_block

    def _do_wall(self, init_block, dir):
        node = Node((0, 0))
        node.type = Block.WALL
        return node

    def _do_slider_v(self, init_block, dir):
        if dir == Dir.UP or dir == Dir.DOWN:
            return init_block._incident[dir]
        node = Node((0, 0))
        node.type = Block.WALL
        return node

    def _do_slider_h(self, init_block, dir):
        if dir == Dir.LEFT or dir == Dir.RIGHT:
            return init_block._incident[dir]
        node = Node((0, 0))
        node.type = Block.WALL
        return node

    def _do_slider_a(self, init_block, dir):
        return init_block._incident[dir]

    def _do_selector_x(self, init_block, dir):
        if init_block.get_revers_incident(dir).coord == self._hero:
            node = Node((0, 0))
            node.type = Block.WALL
            return node 
        return init_block._incident[dir]

    def _do_selector_o(self, init_block, dir):
        return init_block._incident[dir]