import sys
from PyQt5 import QtCore

from PyQt5.QtGui import QPaintEngine, QPen
from cyberbox.game.Map import Map
from PyQt5.QtWidgets import QApplication, QWidget


def printer(arr):
    for i in range(len(arr)):
        print(arr[i]);

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.pen = QPen()              
    
    def paintEvent(self, event):
        painter = QPaintEngine(self)
        painter.setPen(self.pen)
        painter.drawRect(100, 170, 100, 100)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(1750, 750)
    widget.move(100, 100)
    widget.setWindowTitle('Кибербокс')
    widget.show()
    sys.exit(app.exec_())
#    map = Map()
#    map.fill('fd');
#    printer(map.get_map_blocks())
