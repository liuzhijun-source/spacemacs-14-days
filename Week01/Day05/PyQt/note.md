# PyQt 学习笔记
## PyQt5 的主要模块

PyQt5类分为很多模块，主要模块有：

- QtCore 包含了核心的非GUI的功能。主要和时间、文件与文件夹、各种数据、流、URLs、mime类文件、进程与线程一起使用。
- QtGui 包含了窗口系统、事件处理、2D图像、基本绘画、字体和文字类。
- QtMultimedia
- QtBluetooth
- QtNetwork
- QtPositioning
- Enginio
- QtWebSockets
- QtWebKit
- QtWebKitWidgets
- QtXml
- QtSvg
- QtSql
- QtTest

## HelloWorld
### 一个简单的窗口

```python
  import sys
  from PyQt5.QtWidgets import QApplication, QWidget

  if __name__ == "__main__":
      app = QApplication(sys.argv)
      w = QWidget()
      w.resize(250, 150)
      w.move(300, 300)
      w.setWindowTitle("Hello World")
      w.show()

      sys.exit(app.exec_())
```

上面的代码，能展示出一个小窗口

```python
    import sys
    from PyQt5.QtWidgets import QApplication, QWidget
```

这里引入了PyQt5.QtWidgets模块，这个模块包含了基本的组件

```python
  app = QApplication(sys.argv)
```

每个PyQt5应用都必须创建一个应用对象。sys.argv是一组命令行参数的列表，Python可以在shell里面运行，这个参数提供对脚本控制的功能

**每创建一个PyQt5应用，就必须要写这个，sys.argv提供对python代码的控制功能**

```python
  w = QWidget()
```

QWidget控件是一个用户界面的基本控件，它提供了基本的应用构造器。默认情况下，构造器是没有父级的，没有父级的构造器被称为窗口（window）。

resize方法可以用来修改窗口的大小， `resize(250, 150)`，第一个参数是窗口的宽，第二个参数是窗口的长， `move` 用于修改窗口的位置，接收一个坐标。 `setWindowTitle()` 用来修改窗口的标题， `show` 让窗口在桌面上显示出来。

最后，我们进入了应用的主循环中，事件处理器这个时候开始工作。主循环从窗口上接收事件，并把事件派发到应用控件里。当调用 `exit()` 方法或直接销毁主控件时，主循环就会结束。 `sys.exit()` 方法能确保主循环安全退出。外部环境会收到主控件如何结束的信息。

- `setGeometry()`

这个方法相当于`resize()`和`move()`的合体，参数分别是屏幕坐标的x、y和窗口的宽、高,

### 窗口图标

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

- `setWindowIcon(QIcon("web.png"))**

这个方法用来设置窗口的图标，`QIcon(**`填写窗口的路径

### 提示框

```python
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

- `QToolTip.setFont(QFont('SansSerif', 10))`

用来设置ToolTip的字体

- `setToolTip()`

用来设置 ToolTip，当你吧光标放在窗口上时，便会显示这个

- `QPushButton(name, self)`

用来放置一个按钮，name 接受一个字符串，同时可以使用`setToolTip()`来指定按钮的提示内容，可以使用富文本格式的内容

```python
btn.resize(btn.sizeHint())
btn.move(50, 50)
```

创建一个按钮，并且为按钮添加了一个提示框，`move()`可以移动按钮的位置，`resize()`可以用来设置按钮的大小，sizeHint（）提供了一个默认的按钮的大小
