import sys
import sqlite3
from Ui_toolbox import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox,QTableWidgetItem
from PyQt6.QtCore import QDate, QDateTime
from qt_material import apply_stylesheet


class myToolBox(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myToolBox, self).__init__()
        self.setupUi(self)
        # self.init_db()
        self.queryDB()

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

    def init_db(self):
        """
        Purpose: Creates the database and table if they don't exist.
        """
        try:
            conn = sqlite3.connect('mydb.db')
            cursor = conn.cursor()

            # 检查表是否存在
            cursor.execute("""
                SELECT count(name) FROM sqlite_master 
                WHERE type='table' AND name='tests'
            """)

            if cursor.fetchone()[0] == 0:  # 表不存在
                cursor.execute("""
                    CREATE TABLE tests (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        type TEXT NOT NULL,
                        amount integer NOT NULL,
                        note TEXT
                    )
                """)
                conn.commit()
                print("数据表已创建")
            else:
                print("数据表已存在，连接成功")

            return conn

        except Exception as e:
            QMessageBox.critical(None, "数据库错误", f"数据库操作失败: {str(e)}")
            return None
    # end def

    # end def
    def addDB(self):
        """
        Purpose: arg
        """
        # 获取输入内容（假设从某个输入框获取，这里需要根据实际UI调整）
        type_text = self.comboBox.currentText()
        num_text = self.num_db.text()
        input_content = self.text_db.text() 

        # 连接数据库
        conn = self.init_db()
        if conn:
            cursor = conn.cursor()
            # 插入数据到数据库
            cursor.execute(
                """
                INSERT INTO tests (type, amount, note)
                VALUES (?, ?, ?)
            """,
                (type_text, num_text, input_content),
            )  
            conn.commit()
            conn.close()
            QMessageBox.information(self, "成功", "数据已插入数据库")
            self.queryDB()
        else:
            print("数据库连接失败OR输入为空")

    def delDB(self): 
        """
        Purpose: Deletes the selected item from the database based on the selected row in the table widget.
        """
        selected_row = self.tableWidget.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "警告", "请先选择要删除的行")
            return

        # Get the ID of the selected item
        item_id = self.tableWidget.item(selected_row, 0)
        if not item_id or not item_id.text():
            QMessageBox.warning(self, "警告", "无法获取选中行的ID")
            return

        id_to_delete = int(item_id.text())
        reply = QMessageBox.question(
            self,
            "确认删除",
            "确定要删除选中的行吗？",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if reply == QMessageBox.StandardButton.Yes:
            # Connect to the database
            conn = self.init_db()
            if conn:
                cursor = conn.cursor()
                # Delete the item from the database
                cursor.execute("DELETE FROM tests WHERE id = ?", (id_to_delete,))
                conn.commit()
                conn.close()

                # Remove the row from the table widget
                self.tableWidget.removeRow(selected_row)
                QMessageBox.information(self, "成功", "数据已从数据库删除")
            else:
                print("数据库连接失败")

    def queryDB(self):
        """Queries all items from the database and displays them in the table widget."""
        try:
            conn = self.init_db()
            if conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, type, amount, note FROM tests")
                rows = cursor.fetchall()
                self.tableWidget.setRowCount(0)
                self.tableWidget.setColumnCount(4)  # 明确设置列数
                self.tableWidget.setHorizontalHeaderLabels(["ID", "类型", "数量", "备注"])

                for row_number, row_data in enumerate(rows):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        item = QTableWidgetItem(str(data if data is not None else ""))
                        self.tableWidget.setItem(row_number, column_number, item)

                conn.close()
            else:
                print("数据库连接失败")
        except Exception as e:
            print(f"查询数据库时出错: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myToolBox()
    # 使用qt_material主题美化
    # apply_stylesheet(app, theme='dark_blue.xml')
    w.show()
    sys.exit(app.exec())
