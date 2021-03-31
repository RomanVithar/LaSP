from task6.cyberbox.common.Block import Block


class Node:
    def __init__(self,coord):
        self._coord = coord
        self._incident = {}
        self._type = Block.NOTHING
        self._switcher_type = {}

    def _init_switcher(self):
        self._switcher_type = {
            Block.NOTHING: self._do_nothing,
            Block.WALL: self._do_wall,
            Block.SLIDER_VERTICAL: self._do_slider_v, 
            Block.SLIDER_HORIZONTAL: self._do_slider_h,
            Block.SLIDER_ALL: self._do_slider_a,
            Block.PUSHER_U:self._do_pusher_u, 
            Block.PUSHER_D:self._do_pusher_d,
            Block.PUSHER_R:self._do_pusher_r,
            Block.PUSHER_L:self._do_pusher_l,
            Block.ZAPPER_U:self._do_zapper_u,
            Block.ZAPPER_D:self._do_zapper_d,
            Block.ZAPPER_R:self._do_zapper_r,
            Block.ZAPPER_L:self._do_zapper_l,
            Block.SELECTOR_X:self._do_selector_x,
            Block.SELECTOR_O:self._do_selector_o,
            Block.HERO: self._do_hero,
        }

    def add_incident(self, dir, node):
        self._incident.update({dir:node})

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
    def coord(self,coord):
        self._coord = coord

    
    def move(self, dir):
        self._handler = self._switcher_type[self._type]  
        self._handler(dir)


    def _do_nothing(self, dir):
        pass

    def _do_pusher_l(self, dir):
        pass

    def _do_pusher_r(self, dir):
        pass

    def _do_pusher_u(self, dir):
        pass
        
    def _do_pusher_d(self, dir):
        pass
        
    def _do_selector_x(self, dir):
        pass
        
    def _do_selector_o(self, dir):
        pass
        
    def _do_slider_v(self, dir):
        pass
        
    def _do_slider_h(self, dir):
        pass

    def _do_slider_a(self, dir):
        pass
        
    def _do_wall(self, dir):
        pass
        
    def _do_hero(self, dir):
        pass
        
    def _do_zapper_l(self, dir):
        pass
        
    def _do_zapper_r(self, dir):
        pass
        
    def _do_zapper_d(self, dir):
        pass

    def _do_zapper_u(self, dir):
        pass