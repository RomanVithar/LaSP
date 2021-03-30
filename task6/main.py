import sys
from cyberbox.gui.GameScene import GameScene
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = GameScene()
    sys.exit(app.exec_())    