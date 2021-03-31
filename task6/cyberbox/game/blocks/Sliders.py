from task6.cyberbox.game.blocks.Node import Node
from task6.cyberbox.common.Block import Block 


class SliderHorizontal(Node):
    def __init__(self, coord):
        super().__init__(coord)
        self._type = Block.SLIDER_HORIZONTAL


class SliderVertical(Node):
    def __init__(self, coord):
        super().__init__(coord)
        self._type = Block.SLIDER_VERTICAL


class SliderAll(Node):
    def __init__(self, coord):
        super().__init__(coord)
        self._type = Block.SLIDER_ALL