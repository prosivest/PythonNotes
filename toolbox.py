import sys
from Ui_toolbox import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QWidget,QMainWindow
from PyQt6.QtCore import QDate,QDateTime


class myToolBox(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myToolBox,self).__init__()
        self.setupUi(self)

    def caldays(self):
        now = QDate.currentDate()
        # xday = self.dateEdit.date().toString('yyyy-MM-dd')
        xday = self.dateEdit.date()
        days = xday.daysTo(now)
        self.label_3.setText('%d天'%(days))
        week = days//7
        day = days%7
        self.label_5.setText('%d周%d天'%(week,day))

        
    # end def
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w= myToolBox()
    w.show()
    sys.exit(app.exec())