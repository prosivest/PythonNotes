import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QTabWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QMessageBox,
)


# --- 工具类的基类或模板 ---
class BaseTool(QWidget):
    """
    所有工具都应该继承自这个基类或遵循类似的结构。
    每个工具都是一个 QWidget。
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()  # 每个工具负责设置自己的UI

    def setup_ui(self):
        """
        设置工具的用户界面。子类必须实现这个方法。
        """
        layout = QVBoxLayout(self)
        label = QLabel("这是一个基础工具的占位符。请在子类中实现 setup_ui 方法。", self)
        layout.addWidget(label)
        self.setLayout(layout)

    def get_tool_name(self):
        """
        返回工具的名称，用于 Tab 的标题。子类可以重写此方法。
        """
        return "未知工具"


# --- 示例工具 1: 简单的文本输入和显示工具 ---
class TextDisplayTool(BaseTool):
    def __init__(self, parent=None):
        super().__init__(parent)

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.input_label = QLabel("请输入文本:", self)
        layout.addWidget(self.input_label)

        self.text_input = QLineEdit(self)
        layout.addWidget(self.text_input)

        self.display_button = QPushButton("显示文本", self)
        self.display_button.clicked.connect(self.display_text)
        layout.addWidget(self.display_button)

        self.display_label = QLabel("显示区域:", self)
        layout.addWidget(self.display_label)

        layout.addStretch(1)  # 添加伸展器，让内容靠上

        self.setLayout(layout)

    def display_text(self):
        input_text = self.text_input.text()
        self.display_label.setText(f"显示区域: {input_text}")

    def get_tool_name(self):
        return "文本显示工具"


# --- 示例工具 2: 简单的信息框工具 ---
class MessageBoxTool(BaseTool):
    def __init__(self, parent=None):
        super().__init__(parent)

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.message_label = QLabel("点击按钮显示信息框:", self)
        layout.addWidget(self.message_label)

        self.show_button = QPushButton("显示信息框", self)
        self.show_button.clicked.connect(self.show_message)
        layout.addWidget(self.show_button)

        layout.addStretch(1)  # 添加伸展器

        self.setLayout(layout)

    def show_message(self):
        QMessageBox.information(self, "信息", "这是一个示例信息框！")

    def get_tool_name(self):
        return "信息框工具"


# --- 主应用窗口 ---
class PersonalToolbox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("个人工具箱")
        self.setGeometry(100, 100, 800, 600)  # 设置窗口大小和位置

        # 创建 Tab Widget 作为中心部件
        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        # 初始化并添加工具
        self.init_tools()

    def init_tools(self):
        """
        初始化并添加工具到工具箱。
        要添加新工具，只需在这里实例化你的工具类并调用 self.add_tool()
        """
        self.add_tool(TextDisplayTool())
        self.add_tool(MessageBoxTool())
        # self.add_tool(YourNewToolClass()) # 将来添加新工具的方式

    def add_tool(self, tool_widget: BaseTool):
        """
        将一个工具 (QWidget 实例) 添加到 Tab Widget 中。
        """
        if isinstance(tool_widget, QWidget):
            tab_title = (
                tool_widget.get_tool_name()
                if hasattr(tool_widget, "get_tool_name")
                else "新工具"
            )
            self.tab_widget.addTab(tool_widget, tab_title)
        else:
            print(f"警告: 尝试添加的不是一个 QWidget 实例: {type(tool_widget)}")


# --- 应用入口 ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    toolbox = PersonalToolbox()
    toolbox.show()
    sys.exit(app.exec())


# 测试
