from cyberbox.Common import Block
from cyberbox.game.Game import Game
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel, QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap
from PyQt5.QtCore import Qt


class GameScene(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self._block_w = 40
        self._block_h = 40
        self._game = Game()
        self._game.restart()
        self._level_numb = self._game.level_number[0]
        self._level_name = self._game.level_number[1] 
        self._level_live = self._game.live_number
        self._init_sprites()

    def _init_sprites(self):
        self._level_label = QLabel(self)
        self._level_label.setText("<b>Room {}<b><br><b>{}<b>".format(self._level_numb, self._level_name))
        self._label_live_number = QLabel(self)
        self._label_live_number.setText("<b>Attempts remaining: {}<b>".format(self._level_live))
        pixmap = QPixmap('task6/resources/images/background.png')
        self.resize(pixmap.width(), pixmap.height())
        back_label = QLabel(self)
        back_label.setPixmap(pixmap)
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
        pixmap = QPixmap('task6/resources/images/hero.png')
        self._hero_label.setPixmap(pixmap)
        back_label.show()
        help_label = QLabel(self)
        help_label.setText('<b>Arrows to move.<b><br><b>R to retry this level.<b>')
        help_label.move(385,510)
        help_label.show()
        help_label.raise_()
        self._level_label.show()
        self._label_live_number.show()
        self._label_live_number.move(133, 510)
        self._level_label.raise_()
        self._level_label.move(40, 45)
        self._label_live_number.raise_()
        self._hero_label.show()


        self._block_switcher = {
            Block.NOTHING: QPixmap('task6/resources/images/nothing.png'),
            Block.WALL: QPixmap('task6/resources/images/wall.png'),
            Block.SLIDER_VERTICAL: QPixmap('task6/resources/images/slider_vertical.png'),
            Block.SLIDER_HORIZONTAL: QPixmap('task6/resources/images/slider_horizontal.png'),
            Block.SLIDER_ALL: QPixmap('task6/resources/images/slider_all.png'),
            Block.PUSHER_U: QPixmap('task6/resources/images/pusher_u.png'),
            Block.PUSHER_D: QPixmap('task6/resources/images/pusher_d.png'),
            Block.PUSHER_R: QPixmap('task6/resources/images/pusher_r.png'),
            Block.PUSHER_L: QPixmap('task6/resources/images/pusher_l.png'),
            Block.ZAPPER_U: QPixmap('task6/resources/images/zapper_u.png'),
            Block.ZAPPER_D: QPixmap('task6/resources/images/zapper_d.png'),
            Block.ZAPPER_R: QPixmap('task6/resources/images/zapper_r.png'),
            Block.ZAPPER_L: QPixmap('task6/resources/images/zapper_l.png'),
            Block.SELECTOR_X: QPixmap('task6/resources/images/selector_x.png'),
            Block.SELECTOR_O: QPixmap('task6/resources/images/selector_o.png'),
            Block.HERO: QPixmap('task6/resources/images/hero.png'),
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
        if self._game.level_number != (self._level_numb, self._level_name):
            self._level_numb, self._level_name = self._game.level_number
            self._level_label.setText("<b>Room {}\n{}<b>".format(self._level_numb, self._level_name))
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
            self._game.restart()
            self._level_live = self._game.live_number
            self._label_live_number.setText(("<b>Attempts remaining: {}<b>".format(self._level_live)))