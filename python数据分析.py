"""
Python数据分析平台
基于PyQt6框架开发的桌面应用程序，提供数据导入/导出、清洗转换、分析计算和可视化功能
"""
 
# 导入模块
import sys  # 系统相关功能
from PyQt6.QtWidgets import (  # PyQt6 GUI组件
    QApplication, QMainWindow, QLabel, QStatusBar, 
    QToolBar, QTableWidget, QTableWidgetItem, QMenu, QFileDialog,
    QInputDialog, QMessageBox
)
from PyQt6.QtGui import QAction  # 动作类
from PyQt6.QtCore import Qt  # Qt核心功能
import pandas as pd  # 数据处理库，用于CSV/Excel文件读取
import json  # JSON处理模块，用于JSON文件读取
import numpy as np  # 数值计算库
import matplotlib.pyplot as plt  # 数据可视化库，用于创建静态图表
import seaborn as sns  # 基于matplotlib的高级可视化库，提供更美观的统计图表
from sklearn import linear_model, preprocessing  # 机器学习库
import statsmodels.api as sm  # 统计分析库
 
 
class DataAnalysisPlatform(QMainWindow):
    """
    数据分析平台主窗口类
     
    属性:
        table_widget: QTableWidget - 中央数据表格显示区
        status_bar: QStatusBar - 底部状态栏
        toolbar: QToolBar - 主工具栏
    """
     
    def __init__(self):
        """初始化主窗口"""
        super().__init__()
         
        # 设置窗口标题和尺寸
        self.setWindowTitle("Python数据分析平台")
        self.setGeometry(100, 100, 1200, 800)  # x, y, width, height
         
        # 初始化UI组件
        self._init_ui()
         
    def _init_ui(self):
        """初始化用户界面"""
        # 创建中央表格部件
        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)
         
        # 创建状态栏
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("就绪")
         
        # 创建菜单栏
        self._create_menus()
         
        # 创建工具栏
        self._create_toolbar()
         
        # 设置表格右键菜单
        self.table_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_widget.customContextMenuRequested.connect(self._show_context_menu)
         
    def _create_menus(self):
        """创建菜单栏"""
        # 文件菜单
        file_menu = self.menuBar().addMenu("文件")
         
        # 打开动作
        open_action = QAction("打开", self)
        open_action.triggered.connect(self._open_file)
        file_menu.addAction(open_action)
         
        # 保存动作
        save_action = QAction("保存", self)
        save_action.triggered.connect(self._save_file)
        file_menu.addAction(save_action)
         
        # 编辑菜单
        edit_menu = self.menuBar().addMenu("编辑")
         
        # 排序动作
        sort_action = QAction("排序", self)
        sort_action.triggered.connect(self._sort_data)
        edit_menu.addAction(sort_action)
         
        # 筛选动作
        filter_action = QAction("筛选", self)
        filter_action.triggered.connect(self._filter_data)
        edit_menu.addAction(filter_action)
         
        # 帮助菜单
        help_menu = self.menuBar().addMenu("帮助")
         
        # 关于动作
        about_action = QAction("关于", self)
        about_action.triggered.connect(self._show_about)
        help_menu.addAction(about_action)
         
    def _create_toolbar(self):
        """创建工具栏"""
        self.toolbar = QToolBar("主工具栏")
        self.addToolBar(self.toolbar)
         
        # 添加工具按钮
        open_action = QAction("打开", self)
        open_action.triggered.connect(self._open_file)
        self.toolbar.addAction(open_action)
         
        save_action = QAction("保存", self)
        save_action.triggered.connect(self._save_file)
        self.toolbar.addAction(save_action)
         
        self.toolbar.addSeparator()
         
        sort_action = QAction("排序", self)
        sort_action.triggered.connect(self._sort_data)
        self.toolbar.addAction(sort_action)
         
        filter_action = QAction("筛选", self)
        filter_action.triggered.connect(self._filter_data)
        self.toolbar.addAction(filter_action)
         
        self.toolbar.addSeparator()
         
        analyze_action = QAction("分析", self)
        analyze_action.triggered.connect(self._data_analysis)
        self.toolbar.addAction(analyze_action)
         
        # 可视化按钮并连接信号槽
        visualize_action = QAction("可视化", self)
        visualize_action.triggered.connect(self._visualize_data)
        self.toolbar.addAction(visualize_action)
         
    def _copy_data(self):
        """复制选中单元格数据到剪贴板"""
        selected_items = self.table_widget.selectedItems()
        if not selected_items:
            self.status_bar.showMessage("没有选中要复制的数据")
            return
             
        # 获取选中单元格的文本内容
        data = []
        current_row = -1
         
        for item in selected_items:
            if item.row() != current_row:
                data.append([])
                current_row = item.row()
            data[-1].append(item.text())
         
        # 将数据转换为制表符分隔的字符串
        text = "\n".join("\t".join(row) for row in data)
         
        # 复制到剪贴板
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
        self.status_bar.showMessage(f"已复制 {len(selected_items)} 个单元格数据")
         
    def _paste_data(self):
        """从剪贴板粘贴数据到表格"""
        clipboard = QApplication.clipboard()
        text = clipboard.text()
         
        if not text:
            self.status_bar.showMessage("剪贴板中没有数据")
            return
             
        try:
            # 解析剪贴板数据（制表符分隔的行，换行符分隔的列）
            data = [row.split("\t") for row in text.split("\n") if row]
             
            # 获取当前选中单元格位置
            selected_items = self.table_widget.selectedItems()
            start_row = selected_items[0].row() if selected_items else 0
            start_col = selected_items[0].column() if selected_items else 0
             
            # 将数据粘贴到表格中
            for row_idx, row_data in enumerate(data):
                for col_idx, cell_data in enumerate(row_data):
                    target_row = start_row + row_idx
                    target_col = start_col + col_idx
                     
                    # 确保表格有足够的行和列
                    if target_row >= self.table_widget.rowCount():
                        self.table_widget.insertRow(target_row)
                    if target_col >= self.table_widget.columnCount():
                        self.table_widget.insertColumn(target_col)
                     
                    # 设置单元格数据
                    item = QTableWidgetItem(cell_data)
                    self.table_widget.setItem(target_row, target_col, item)
             
            self.status_bar.showMessage(f"已粘贴 {len(data)} 行数据")
        except Exception as e:
            self.status_bar.showMessage(f"粘贴失败: {str(e)}")
         
    def _show_context_menu(self, position):
        """显示表格右键菜单"""
        menu = QMenu()
         
        # 获取当前点击的行
        row = self.table_widget.rowAt(position.y())
        col = self.table_widget.columnAt(position.x())
         
        # 添加菜单项并连接功能
        copy_action = menu.addAction("复制")
        copy_action.triggered.connect(self._copy_data)
         
        paste_action = menu.addAction("粘贴")
        paste_action.triggered.connect(self._paste_data)
         
        menu.addSeparator()
         
        delete_action = menu.addAction("删除行")
        delete_action.triggered.connect(lambda: self._delete_row(row))
         
        insert_action = menu.addAction("插入行")
        insert_action.triggered.connect(lambda: self._insert_row(row))
         
        menu.addSeparator()
         
        add_col_action = menu.addAction("添加列")
        add_col_action.triggered.connect(self._add_column)
         
        remove_col_action = menu.addAction("删除列")
        remove_col_action.triggered.connect(self._remove_column)
         
        # 新增编辑列名功能
        if col >= 0:  # 确保点击的是有效的列
            edit_col_action = menu.addAction("编辑列名")
            edit_col_action.triggered.connect(lambda: self._edit_column_name(col))
         
        # 显示菜单
        menu.exec(self.table_widget.viewport().mapToGlobal(position))
         
    def _edit_column_name(self, col):
        """编辑指定列的列名"""
        from PyQt6.QtWidgets import QInputDialog
         
        # 获取当前列名
        current_name = self.table_widget.horizontalHeaderItem(col).text()
         
        # 弹出输入对话框
        new_name, ok = QInputDialog.getText(
            self,
            "编辑列名",
            "请输入新的列名:",
            text=current_name
        )
         
        if ok and new_name:
            # 更新列名
            self.table_widget.setHorizontalHeaderItem(col, QTableWidgetItem(new_name))
            self.status_bar.showMessage(f"已更新列名: {current_name} -> {new_name}")
 
    def _add_column(self):
        """在表格末尾添加新列"""
        col = self.table_widget.columnCount()
        self.table_widget.insertColumn(col)
        self.table_widget.setHorizontalHeaderItem(col, QTableWidgetItem(f"列{col+1}"))
        self.status_bar.showMessage(f"已添加第{col+1}列")
         
    def _remove_column(self):
        """删除当前选中列"""
        col = self.table_widget.currentColumn()
        if col >= 0:
            self.table_widget.removeColumn(col)
            self.status_bar.showMessage(f"已删除第{col+1}列")
        else:
            self.status_bar.showMessage("请先选择要删除的列")
         
    def _insert_row(self, row):
        """在指定位置插入新行"""
        self.table_widget.insertRow(row)
        # 初始化新行的单元格
        for col in range(self.table_widget.columnCount()):
            self.table_widget.setItem(row, col, QTableWidgetItem(""))
         
    def _delete_row(self, row):
        """删除指定行"""
        if row >= 0:
            self.table_widget.removeRow(row)
         
    def _open_file(self):
        """
        打开数据文件并加载到表格中
         
        支持格式: CSV/Excel/JSON
        功能: 通过文件对话框选择文件，读取数据并显示在表格中
        """
        from PyQt6.QtWidgets import QFileDialog  # 文件对话框组件
        import pandas as pd  # 数据处理库
        import json  # JSON处理模块
         
        # 设置文件过滤器，支持多种格式
        file_filter = "数据文件 (*.csv *.xlsx *.json);;CSV文件 (*.csv);;Excel文件 (*.xlsx);;JSON文件 (*.json)"
         
        # 弹出文件选择对话框
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "打开数据文件",  # 对话框标题
            "",  # 初始目录
            file_filter  # 文件过滤器
        )
         
        # 如果用户选择了文件
        if file_path:
            try:
                # 根据文件扩展名选择不同的读取方式
                if file_path.endswith('.csv'):
                    # 读取CSV文件
                    data = pd.read_csv(file_path)  # 使用pandas读取CSV
                elif file_path.endswith('.xlsx'):
                    # 读取Excel文件
                    data = pd.read_excel(file_path)  # 使用pandas读取Excel
                elif file_path.endswith('.json'):
                    # 读取JSON文件
                    with open(file_path, 'r', encoding='utf-8') as f:
                        json_data = json.load(f)  # 加载JSON数据
                    data = pd.DataFrame(json_data)  # 转换为DataFrame
                else:
                    raise ValueError("不支持的文件格式")
                 
                # 清空现有表格
                self.table_widget.clear()
                 
                # 设置表格行列数
                self.table_widget.setRowCount(data.shape[0])  # 行数为数据行数
                self.table_widget.setColumnCount(data.shape[1])  # 列数为数据列数
                 
                # 设置表头
                self.table_widget.setHorizontalHeaderLabels(data.columns.tolist())
                 
                # 填充表格数据
                for i in range(data.shape[0]):  # 遍历每一行
                    for j in range(data.shape[1]):  # 遍历每一列
                        # 获取单元格值，处理NaN值为空字符串
                        value = str(data.iloc[i, j]) if not pd.isna(data.iloc[i, j]) else ""
                        # 创建表格项并设置值
                        item = QTableWidgetItem(value)
                        self.table_widget.setItem(i, j, item)
                 
                # 显示成功消息
                self.status_bar.showMessage(f"成功加载文件: {file_path}")
                 
            except Exception as e:
                # 显示错误消息
                self.status_bar.showMessage(f"加载文件失败: {str(e)}")
         
    def _save_file(self):
        """
        保存表格数据到文件
         
        支持格式: CSV/Excel/JSON
        功能: 通过文件对话框选择保存路径和格式，将表格数据保存到指定文件
        """
        from PyQt6.QtWidgets import QFileDialog  # 文件对话框组件
        import pandas as pd  # 数据处理库
        import json  # JSON处理模块
         
        # 检查表格是否有数据
        if self.table_widget.rowCount() == 0 or self.table_widget.columnCount() == 0:
            self.status_bar.showMessage("表格中没有数据可保存")
            return
         
        # 设置文件过滤器，支持多种格式
        file_filter = "CSV文件 (*.csv);;Excel文件 (*.xlsx);;JSON文件 (*.json)"
         
        # 弹出文件保存对话框
        file_path, selected_filter = QFileDialog.getSaveFileName(
            self,
            "保存数据文件",  # 对话框标题
            "",  # 初始目录
            file_filter  # 文件过滤器
        )
         
        # 如果用户选择了保存路径
        if file_path:
            try:
                # 从表格中提取数据
                data = []
                headers = []
                 
                # 获取表头
                for col in range(self.table_widget.columnCount()):
                    header = self.table_widget.horizontalHeaderItem(col)
                    headers.append(header.text() if header else f"Column{col+1}")
                 
                # 获取表格数据
                for row in range(self.table_widget.rowCount()):
                    row_data = []
                    for col in range(self.table_widget.columnCount()):
                        item = self.table_widget.item(row, col)
                        row_data.append(item.text() if item else "")
                    data.append(row_data)
                 
                # 创建DataFrame
                df = pd.DataFrame(data, columns=headers)
                 
                # 根据选择的文件格式保存数据
                if selected_filter == "CSV文件 (*.csv)" or file_path.endswith('.csv'):
                    # 保存为CSV文件
                    df.to_csv(file_path, index=False, encoding='utf-8-sig')
                elif selected_filter == "Excel文件 (*.xlsx)" or file_path.endswith('.xlsx'):
                    # 保存为Excel文件
                    df.to_excel(file_path, index=False)
                elif selected_filter == "JSON文件 (*.json)" or file_path.endswith('.json'):
                    # 保存为JSON文件
                    df.to_json(file_path, orient='records', force_ascii=False, indent=4)
                else:
                    raise ValueError("不支持的文件格式")
                 
                # 显示成功消息
                self.status_bar.showMessage(f"数据已成功保存到: {file_path}")
                 
            except Exception as e:
                # 显示错误消息
                self.status_bar.showMessage(f"保存文件失败: {str(e)}")
         
    def _sort_data(self):
        """
        对表格数据进行多列排序
         
        功能: 弹出对话框让用户选择最多3列进行组合排序，支持升序/降序
        """
        from PyQt6.QtWidgets import (QInputDialog, QDialog, QVBoxLayout, 
                                  QLabel, QComboBox, QDialogButtonBox, QHBoxLayout)
         
        # 检查表格是否有数据
        if self.table_widget.rowCount() == 0 or self.table_widget.columnCount() == 0:
            self.status_bar.showMessage("表格中没有数据可排序")
            return
             
        # 创建排序对话框
        dialog = QDialog(self)
        dialog.setWindowTitle("多列排序")
        layout = QVBoxLayout()
         
        # 添加最多3个排序条件
        for i in range(3):
            row_layout = QHBoxLayout()
            row_layout.addWidget(QLabel(f"排序条件 {i+1}:"))
             
            # 列选择下拉框
            col_combo = QComboBox()
            col_combo.setObjectName(f"col_combo_{i}")
            col_combo.addItems([self.table_widget.horizontalHeaderItem(j).text() 
                              for j in range(self.table_widget.columnCount())])
            row_layout.addWidget(col_combo)
             
            # 排序方式下拉框
            order_combo = QComboBox()
            order_combo.setObjectName(f"order_combo_{i}")
            order_combo.addItems(["升序", "降序"])
            row_layout.addWidget(order_combo)
             
            layout.addLayout(row_layout)
         
        # 添加确定/取消按钮
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | 
                                 QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
         
        dialog.setLayout(layout)
         
        if dialog.exec() == QDialog.DialogCode.Accepted:
            # 获取排序条件并执行排序
            self.status_bar.showMessage("正在排序数据...")
             
            # 获取当前表格数据
            data = []
            for row in range(self.table_widget.rowCount()):
                row_data = []
                for col in range(self.table_widget.columnCount()):
                    item = self.table_widget.item(row, col)
                    row_data.append(item.text() if item else "")
                data.append(row_data)
             
            # 转换为DataFrame以便排序
            headers = [self.table_widget.horizontalHeaderItem(col).text() 
                      for col in range(self.table_widget.columnCount())]
            df = pd.DataFrame(data, columns=headers)
             
            # 获取排序条件
            sort_conditions = []
            for i in range(3):
                col_combo = dialog.findChild(QComboBox, f"col_combo_{i}")
                order_combo = dialog.findChild(QComboBox, f"order_combo_{i}")
                 
                if col_combo and col_combo.currentText():
                    ascending = order_combo.currentText() == "升序"
                    sort_conditions.append((col_combo.currentText(), ascending))
             
            # 执行多列排序
            if sort_conditions:
                df = df.sort_values(
                    by=[col for col, _ in sort_conditions],
                    ascending=[asc for _, asc in sort_conditions]
                )
                 
                # 更新表格数据
                self.table_widget.setRowCount(len(df))
                for row in range(len(df)):
                    for col in range(len(df.columns)):
                        self.table_widget.setItem(row, col, 
                            QTableWidgetItem(str(df.iloc[row, col])))
                 
            self.status_bar.showMessage(f"已按{len(sort_conditions)}列排序完成")
        else:
            self.status_bar.showMessage("排序已取消")
         
 
         
    def _clean_data(self):
        """
        数据清洗功能
         
        功能: 对表格数据进行清洗处理，包括空值处理和数据整理
        参数: 无
        返回值: 无
        """
        from PyQt6.QtWidgets import QInputDialog, QMessageBox  # 输入对话框和消息框组件
         
        # 检查表格是否有数据
        if self.table_widget.rowCount() == 0 or self.table_widget.columnCount() == 0:
            self.status_bar.showMessage("表格中没有数据可清洗")
            return
             
        # 弹出对话框让用户选择清洗选项
        options = ["删除空行", "填充空值", "删除重复行", "数据类型转换"]
        option, ok = QInputDialog.getItem(
            self,
            "选择清洗选项",  # 对话框标题
            "请选择要执行的清洗操作:",  # 提示文本
            options,  # 选项列表
            0,  # 默认选中第一项
            False  # 不允许编辑
        )
         
        # 如果用户取消了选择
        if not ok:
            return
             
        # 根据用户选择执行不同的清洗操作
        try:
            if option == "删除空行":
                # 删除所有空行
                rows_to_remove = []
                for row in range(self.table_widget.rowCount()):
                    is_empty = True
                    for col in range(self.table_widget.columnCount()):
                        item = self.table_widget.item(row, col)
                        if item and item.text().strip():
                            is_empty = False
                            break
                    if is_empty:
                        rows_to_remove.append(row)
                 
                # 从后往前删除行，避免索引错乱
                for row in sorted(rows_to_remove, reverse=True):
                    self.table_widget.removeRow(row)
                 
                self.status_bar.showMessage(f"已删除 {len(rows_to_remove)} 个空行")
                 
            elif option == "填充空值":
                # 填充空值
                col, ok = QInputDialog.getInt(
                    self,
                    "选择列",
                    "请输入要填充空值的列号(从1开始):",
                    1,  # 默认值
                    1,  # 最小值
                    self.table_widget.columnCount(),  # 最大值
                    1  # 步长
                )
                 
                if not ok:
                    return
                     
                # 获取填充值
                value, ok = QInputDialog.getText(
                    self,
                    "输入填充值",
                    "请输入要填充的值:"
                )
                 
                if not ok:
                    return
                     
                # 填充空值
                col_index = col - 1
                filled_count = 0
                for row in range(self.table_widget.rowCount()):
                    item = self.table_widget.item(row, col_index)
                    if not item or not item.text().strip():
                        self.table_widget.setItem(row, col_index, QTableWidgetItem(value))
                        filled_count += 1
                 
                self.status_bar.showMessage(f"已填充 {filled_count} 个空值")
                 
            elif option == "删除重复行":
                # 删除重复行
                rows_to_remove = []
                seen_rows = set()
                 
                for row in range(self.table_widget.rowCount()):
                    row_data = []
                    for col in range(self.table_widget.columnCount()):
                        item = self.table_widget.item(row, col)
                        row_data.append(item.text() if item else "")
                     
                    row_tuple = tuple(row_data)
                    if row_tuple in seen_rows:
                        rows_to_remove.append(row)
                    else:
                        seen_rows.add(row_tuple)
                 
                # 从后往前删除行
                for row in sorted(rows_to_remove, reverse=True):
                    self.table_widget.removeRow(row)
                 
                self.status_bar.showMessage(f"已删除 {len(rows_to_remove)} 个重复行")
                 
            elif option == "数据类型转换":
                # 数据类型转换
                col, ok = QInputDialog.getInt(
                    self,
                    "选择列",
                    "请输入要转换数据类型的列号(从1开始):",
                    1,
                    1,
                    self.table_widget.columnCount(),
                    1
                )
                 
                if not ok:
                    return
                     
                # 选择目标类型
                types = ["整数", "浮点数", "字符串", "布尔值"]
                target_type, ok = QInputDialog.getItem(
                    self,
                    "选择目标类型",
                    "请选择要转换的数据类型:",
                    types,
                    0,
                    False
                )
                 
                if not ok:
                    return
                     
                # 执行转换
                col_index = col - 1
                converted_count = 0
                for row in range(self.table_widget.rowCount()):
                    item = self.table_widget.item(row, col_index)
                    if item and item.text().strip():
                        try:
                            text = item.text()
                            if target_type == "整数":
                                value = int(text)
                            elif target_type == "浮点数":
                                value = float(text)
                            elif target_type == "布尔值":
                                value = True if text.lower() in ["true", "1", "yes"] else False
                            else:  # 字符串
                                value = str(text)
                             
                            self.table_widget.setItem(row, col_index, QTableWidgetItem(str(value)))
                            converted_count += 1
                        except ValueError:
                            pass
                 
                self.status_bar.showMessage(f"已转换 {converted_count} 个值为 {target_type}")
                 
        except Exception as e:
            self.status_bar.showMessage(f"数据清洗失败: {str(e)}")
             
    def _filter_data(self):
        """
        对表格数据进行高级筛选
         
        功能: 弹出对话框让用户设置多条件筛选，支持运算符(=,>,<等)和逻辑组合(AND/OR)
        改进: 支持多条件组合筛选，简化操作流程
        """
        from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                                  QComboBox, QLineEdit, QDialogButtonBox, QPushButton,
                                  QScrollArea, QWidget, QGroupBox)
        from PyQt6.QtCore import Qt
         
        # 检查表格是否有数据
        if self.table_widget.rowCount() == 0 or self.table_widget.columnCount() == 0:
            self.status_bar.showMessage("表格中没有数据可筛选")
            return
             
        # 创建筛选对话框
        dialog = QDialog(self)
        dialog.setWindowTitle("高级筛选")
        dialog.resize(500, 400)
        layout = QVBoxLayout()
         
        # 创建滚动区域
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
         
        # 添加条件组
        condition_group = QGroupBox("筛选条件")
        condition_group_layout = QVBoxLayout()
         
        # 初始条件
        condition_widgets = []
         
        def add_condition():
            condition_widget = QWidget()
            condition_layout = QHBoxLayout()
             
            # 列选择下拉框
            col_combo = QComboBox()
            col_combo.addItems([self.table_widget.horizontalHeaderItem(j).text() 
                              for j in range(self.table_widget.columnCount())])
            condition_layout.addWidget(col_combo)
             
            # 运算符下拉框
            operator_combo = QComboBox()
            operator_combo.addItems(["=", ">", "<", "<=", ">=", "!=", "包含", "不包含", "开头为", "结尾为", "为空", "不为空"])
            condition_layout.addWidget(operator_combo)
             
            # 值输入框
            value_edit = QLineEdit()
            condition_layout.addWidget(value_edit)
             
            # 删除按钮
            delete_btn = QPushButton("删除")
            delete_btn.clicked.connect(lambda: remove_condition(condition_widget))
            condition_layout.addWidget(delete_btn)
             
            condition_widget.setLayout(condition_layout)
            condition_group_layout.addWidget(condition_widget)
            condition_widgets.append({
                "widget": condition_widget,
                "col_combo": col_combo,
                "operator_combo": operator_combo,
                "value_edit": value_edit
            })
         
        def remove_condition(widget):
            condition_group_layout.removeWidget(widget)
            widget.deleteLater()
            condition_widgets[:] = [cw for cw in condition_widgets if cw["widget"] != widget]
         
        # 添加初始条件
        add_condition()
         
        # 添加条件按钮
        add_btn = QPushButton("添加条件")
        add_btn.clicked.connect(add_condition)
        condition_group_layout.addWidget(add_btn)
         
        condition_group.setLayout(condition_group_layout)
        scroll_layout.addWidget(condition_group)
         
        # 添加逻辑组合选项
        logic_group = QGroupBox("逻辑组合")
        logic_layout = QVBoxLayout()
        logic_combo = QComboBox()
        logic_combo.addItems(["AND", "OR"])
        logic_layout.addWidget(logic_combo)
        logic_group.setLayout(logic_layout)
        scroll_layout.addWidget(logic_group)
         
        scroll.setWidget(scroll_content)
        layout.addWidget(scroll)
         
        # 添加确定/取消按钮
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | 
                                 QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
         
        dialog.setLayout(layout)
         
        if dialog.exec() == QDialog.DialogCode.Accepted:
            # 获取筛选条件并执行筛选
            self.status_bar.showMessage("正在筛选数据...")
             
            # 获取当前表格数据
            data = []
            for row in range(self.table_widget.rowCount()):
                row_data = []
                for col in range(self.table_widget.columnCount()):
                    item = self.table_widget.item(row, col)
                    row_data.append(item.text() if item else "")
                data.append(row_data)
             
            # 转换为DataFrame以便筛选
            headers = [self.table_widget.horizontalHeaderItem(col).text() 
                      for col in range(self.table_widget.columnCount())]
            df = pd.DataFrame(data, columns=headers)
             
            # 获取筛选条件
            masks = []
            logic = logic_combo.currentText()
             
            for condition in condition_widgets:
                col_name = condition["col_combo"].currentText()
                operator = condition["operator_combo"].currentText()
                value = condition["value_edit"].text()
                 
                # 构建筛选条件
                if operator == "=":
                    mask = df[col_name] == value
                elif operator == ">":
                    mask = df[col_name] > value
                elif operator == "<":
                    mask = df[col_name] < value
                elif operator == "<=":
                    mask = df[col_name] <= value
                elif operator == ">=":
                    mask = df[col_name] >= value
                elif operator == "!=":
                    mask = df[col_name] != value
                elif operator == "包含":
                    mask = df[col_name].str.contains(value, na=False)
                elif operator == "不包含":
                    mask = ~df[col_name].str.contains(value, na=False)
                elif operator == "开头为":
                    mask = df[col_name].str.startswith(value, na=False)
                elif operator == "结尾为":
                    mask = df[col_name].str.endswith(value, na=False)
                elif operator == "为空":
                    mask = df[col_name].isna() | (df[col_name] == "")
                elif operator == "不为空":
                    mask = ~df[col_name].isna() & (df[col_name] != "")
                 
                masks.append(mask)
             
            # 组合筛选条件
            if masks:
                combined_mask = masks[0]
                for mask in masks[1:]:
                    if logic == "AND":
                        combined_mask &= mask
                    else:
                        combined_mask |= mask
                 
                filtered_df = df[combined_mask]
            else:
                filtered_df = df.copy()
             
            # 更新表格显示
            self.table_widget.setRowCount(len(filtered_df))
            for row in range(len(filtered_df)):
                for col in range(len(filtered_df.columns)):
                    self.table_widget.setItem(row, col, 
                        QTableWidgetItem(str(filtered_df.iloc[row, col])))
             
            self.status_bar.showMessage(
                f"已筛选出{len(filtered_df)}条记录 (共{len(df)}条)" +
                f" | 使用{len(condition_widgets)}个条件{logic}组合"
            )
        else:
            self.status_bar.showMessage("筛选已取消")
         
 
         
    def _data_cleaning(self):
        """
        数据清洗功能
         
        功能: 对表格数据进行清洗处理，包括空值处理和数据整理
        参数: 无
        返回值: 无
        """
        from PyQt6.QtWidgets import QInputDialog  # 输入对话框组件
         
        # 检查表格是否有数据
        if self.table_widget.rowCount() == 0 or self.table_widget.columnCount() == 0:
            self.status_bar.showMessage("表格中没有数据可清洗")
            return
             
        # 获取所有列名作为选项
        columns = []
        for col in range(self.table_widget.columnCount()):
            header = self.table_widget.horizontalHeaderItem(col)
            columns.append(header.text() if header else f"Column{col+1}")
             
        # 弹出对话框让用户选择清洗列
        column, ok = QInputDialog.getItem(
            self,
            "选择清洗列",  # 对话框标题
            "请选择要清洗的列:",  # 提示文本
            columns,  # 选项列表
            0,  # 默认选中第一项
            False  # 不允许编辑
        )
         
        # 如果用户取消了选择
        if not ok:
            return
             
        # 获取列索引
        col_index = columns.index(column)
         
        # 弹出对话框让用户选择清洗方式
        methods = ["删除空值行", "填充默认值", "删除重复行"]
        method, ok = QInputDialog.getItem(
            self,
            "选择清洗方式",
            "请选择清洗方式:",
            methods,
            0,
            False
        )
         
        # 如果用户取消了选择
        if not ok:
            return
             
        # 执行数据清洗
        try:
            if method == "删除空值行":
                # 删除空值行逻辑
                rows_to_keep = []
                for row in range(self.table_widget.rowCount()):
                    item = self.table_widget.item(row, col_index)
                    if item and item.text().strip():  # 检查单元格是否有值
                        rows_to_keep.append(row)
                 
                # 创建新表格数据
                new_data = []
                for row in rows_to_keep:
                    row_data = []
                    for col in range(self.table_widget.columnCount()):
                        item = self.table_widget.item(row, col)
                        row_data.append(item.text() if item else "")
                    new_data.append(row_data)
                 
                # 更新表格
                self._update_table_with_data(new_data)
                 
                self.status_bar.showMessage(f"已删除{self.table_widget.rowCount() - len(rows_to_keep)}条空值行")
                 
            elif method == "填充默认值":
                # 填充默认值逻辑
                default_value, ok = QInputDialog.getText(
                    self,
                    "输入默认值",
                    f"请输入{column}列的默认值:"
                )
                 
                if ok:
                    for row in range(self.table_widget.rowCount()):
                        item = self.table_widget.item(row, col_index)
                        if not item or not item.text().strip():
                            self.table_widget.setItem(row, col_index, QTableWidgetItem(default_value))
                     
                    self.status_bar.showMessage(f"已将{column}列的空值填充为: {default_value}")
                 
            elif method == "删除重复行":
                # 删除重复行逻辑
                unique_values = set()
                rows_to_keep = []
                 
                for row in range(self.table_widget.rowCount()):
                    item = self.table_widget.item(row, col_index)
                    value = item.text() if item else ""
                    if value not in unique_values:
                        unique_values.add(value)
                        rows_to_keep.append(row)
                 
                # 创建新表格数据
                new_data = []
                for row in rows_to_keep:
                    row_data = []
                    for col in range(self.table_widget.columnCount()):
                        item = self.table_widget.item(row, col)
                        row_data.append(item.text() if item else "")
                    new_data.append(row_data)
                 
                # 更新表格
                self._update_table_with_data(new_data)
                 
                self.status_bar.showMessage(f"已删除{self.table_widget.rowCount() - len(rows_to_keep)}条重复行")
                 
        except Exception as e:
            self.status_bar.showMessage(f"数据清洗失败: {str(e)}")
             
    def _update_table_with_data(self, data):
        """
        用新数据更新表格
         
        参数:
            data: list - 二维列表，包含表格数据
        返回值: 无
        """
        # 清空表格内容
        self.table_widget.clearContents()
         
        # 设置新行数
        self.table_widget.setRowCount(len(data))
         
        # 填充新数据
        for row in range(len(data)):
            for col in range(len(data[row])):
                item = QTableWidgetItem(data[row][col])
                self.table_widget.setItem(row, col, item)
                 
    def _visualize_data(self):
        """
        数据可视化功能
         
        功能: 对表格数据进行可视化展示，支持多种图表类型
        参数: 无
        返回值: 无
        """
        from PyQt6.QtWidgets import QInputDialog, QMessageBox  # 输入对话框和消息框组件
         
        # 检查表格是否有数据
        if self.table_widget.rowCount() == 0 or self.table_widget.columnCount() == 0:
            self.status_bar.showMessage("表格中没有数据可可视化")
            return
             
        # 获取所有列名作为选项
        columns = []
        for col in range(self.table_widget.columnCount()):
            header = self.table_widget.horizontalHeaderItem(col)
            columns.append(header.text() if header else f"Column{col+1}")
             
        # 弹出对话框让用户选择可视化列
        column, ok = QInputDialog.getItem(
            self,
            "选择可视化列",  # 对话框标题
            "请选择要可视化的列:",  # 提示文本
            columns,  # 选项列表
            0,  # 默认选中第一项
            False  # 不允许编辑
        )
         
        # 如果用户取消了选择
        if not ok:
            return
             
        # 获取列索引
        col_index = columns.index(column)
         
        # 弹出对话框让用户选择图表类型
        chart_types = ["柱状图", "折线图", "饼图", "箱线图", "散点图"]
        chart_type, ok = QInputDialog.getItem(
            self,
            "选择图表类型",
            "请选择图表类型:",
            chart_types,
            0,
            False
        )
         
        # 如果用户取消了选择
        if not ok:
            return
             
        # 收集列数据
        numeric_data = []
        labels = []
        for row in range(self.table_widget.rowCount()):
            item = self.table_widget.item(row, col_index)
            if item and item.text().strip():  # 只处理有值的单元格
                try:
                    # 尝试转换为数值
                    value = float(item.text())
                    numeric_data.append(value)
                    labels.append(str(row+1))  # 使用行号作为标签
                except ValueError:
                    # 非数值数据跳过
                    pass
         
        # 如果没有有效数据
        if not numeric_data:
            self.status_bar.showMessage(f"{column}列没有可可视化的数值数据")
            return
             
        # 执行可视化
        try:
            plt.figure(figsize=(8, 6))  # 设置图表大小
             
            if chart_type == "柱状图":
                # 创建柱状图
                plt.bar(labels, numeric_data)
                plt.title(f"{column}列柱状图")  # 设置标题
                plt.xlabel("行号")  # X轴标签
                plt.ylabel("数值")  # Y轴标签
                 
            elif chart_type == "折线图":
                # 创建折线图
                plt.plot(labels, numeric_data, marker='o')
                plt.title(f"{column}列折线图")
                plt.xlabel("行号")
                plt.ylabel("数值")
                 
            elif chart_type == "饼图":
                # 创建饼图
                plt.pie(numeric_data, labels=labels, autopct='%1.1f%%')
                plt.title(f"{column}列饼图")
                 
            elif chart_type == "箱线图":
                # 创建箱线图
                sns.boxplot(data=numeric_data)
                plt.title(f"{column}列箱线图")
                plt.ylabel("数值")
                 
            elif chart_type == "散点图":
                # 创建散点图
                plt.scatter(range(len(numeric_data)), numeric_data)
                plt.title(f"{column}列散点图")
                plt.xlabel("索引")
                plt.ylabel("数值")
                 
            plt.tight_layout()  # 自动调整子图参数
            plt.show()  # 显示图表
             
            self.status_bar.showMessage(f"已生成{column}列的{chart_type}")
             
        except Exception as e:
            self.status_bar.showMessage(f"数据可视化失败: {str(e)}")
             
    def _data_analysis(self):
        """
        数据分析功能
         
        功能: 对表格数据进行基础统计分析
        参数: 无
        返回值: 无
        """
        from PyQt6.QtWidgets import QMessageBox  # 消息框组件
        import numpy as np  # 数值计算库
         
        # 检查表格是否有数据
        if self.table_widget.rowCount() == 0 or self.table_widget.columnCount() == 0:
            self.status_bar.showMessage("表格中没有数据可分析")
            return
             
        # 基础统计分析
        try:
            stats = []
            for col in range(self.table_widget.columnCount()):
                data = []
                for row in range(self.table_widget.rowCount()):
                    item = self.table_widget.item(row, col)
                    if item and item.text().strip():  # 只处理有值的单元格
                        try:
                            value = float(item.text())
                            data.append(value)
                        except ValueError:
                            pass
                 
                if data:
                    header = self.table_widget.horizontalHeaderItem(col)
                    col_name = header.text() if header else f"Column{col+1}"
                     
                    # 计算统计量
                    stats.append(f"{col_name}列统计结果:")
                    stats.append(f"-----------------")
                    stats.append(f"数据个数: {len(data)}")
                    stats.append(f"平均值: {np.mean(data):.2f}")
                    stats.append(f"标准差: {np.std(data):.2f}")
                    stats.append(f"最小值: {min(data):.2f}")
                    stats.append(f"25%分位数: {np.percentile(data, 25):.2f}")
                    stats.append(f"中位数: {np.median(data):.2f}")
                    stats.append(f"75%分位数: {np.percentile(data, 75):.2f}")
                    stats.append(f"最大值: {max(data):.2f}")
                    stats.append("")
             
            # 显示统计结果
            if stats:
                QMessageBox.information(
                    self,
                    "基础统计结果",
                    "\n".join(stats)
                )
                self.status_bar.showMessage("已完成基础统计分析")
            else:
                self.status_bar.showMessage("没有找到可分析的数值数据")
                 
        except Exception as e:
            self.status_bar.showMessage(f"数据分析失败: {str(e)}")
         
    # except Exception as e:
    #     self.status_bar.showMessage(f"数据分析失败: {str(e)}")
     
    def _show_about(self):
        """显示关于信息"""
        self.status_bar.showMessage("关于功能待实现")
 
 
if __name__ == "__main__":
    """程序入口"""
    app = QApplication(sys.argv)
     
    # 创建主窗口
    window = DataAnalysisPlatform()
    window.show()
     
    # 运行应用
    sys.exit(app.exec())