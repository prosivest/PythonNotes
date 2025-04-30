import sys
from Ui_DialogTest import Ui_Dialog
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox,QDialog


class myDialog(QDialog,Ui_Dialog):
    def __init__(self):
        """
        Purpose: 
        """
        super(myDialog,self).__init__()
        self.setupUi(self)
    
    def show1(self):
        """
        Purpose: arg
        """
        
        QMessageBox.information(self,'提示',self.label.text())
        self.label.setText('111111111')
    
    def show2(self):
        """
        Purpose: arg
        """
        self.label.setText('testtest')
    # end def
        
    # end default constructor

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myDialog()
    w.show()
    sys.exit(app.exec())