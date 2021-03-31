from task6.cyberbox.game.blocks.Node import Node
from task6.cyberbox.common.Block import Block 


class PusherL(Node):
    def __init__(self, coord):
        super().__init__(coord)
        self._type = Block.PUSHER_L


class PusherR(Node):
    def __init__(self, coord):
        super().__init__(coord)
        self._type = Block.PUSHER_R


class PusherU(Node):
    def __init__(self, coord):
        super().__init__(coord)
        self._type = Block.PUSHER_U


class PusherD(Node):
    def __init__(self, coord):
        super().__init__(coord)
        self._type = Block.PUSHER_D
