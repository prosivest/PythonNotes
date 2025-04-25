import sys
from PyQt6.QtWidgets import QApplication,QWidget, QTabWidget,QLabel,QCheckBox,QPushButton ,QFormLayout,QLineEdit
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import QDate,QDateTime

class myTabWidget(QTabWidget):
    def __init__(self):
        """
        Purpose: 
        """
        super().__init__()
        self.initUI()
    def initUI(self):
        """
        Purpose: 
        """
        self.setGeometry(300,300,360,160)
        self.setWindowTitle("我的QTabwidget测试")
        self.setTabPosition(QTabWidget.TabPosition.North)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.addTab(self.tab1,"周数计算")
        self.addTab(self.tab2,"天/周数计算")
        self.tab1UI()
        self.tab2UI()
        # end def
    
    def tab1UI(self):
        """
        Purpose: 
        """
        flayout = QFormLayout()
        self.acc_day = QLineEdit()
        self.acc_day.setValidator(QIntValidator())
        self.acc_day.setMaxLength(3)
        self.acc_week = QLineEdit()
        self.btn = QPushButton('计算')
        self.btn.clicked.connect(self.clickfunc)
        flayout.addRow('天数：',self.acc_day)
        flayout.addRow('周数：',self.acc_week)
        flayout.addRow(self.btn)
        self.tab1.setLayout(flayout)

        # end def
    
    def tab2UI(self):
        """
        Purpose: 
        """
        flayout = QFormLayout()
        self.days = QLineEdit()
        self.weeks = QLineEdit()
        self.btn2 = QPushButton('ok')
        self.btn2.clicked.connect(self.cal_weeks)
        flayout.addRow('天数',self.days)
        flayout.addRow('周数',self.weeks)
        flayout.addRow(self.btn2)
        self.tab2.setLayout(flayout)

        # end def
        
    def clickfunc(self):
        """
        Purpose: 
        """
        week = int(self.acc_day.text())//7
        day = int(self.acc_day.text())%7
        self.acc_week.setText('%d周%d天'%(week,day))
    # end def
    
    def cal_weeks(self):
        """
        Purpose: 
        """
        now = QDate.currentDate()
        xday = QDate(2024,10,30)
        a = xday.daysTo(now)
        week = (a)//7
        day = (a)%7
        self.days.setText(str(a))
        self.weeks.setText('%d周%d天'%(week,day))


        
    # end def
    # end default constructor

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w= myTabWidget()
    w.show()
    sys.exit(app.exec())
