# Form implementation generated from reading ui file 'f:\PythonNotes\toolbox.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 560))
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 50, 341, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.listWidget = QtWidgets.QListWidget(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 50, 591, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dateEdit.setFont(font)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 10, 30), QtCore.QTime(8, 0, 0)))
        self.dateEdit.setDate(QtCore.QDate(2024, 10, 30))
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(100, 150, 591, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=self.tab_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(100, 260, 591, 81))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.pushButton = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(270, 370, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.tab_3)
        self.tableWidget.setGeometry(QtCore.QRect(0, 140, 791, 391))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.tab_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 0, 391, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.num_db = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.num_db.setObjectName("num_db")
        self.verticalLayout_2.addWidget(self.num_db)
        self.text_db = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.text_db.setObjectName("text_db")
        self.verticalLayout_2.addWidget(self.text_db)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.tab_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(540, 0, 121, 131))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.add_btn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.add_btn.setObjectName("add_btn")
        self.verticalLayout_3.addWidget(self.add_btn)
        self.del_btn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.del_btn.setObjectName("del_btn")
        self.verticalLayout_3.addWidget(self.del_btn)
        self.query_btn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.query_btn.setObjectName("query_btn")
        self.verticalLayout_3.addWidget(self.query_btn)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.tab_4)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 150, 771, 371))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.tab_4)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 10, 371, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(parent=self.gridLayoutWidget)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setDate(QtCore.QDate(2025, 1, 1))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout.addWidget(self.dateEdit_2, 1, 1, 1, 1)
        self.lineEdit_days = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit_days.setObjectName("lineEdit_days")
        self.gridLayout.addWidget(self.lineEdit_days, 2, 1, 1, 1)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=self.tab_4)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(480, 10, 131, 131))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_add = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_4)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout_4.addWidget(self.pushButton_add)
        self.pushButton_modify = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_4)
        self.pushButton_modify.setObjectName("pushButton_modify")
        self.verticalLayout_4.addWidget(self.pushButton_modify)
        self.pushButton_delete = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_4)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.verticalLayout_4.addWidget(self.pushButton_delete)
        self.pushButton_query = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_4)
        self.pushButton_query.setObjectName("pushButton_query")
        self.verticalLayout_4.addWidget(self.pushButton_query)
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtGui.QAction(parent=MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionsetting = QtGui.QAction(parent=MainWindow)
        self.actionsetting.setObjectName("actionsetting")
        self.menu.addAction(self.actionopen)
        self.menu.addAction(self.actionsetting)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        self.pushButton.clicked.connect(MainWindow.caldays) # type: ignore
        self.listWidget.itemClicked['QListWidgetItem*'].connect(MainWindow.gotopages) # type: ignore
        self.add_btn.clicked.connect(MainWindow.addDB) # type: ignore
        self.del_btn.clicked.connect(MainWindow.delDB) # type: ignore
        self.query_btn.clicked.connect(MainWindow.queryDB) # type: ignore
        self.pushButton_add.clicked.connect(MainWindow.add_item) # type: ignore
        self.pushButton_query.clicked.connect(MainWindow.query_item_fromcsv) # type: ignore
        self.pushButton_delete.clicked.connect(MainWindow.delete_item) # type: ignore
        self.pushButton_modify.clicked.connect(MainWindow.modify_item) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "个人工具箱"))
        self.label_6.setText(_translate("MainWindow", "我的个人工具箱"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "天数计算"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "数据库"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "到期管理"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "其他"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "首页"))
        self.label.setText(_translate("MainWindow", "选择日期"))
        self.label_2.setText(_translate("MainWindow", "距今天数"))
        self.label_3.setText(_translate("MainWindow", "天"))
        self.label_4.setText(_translate("MainWindow", "距今周数"))
        self.label_5.setText(_translate("MainWindow", "0周0天"))
        self.pushButton.setText(_translate("MainWindow", "计算"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "天数计算"))
        self.comboBox.setItemText(0, _translate("MainWindow", "in"))
        self.comboBox.setItemText(1, _translate("MainWindow", "out"))
        self.add_btn.setText(_translate("MainWindow", "添加"))
        self.del_btn.setText(_translate("MainWindow", "删除"))
        self.query_btn.setText(_translate("MainWindow", "查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "数据库"))
        self.label_9.setText(_translate("MainWindow", "可用时长（天）"))
        self.label_8.setText(_translate("MainWindow", "购买/更换时间"))
        self.label_7.setText(_translate("MainWindow", "物品名称"))
        self.pushButton_add.setText(_translate("MainWindow", "添加"))
        self.pushButton_modify.setText(_translate("MainWindow", "修改"))
        self.pushButton_delete.setText(_translate("MainWindow", "删除"))
        self.pushButton_query.setText(_translate("MainWindow", "查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "到期管理"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "关于"))
        self.actionopen.setText(_translate("MainWindow", "打开"))
        self.actionsetting.setText(_translate("MainWindow", "设置"))
