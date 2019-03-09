import sys
import os
from PyQt5 import QtWidgets
import shop_data
import main_form
import dialog
import csv


class App(QtWidgets.QMainWindow, main_form.Ui_MainWindow):
    shop_data = shop_data.ShopData()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_enabled_data_fields(False)

        self.comboBox_shop.currentIndexChanged.connect(self.change_shop)
        self.pushbtn_add_shop.clicked.connect(self.add_shop_click)
        self.pushbtn_del_shop.clicked.connect(self.del_shop_click)
        self.pushbtn_confirm_data.clicked.connect(self.update_data_click)
        self.pushbtn_open_total.clicked.connect(self.open_total_click)
        self.action_load_file.triggered.connect(self.load_file_click)
        self.action_save_file.triggered.connect(self.save_file_click)

    def change_shop(self):
        index = self.comboBox_shop.currentIndex()
        if index != -1:
            self.set_enabled_data_fields(True)
            self.refresh_shops(index)
            if not (self.pushbtn_confirm_data.isEnabled()):
                self.pushbtn_confirm_data.setEnabled(True)
        else:
            self.clear_app()
            self.set_enabled_data_fields(False)
            if self.pushbtn_confirm_data.isEnabled():
                self.pushbtn_confirm_data.setEnabled(False)

    def set_enabled_data_fields(self, status):
        # статус элементов, содержащих данные о цехе
        self.set_enabled_fields_by_grid(self.grid_value, status)
        for grid in self.grid_months.children():
            self.set_enabled_fields_by_grid(grid, status)
        # статус кнопок, управляющих данными
        self.set_enabled_fields_by_grid(self.vlayout_data_buttons, status)

    @staticmethod
    def set_enabled_fields_by_grid(grid, status):
        for item in range(len(grid)):
            if type(grid.itemAt(item).widget()) in (QtWidgets.QLabel, QtWidgets.QDoubleSpinBox, QtWidgets.QPushButton):
                grid.itemAt(item).widget().setEnabled(status)

    def refresh_shops(self, shop_id):
        self.dblSpinBox_january.setValue(self.shop_data.get_value_for_month(shop_id, 1))
        self.dblSpinBox_february.setValue(self.shop_data.get_value_for_month(shop_id, 2))
        self.dblSpinBox_march.setValue(self.shop_data.get_value_for_month(shop_id, 3))
        self.dblSpinBox_april.setValue(self.shop_data.get_value_for_month(shop_id, 4))
        self.dblSpinBox_may.setValue(self.shop_data.get_value_for_month(shop_id, 5))
        self.dblSpinBox_june.setValue(self.shop_data.get_value_for_month(shop_id, 6))
        self.dblSpinBox_july.setValue(self.shop_data.get_value_for_month(shop_id, 7))
        self.dblSpinBox_august.setValue(self.shop_data.get_value_for_month(shop_id, 8))
        self.dblSpinBox_september.setValue(self.shop_data.get_value_for_month(shop_id, 9))
        self.dblSpinBox_october.setValue(self.shop_data.get_value_for_month(shop_id, 10))
        self.dblSpinBox_november.setValue(self.shop_data.get_value_for_month(shop_id, 11))
        self.dblSpinBox_december.setValue(self.shop_data.get_value_for_month(shop_id, 12))
        self.refresh_shop_values(self.shop_data.get_shop_list()[shop_id])

    def refresh_shop_values(self, shop):
        if shop[13] != '':
            self.lbl_total_value.setText(shop[13])
        else:
            self.lbl_total_value.setText('0')
        if shop[14] != '':
            self.lbl_max_power_usage_value.setText(shop[14])
        else:
            self.lbl_max_power_usage_value.setText('Не найдено')

    def add_shop_click(self):
        name_shop, ok = QtWidgets.QInputDialog.getText(self, 'Название цеха', 'Введите название нового цеха')
        if ok and name_shop != '':
            self.shop_data.add_shop(name_shop)
            self.comboBox_shop.addItem(name_shop)

    def del_shop_click(self):
        index = self.comboBox_shop.currentIndex()
        if index != -1:
            self.shop_data.del_shop(index)
            self.comboBox_shop.removeItem(index)

    def open_total_click(self):
        dialog_total = dialog.DialogTotal(self.shop_data.get_total_line())
        dialog_total.exec_()

    def update_data_click(self):
        shop_list = self.shop_data.get_shop_list()
        index = self.comboBox_shop.currentIndex()
        sum_months = [0.0]
        max_usage_month = ['Не найдено']
        self.set_data_months(self.grid_months, sum_months, max_usage_month)
        sum_months[0] = format(sum_months[0], '.2f')  # во избежание перегрузок
        shop_list[index] = [self.shop_data.get_shop_name(index), str(self.dblSpinBox_january.value()).replace('.', ','),
                            str(self.dblSpinBox_february.value()).replace('.', ','),
                            str(self.dblSpinBox_march.value()).replace('.', ','),
                            str(self.dblSpinBox_april.value()).replace('.', ','),
                            str(self.dblSpinBox_may.value()).replace('.', ','),
                            str(self.dblSpinBox_june.value()).replace('.', ','),
                            str(self.dblSpinBox_july.value()).replace('.', ','),
                            str(self.dblSpinBox_august.value()).replace('.', ','),
                            str(self.dblSpinBox_september.value()).replace('.', ','),
                            str(self.dblSpinBox_october.value()).replace('.', ','),
                            str(self.dblSpinBox_november.value()).replace('.', ','),
                            str(self.dblSpinBox_december.value()).replace('.', ','),
                            str(sum_months[0]).replace('.', ','), max_usage_month[0]]
        self.refresh_shops(index)

    # изменяет значения принимаемых годовой суммы и месяца с максимальным потреблением,
    # которые передаются как нулевой элемент списков
    @staticmethod
    def set_data_months(grid_months, sum_months, max_usage_month):
        max_usage = 0.0
        for grid in grid_months.children():
            for i in range(len(grid)):
                if type(grid.itemAt(i).widget()) is QtWidgets.QDoubleSpinBox:
                    sum_months[0] += grid.itemAt(i).widget().value()
                    if grid.itemAt(i).widget().value() > max_usage:
                        max_usage = grid.itemAt(i).widget().value()
                        max_usage_month[0] = grid.itemAt(i).widget().statusTip()

    def load_file_click(self):
        csv_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл', os.getenv('Home'), 'CSV (*.csv)')
        if csv_path[0] != '':
            with open(csv_path[0], 'r') as file:
                csv_reader = csv.reader(file, delimiter=';')
                self.clear_app()
                try:
                    self.shop_data.load_shop_list(csv_reader)
                    shop_list = self.shop_data.get_shop_list()
                    for row in shop_list:
                        self.comboBox_shop.addItem(row[0])
                except:
                    QtWidgets.QMessageBox.about(self, 'Ошибка', 'Файл не может быть проанализирован')

    def clear_app(self):
        self.comboBox_shop.clear()
        self.shop_data.clear_shops()
        self.lbl_max_power_usage_value.setText('Не найдено')
        self.lbl_total_value.setText('0,00')
        for grid in self.grid_months.children():
            for i in range(len(grid)):
                if type(grid.itemAt(i).widget()) is QtWidgets.QDoubleSpinBox:
                    grid.itemAt(i).widget().setValue(0)

    def save_file_click(self):
        shop_list = [self.shop_data.get_first_line()]
        shop_list.extend(self.shop_data.get_shop_list())
        shop_list.append(self.shop_data.get_total_line())
        if len(shop_list) > 2:
            csv_path = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохраните файл', '', 'CSV (*.csv);;Excel (*.xlsx)')
            if csv_path[0] != '':
                try:
                    if '.csv' in csv_path[0]:
                        with open(csv_path[0], 'w') as file:
                            csv_writer = csv.writer(file, delimiter=';', lineterminator='\n')
                            for line in shop_list:
                                csv_writer.writerow(line)
                    elif '.xlsx' in csv_path[0]:
                        self.shop_data.save_data_as_xlsx(shop_list, csv_path[0])
                except:
                    QtWidgets.QMessageBox.about(self, 'Ошибка', 'Невозможно записать файл')
        else:
            QtWidgets.QMessageBox.about(self, 'Ошибка', 'Записи о цехах не найдены')


def main():
    app_main = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app_main.exec_())


if __name__ == '__main__':  # Если запускаем этот файл,
    main()  # то активируем функцию main()
