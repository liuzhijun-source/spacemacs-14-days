"""提供控制参数."""
import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QWidget


class example(QWidget):
    """create a qt program."""

    def __init__(self):
        """Init the Qt program."""
        super().__init__()

        self.initUI()

    def initUI(self):
        """绘制窗口."""
        self.setToolTip("This is a QWidget widget")

        btn = QPushButton("Place your cursor here", self)
        btn.setToolTip("This is a QPushButton widget")
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        btn2 = QPushButton("Hello, Click me", self)
        btn2.setToolTip("Hello, Click me")
        btn2.resize(btn.sizeHint())
        btn2.move(50, 100)

        btn3 = QPushButton("这是一个以中文显示的按钮", self)
        btn3.setToolTip("這是以繁體中文顯示的說明")
        btn3.resize(btn.sizeHint())
        btn3.move(50, 150)

        btn4 = QPushButton("This is a botton", self)
        btn4.setToolTip('你好，我是按钮')
        btn4.resize(btn.sizeHint())
        btn4.move(50, 200)

        btn5 = QPushButton("其实我还是很悠闲的", self)
        btn5.setToolTip("还记得我吗")
        btn5.resize(btn.sizeHint())
        btn5.move(50, 250)

        btn6 = QPushButton("我是一个按钮", self)
        btn6.setToolTip("你好，我是按钮")
        btn6.resize(btn.sizeHint())
        btn6.move(50, 300)

        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle("Tooltips")
        self.show()


app = QApplication(sys.argv)
eg = example()
sys.exit(app.exec_())
