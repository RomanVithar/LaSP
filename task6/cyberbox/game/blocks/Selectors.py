from task6.cyberbox.game.blocks.Node import Node
from task6.cyberbox.common.Block import Block 


class SelectorX(Node):
    def __init__(self, coord):
        super().__init__(coord)
        self._type = Block.SELECTOR_X


class SelectorO(Node):
    def __init__(self, coord):
        super().__init__(coord)
        self._type = Block.SELECTOR_O