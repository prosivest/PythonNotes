import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QStackedWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)

class Window1(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        label = QLabel("这是窗口1")
        button = QPushButton("切换到窗口2")
        button.clicked.connect(self.switch_to_window2)
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)

    def switch_to_window2(self):
        self.stacked_widget.setCurrentWidget(window2)

class Window2(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        label = QLabel("这是窗口2")
        button = QPushButton("切换到窗口1")
        button.clicked.connect(self.switch_to_window1)
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)

    def switch_to_window1(self):
        self.stacked_widget.setCurrentWidget(window1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()

    # 创建窗口1和窗口2
    window1 = Window1(stacked_widget)
    window2 = Window2(stacked_widget)

    # 将窗口添加到QStackedWidget中
    stacked_widget.addWidget(window1)
    stacked_widget.addWidget(window2)

    # 设置初始显示的窗口
    stacked_widget.setCurrentWidget(window1)

    # 显示主窗口
    stacked_widget.setWindowTitle("PyQt6 QStackedWidget 示例")
    stacked_widget.resize(400, 300)
    stacked_widget.show()

    sys.exit(app.exec())