import sys
from cyberbox.common.Block import Block
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt
from cyberbox.game.Game import Game


class GameScene(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self._game = Game()
        self._game.load_level(open('resources/levels/level1', 'r'))
        self._block_switcher = {
            Block.NOTHING: Qt.gray,
            Block.WALL:Qt.red,
            Block.SLIDER_VERTICAL: Qt.yellow, 
            Block.SLIDER_HORIZONTAL: Qt.darkBlue,
            Block.SLIDER_ALL: Qt.green,
            Block.PUSHER_U: Qt.green,
            Block.PUSHER_D: Qt.darkBlue,
            Block.PUSHER_R: Qt.darkBlue,
            Block.PUSHER_L: Qt.darkBlue,
            Block.ZAPPER_U: Qt.darkBlue,
            Block.ZAPPER_D: Qt.darkBlue,
            Block.ZAPPER_R: Qt.darkBlue,
            Block.ZAPPER_L: Qt.darkBlue,
            Block.SELECTOR_x: Qt.darkBlue,
            Block.SELECTOR_O: Qt.darkBlue,
            Block.HERO: Qt.black,
        }

    def initUI(self):
        self.setGeometry(100, 100, 1680, 770)
        self.setWindowTitle('кибербокс')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.repaint(qp)
        qp.end()

    def repaint(self, qp):
        qp.setPen(Qt.red)
        temp_size = 53
        size = self.size()
        arr = self._game.get_map()
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                qp.setBrush(self._block_switcher[arr[i][j]])
                qp.drawRect(j*temp_size,i*temp_size,temp_size,temp_size)


