import sys

from PyQt5 import QtGui
from cyberbox.common.Block import Block
from PyQt5.QtWidgets import QLabel, QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap
from PyQt5.QtCore import Qt
from cyberbox.game.Game import Game


class GameScene(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self._block_w = 40
        self._block_h = 40
        self._game = Game()
        #TODO: generator next
        self._game.restart(self._level_loader())
        self._init_sprites()

    def _init_sprites(self):
        pixmap = QPixmap('resources/images/background.png')
        self.resize(pixmap.width(), pixmap.height())
        back_label = QLabel(self)
        back_label.setPixmap(pixmap)
        back_label.show()
        self._labels = list()
        arr = self._game.get_map()
        for i in range(len(arr)):
            sub = list()
            for j in range(len(arr[i])):
                label = QLabel(self)
                label.show()
                sub.append(label)
            self._labels.append(sub)
        self._hero_label = QLabel(self)
        pixmap = QPixmap('resources/images/hero.png')
        self._hero_label.setPixmap(pixmap)
        self._hero_label.show()

        self._block_switcher = {
            Block.NOTHING: QPixmap('resources/images/nothing.png'),
            Block.WALL: QPixmap('resources/images/wall.png'),
            Block.SLIDER_VERTICAL: QPixmap('resources/images/slider_vertical.png'),
            Block.SLIDER_HORIZONTAL: QPixmap('resources/images/slider_horizontal.png'),
            Block.SLIDER_ALL: QPixmap('resources/images/slider_all.png'),
            Block.PUSHER_U: QPixmap('resources/images/pusher_u.png'),
            Block.PUSHER_D: QPixmap('resources/images/pusher_d.png'),
            Block.PUSHER_R: QPixmap('resources/images/pusher_r.png'),
            Block.PUSHER_L: QPixmap('resources/images/pusher_l.png'),
            Block.ZAPPER_U: QPixmap('resources/images/zapper_u.png'),
            Block.ZAPPER_D: QPixmap('resources/images/zapper_d.png'),
            Block.ZAPPER_R: QPixmap('resources/images/zapper_r.png'),
            Block.ZAPPER_L: QPixmap('resources/images/zapper_l.png'),
            Block.SELECTOR_X: QPixmap('resources/images/selector_x.png'),
            Block.SELECTOR_O: QPixmap('resources/images/selector_o.png'),
            Block.HERO: QPixmap('resources/images/hero.png'),
        }

    def initUI(self):
        self.setGeometry(100, 100, 880, 570)
        self.setWindowTitle('кибербокс')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.repaint()
        qp.end()

    def repaint(self):
        arr = self._game.get_map()
        for i in range(1, len(arr)-1):
            for j in range(1, len(arr[i])-1):
                pixmap = self._block_switcher[arr[i][j]]
                self._labels[i][j].setPixmap(pixmap)
                self._labels[i][j].setGeometry(
                    j*self._block_w - self._block_w + 8, i*self._block_h + self._block_h + 4, self._block_w, self._block_h)
        i, j = self._game.hero
        self._hero_label.setGeometry(j*self._block_w - self._block_w + 8,
                                     i*self._block_h + self._block_h + 4, self._block_w, self._block_h)

    def keyPressEvent(self, event):
        # h - 72; l - 76; j - 74; k - 75; r - 82
        if event.key() == 74:
            self._game.down()
        elif event.key() == 75:
            self._game.up()
        elif event.key() == 72:
            self._game.left()
        elif event.key() == 76:
            self._game.right()
        elif event.key() == 82:
            #TODO: generator next but this need use not next but current
            self._game.restart(self._level_loader())
        elif event.key() == 68:
            # debug
            self.print_map()

    #TODO: generator
    def _level_loader(self):
        return open('resources/levels/level1', 'r') 

# debug


    def print_map(self):
        arr = self._game.get_map()
        for i in range(len(arr)):
            print(arr[i])
