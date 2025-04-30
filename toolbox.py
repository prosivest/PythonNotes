import sys
from Ui_toolbox import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from PyQt6.QtCore import QDate, QDateTime
from qt_material import apply_stylesheet


class myToolBox(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myToolBox, self).__init__()
        self.setupUi(self)

    def caldays(self):
        now = QDate.currentDate()
        # xday = self.dateEdit.date().toString('yyyy-MM-dd')
        xday = self.dateEdit.date()
        days = xday.daysTo(now)
        self.label_3.setText("%d天" % (days))
        week = days // 7
        day = days % 7
        self.label_5.setText("%d周%d天" % (week, day))

    def gotopages(self):
        pages = self.listWidget.currentRow() + 1
        if pages == 3:
            # comment:
            QMessageBox.information(
                self, "提示信息", self.listWidget.currentItem().text()
            )

        else:
            # comment:
            self.tabWidget.setCurrentIndex(pages)
        # end if

    # end def


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myToolBox()
    # 使用qt_material主题美化
    # apply_stylesheet(app, theme='dark_blue.xml')
    w.show()
    sys.exit(app.exec())
