import sys
import sqlite3
import csv
# import logging
from Ui_toolbox import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QTableWidgetItem, QLabel,QInputDialog,QAbstractItemView
from PyQt6.QtCore import QDate, QDateTime, QTimer
from qt_material import apply_stylesheet


class myToolBox(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myToolBox, self).__init__()
        self.setupUi(self)
        # self.init_db()
        self.queryDB()
        self.init_items()

        # 创建状态栏时间显示
        self.time_label = QLabel(self)
        self.statusbar.addPermanentWidget(self.time_label)

        # 创建定时器，每秒更新一次时间
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 1000毫秒 = 1秒

        # logging.basicConfig(
        #     level=logging.DEBUG,  # 记录所有级别的日志
        #     format='%(asctime)s - %(levelname)s - %(message)s',
        #     # filename='app.log', # 如果取消这行注释，日志会写入文件
        #     # filemode='w'      # 'w' 表示覆盖写入, 'a' 表示追加写入
        # )

        # 初始化时间显示
        self.update_time()

        

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
        if pages == 4:
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
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
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

    def update_time(self):
        """Updates the time display in the status bar."""
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        self.time_label.setText(current_time)

    def init_items(self):
        """
        Purpose:初始化表格显示，读取csv文件。
        """
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.dateEdit_2.setDate(QDate.currentDate())
        # 初始化表格数据
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setHorizontalHeaderLabels(["物品名称", "购买/更换时间", "可用时长（天）"])

        # 从CSV文件读取数据
        try:
            with open("items.csv", "r", encoding="utf-8") as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # 跳过表头
                for row in csv_reader:
                    if len(row) == 3:  # 确保每行有3列数据
                        self.tableWidget_2.insertRow(self.tableWidget_2.rowCount())
                        for col, val in enumerate(row):
                            item = QTableWidgetItem(str(val if val is not None else ""))
                            self.tableWidget_2.setItem(self.tableWidget_2.rowCount()-1, col, item)
                print("数据已读取")
        except FileNotFoundError:
            print("items.csv文件未找到")
        except Exception as e:
            print(f"读取CSV文件时出错: {e}")

    # end def

    def add_item(self):
        """
        Purpose: 添加物品 
        """
        item_name = self.lineEdit_name.text()
        item_data = self.dateEdit_2.date().toString("yyyy-MM-dd")
        item_leftdays = self.lineEdit_days.text()

        data = [item_name, item_data, item_leftdays]
        # 将数据写入CSV文件
        try:
            with open("items.csv", "a", encoding="utf-8", newline="") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(data)
                QMessageBox.information(self, "成功", "数据已写入")
        except Exception as e:
            print(f"写入CSV文件时出错: {e}")
        self.tableWidget_2.setRowCount(0)
        self.init_items()
    def query_item_fromcsv(self):
        """
        Purpose: 
        """
        self.tableWidget_2.setRowCount(0)
        self.init_items()
        QMessageBox.information(self, "成功", "数据已刷新")

    def modify_item(self):
        """
        Purpose: 修改选中行数据，并存储到csv文件中
        """
        selected_rows = self.tableWidget_2.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "警告", "请先选择要修改的行")
            return

        # 获取第一个选中的行（假设只能修改一行）
        row = selected_rows[0].row()

        # 获取当前行的数据
        current_data = []
        for col in range(3):
            item = self.tableWidget_2.item(row, col)
            current_data.append(item.text() if item else "")

        # 这里可以添加修改数据的逻辑，例如弹出一个对话框让用户输入新值
        # 为了简化，这里直接使用当前数据（实际应用中应该让用户输入新值）
        # new_data = current_data  # 实际应用中应该替换为用户输入的新值
        # 弹出对话框让用户输入新值
        new_item_name, ok1 = QInputDialog.getText(self, '修改物品名称', '请输入新的物品名称:', text=current_data[0])
        new_item_data, ok2 = QInputDialog.getText(self, '修改物品日期', '请输入新的日期 (yyyy-MM-dd):', text=current_data[1])
        new_item_leftdays, ok3 = QInputDialog.getText(self, '修改剩余天数', '请输入新的剩余天数:', text=current_data[2])

        # 检查用户是否点击了确定按钮
        if ok1 and ok2 and ok3:
            new_data = [new_item_name, new_item_data, new_item_leftdays]
        else:
            # 如果用户取消，保持原数据不变
            new_data = current_data

        # 从CSV文件中读取所有数据
        try:
            with open("items.csv", "r", encoding="utf-8") as file:
                csv_reader = csv.reader(file)
                data = list(csv_reader)

            # 更新指定行的数据（跳过表头）
            if row + 1 < len(data):  # +1 因为第一行是表头
                data[row + 1] = new_data

            # 将更新后的数据写回CSV文件
            with open("items.csv", "w", encoding="utf-8", newline="") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data)

            QMessageBox.information(self, "成功", "数据已修改")
            # 刷新表格
            self.tableWidget_2.setRowCount(0)
            self.init_items()
        except Exception as e:
            print(f"修改CSV文件数据时出错: {e}")

    def delete_item(self):
        """
        Purpose:
        """
        # 获取选中的行
        selected_rows = self.tableWidget_2.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "警告", "请先选择要删除的行")
            return

        # 收集要删除的行的数据
        rows_to_delete = sorted([row.row() for row in selected_rows], reverse=True)

        # 从表格中删除行
        for row in rows_to_delete:
            self.tableWidget_2.removeRow(row)

        # 从CSV文件中删除对应的数据
        try:
            # 读取所有数据
            with open("items.csv", "r", encoding="utf-8") as file:
                csv_reader = csv.reader(file)
                data = list(csv_reader)

            # 过滤掉要删除的数据
            new_data = []
            for row in data[1:]:  # 跳过表头
                # 检查该行是否在表格中（这里假设表格中的数据是唯一的，可以根据实际需求调整）
                # 由于我们无法直接比较，这里简化处理：重新写入所有未被选中的行
                pass

            # 更准确的方法是重新构建数据，排除被删除的行
            # 由于我们无法直接获取被删除行的内容，这里采用另一种方法：
            # 重新读取表格中的数据并写回CSV
            with open("items.csv", "w", encoding="utf-8", newline="") as file:
                csv_writer = csv.writer(file)
                # 写入表头
                csv_writer.writerow(["物品名称", "购买/更换时间", "可用时长（天）"])
                # 重新写入表格中的所有数据
                for row in range(self.tableWidget_2.rowCount()):
                    row_data = []
                    for col in range(3):
                        item = self.tableWidget_2.item(row, col)
                        row_data.append(item.text() if item else "")
                    csv_writer.writerow(row_data)

            QMessageBox.information(self, "成功", "数据已删除")
        except Exception as e:
            print(f"删除CSV文件数据时出错: {e}")

    # end def


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myToolBox()
    # 使用qt_material主题美化
    # apply_stylesheet(app, theme='dark_blue.xml')
    w.show()
    sys.exit(app.exec())
