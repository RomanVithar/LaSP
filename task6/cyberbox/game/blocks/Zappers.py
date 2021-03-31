from task6.cyberbox.game.blocks.Node import Node
from task6.cyberbox.common.Block import Block 


class ZapperL(Node):
    def __init__(self, coord):
        super().__init__(coord)
        self._type = Block.ZAPPER_L


class ZapperR(Node):
    def __init__(self, coord):
        super().__init__(coord)
        self._type = Block.ZAPPER_R


class ZapperU(Node):
    def __init__(self, coord):
        super().__init__(coord)
        self._type = Block.ZAPPER_U


class ZapperD(Node):
    def __init__(self, coord):
        super().__init__(coord)
        self._type = Block.ZAPPER_D
