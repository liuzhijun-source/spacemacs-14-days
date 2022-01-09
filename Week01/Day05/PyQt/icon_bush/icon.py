import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget


class example(QWidget):

    def __init__(self):
        """Follow the clas"""
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon("web.png"))
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = example()
    sys.exit(app.exec_())
