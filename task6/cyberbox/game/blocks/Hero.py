from task6.cyberbox.game.blocks.Node import Node
from task6.cyberbox.common.Block import Block 


class Hero(Node):
    def __init__(self, coord):
        super().__init__(coord)
        self._type = Block.HERO