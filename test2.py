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