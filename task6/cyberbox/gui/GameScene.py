import sys
from cyberbox.common.Block import Block
from PyQt5.QtWidgets import QLabel, QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap
from PyQt5.QtCore import Qt
from cyberbox.game.Game import Game


class GameScene(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self._game = Game()
        self._game.load_level(open('resources/levels/level1', 'r'))
        self._init_sprites()


    def _init_sprites(self):
        self._labels = list()
        arr = self._game.get_map()
        for i in range(len(arr)):
            sub = list()
            for j in range(len(arr[i])):
                label = QLabel(self)
                label.show()
                sub.append(label)
            self._labels.append(sub)

        self._block_switcher = {
            Block.NOTHING: QPixmap('resources/images/nothing.png'),
            Block.WALL:QPixmap('resources/images/wall.png'),
            Block.SLIDER_VERTICAL: QPixmap('resources/images/slider_vertical.png'), 
            Block.SLIDER_HORIZONTAL: QPixmap('resources/images/slider_horizontal.png'),
            Block.SLIDER_ALL: QPixmap('resources/images/slider_all.png'),
            Block.PUSHER_U:QPixmap('resources/images/pusher_u.png'), 
            Block.PUSHER_D:QPixmap('resources/images/pusher_d.png'),
            Block.PUSHER_R:QPixmap('resources/images/pusher_r.png'),
            Block.PUSHER_L:QPixmap('resources/images/pusher_l.png'),
            Block.ZAPPER_U:QPixmap('resources/images/zapper_u.png'),
            Block.ZAPPER_D:QPixmap('resources/images/zapper_d.png'),
            Block.ZAPPER_R:QPixmap('resources/images/zapper_r.png'),
            Block.ZAPPER_L:QPixmap('resources/images/zapper_l.png'),
            Block.SELECTOR_X:QPixmap('resources/images/selector_x.png'),
            Block.SELECTOR_O:QPixmap('resources/images/selector_o.png'),
            Block.HERO: QPixmap('resources/images/hero.png'),
        }



    def initUI(self):
        self.setGeometry(100, 100, 880, 570)
        self.setWindowTitle('кибербокс')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.repaint(qp)
        qp.end()

    def repaint(self, qp):
        arr = self._game.get_map()
        for i in range(1,len(arr)-1):
            for j in range(1,len(arr[i])-1):
                pixmap = self._block_switcher[arr[i][j]]
                self._labels[i][j].setPixmap(pixmap)
                self._labels[i][j].setGeometry(j*pixmap.width(), i*pixmap.height(), pixmap.width(), pixmap.height())

