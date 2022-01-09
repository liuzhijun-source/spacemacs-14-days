"""用来退出 Qt 程序，提供指令集."""
import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setGeometry(300, 300, 150, 250)
    w.setWindowTitle("Hello World")
    w.show()
    sys.exit(app.exec_())
