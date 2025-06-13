'''
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import QThread, pyqtSignal
import sys
import time
from datetime import datetime

class ClockThread(QThread):
    # 自定义信号，传递当前时间字符串
    time_signal = pyqtSignal(str)
    stop_signal = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self._running = True
    
    def run(self):
        while self._running:
            now = datetime.now().strftime("%H:%M:%S")
            self.time_signal.emit(now)   # 发出信号，传递当前时间
            time.sleep(1)                # 每秒刷新一次

    def stop(self):
        self._running = False

class ClockWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QThread 时钟示例")
        self.label = QLabel("00:00:00", self)
        self.label.setStyleSheet("font-size: 40px; qproperty-alignment: 'AlignCenter';")
        self.start_btn = QPushButton("启动")
        self.stop_btn = QPushButton("停止")
        self.stop_btn.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.start_btn)
        layout.addWidget(self.stop_btn)
        self.setLayout(layout)

        self.clock_thread = None
        self.start_btn.clicked.connect(self.start_clock)
        self.stop_btn.clicked.connect(self.stop_clock)

    def start_clock(self):
        if self.clock_thread is None or not self.clock_thread.isRunning():
            self.clock_thread = ClockThread()
            self.clock_thread.time_signal.connect(self.update_time)
            self.clock_thread.start()
            self.start_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)
    
    def stop_clock(self):
        if self.clock_thread is not None:
            self.clock_thread.stop()
            self.clock_thread.wait()
            self.start_btn.setEnabled(True)
            self.stop_btn.setEnabled(False)
            
    def update_time(self, timestr):
        self.label.setText(timestr)

    def closeEvent(self, event):
        if self.clock_thread is not None:
            self.clock_thread.stop()
            self.clock_thread.wait()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ClockWindow()
    win.show()
    sys.exit(app.exec())

'''

# import logging

# # 使用 basicConfig 进行快速配置
# # level: 设置记录的最低级别
# # format: 设置输出格式
# # filename: 如果提供，日志将写入文件而不是控制台
# logging.basicConfig(
#     level=logging.DEBUG,  # 记录所有级别的日志
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     # filename='app.log', # 如果取消这行注释，日志会写入文件
#     # filemode='w'      # 'w' 表示覆盖写入, 'a' 表示追加写入
# )

# logging.debug("这是一个 debug 信息，用于诊断。")
# logging.info("程序正常启动，一切就绪。")
# logging.warning("配置文件未找到，使用默认设置。")
# logging.error("无法连接到数据库。")
# logging.critical("严重错误：磁盘空间不足，程序即将关闭。")

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QCalendarWidget
from PyQt6.QtGui import QTextCharFormat, QColor
from PyQt6.QtCore import QDate

class MultiSelectCalendar(QCalendarWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.selected_dates = set()
        self.selection_format = QTextCharFormat()
        self.selection_format.setBackground(QColor("lightblue"))

        # 设置点击选择功能
        self.clicked.connect(self.toggle_date)

    def toggle_date(self, date):
        if date in self.selected_dates:
            self.selected_dates.remove(date)
            # 恢复为普通显示
            self.setDateTextFormat(date, QTextCharFormat())
        else:
            self.selected_dates.add(date)
            self.setDateTextFormat(date, self.selection_format)

    def get_selected_dates(self):
        # 返回所有已选日期
        return sorted(self.selected_dates)

# 使用方法
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("多选日期演示")
        widget = QWidget()
        layout = QVBoxLayout(widget)

        self.calendar = MultiSelectCalendar()
        self.label = QLabel("所选日期：")
        self.button = QPushButton("获取已选日期")
        layout.addWidget(self.calendar)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setCentralWidget(widget)

        self.button.clicked.connect(self.show_dates)

    def show_dates(self):
        dates = self.calendar.get_selected_dates()
        # 存储格式：可以转字符串、写入文件等
        dates_text = ', '.join([d.toString("yyyy-MM-dd") for d in dates])
        self.label.setText("所选日期：" + dates_text)
        # 存储举例
        # with open('selected_dates.txt', 'w', encoding='utf-8') as f:
        #     for d in dates:
        #         f.write(d.toString("yyyy-MM-dd") + '\n')

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

