from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(300, 420)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 420))
        MainWindow.setMaximumSize(QtCore.QSize(300, 420))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 5, 10, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.grid_shops = QtWidgets.QGridLayout()
        self.grid_shops.setContentsMargins(-1, 5, -1, 5)
        self.grid_shops.setSpacing(5)
        self.grid_shops.setObjectName("grid_shops")
        self.pushbtn_add_shop = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushbtn_add_shop.sizePolicy().hasHeightForWidth())
        self.pushbtn_add_shop.setSizePolicy(sizePolicy)
        self.pushbtn_add_shop.setMinimumSize(QtCore.QSize(20, 22))
        self.pushbtn_add_shop.setMaximumSize(QtCore.QSize(30, 25))
        self.pushbtn_add_shop.setObjectName("pushbtn_add_shop")
        self.grid_shops.addWidget(self.pushbtn_add_shop, 0, 1, 1, 1)
        self.pushbtn_del_shop = QtWidgets.QPushButton(self.centralwidget)
        self.pushbtn_del_shop.setMaximumSize(QtCore.QSize(30, 25))
        self.pushbtn_del_shop.setObjectName("pushbtn_del_shop")
        self.grid_shops.addWidget(self.pushbtn_del_shop, 0, 2, 1, 1)
        self.comboBox_shop = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_shop.setMinimumSize(QtCore.QSize(120, 22))
        self.comboBox_shop.setMaximumSize(QtCore.QSize(16777215, 23))
        self.comboBox_shop.setEditable(False)
        self.comboBox_shop.setCurrentText("")
        self.comboBox_shop.setObjectName("comboBox_shop")
        self.grid_shops.addWidget(self.comboBox_shop, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.grid_shops)
        self.grid_value = QtWidgets.QGridLayout()
        self.grid_value.setContentsMargins(-1, 5, -1, 5)
        self.grid_value.setSpacing(5)
        self.grid_value.setObjectName("grid_value")
        self.lbl_total = QtWidgets.QLabel(self.centralwidget)
        self.lbl_total.setMinimumSize(QtCore.QSize(200, 20))
        self.lbl_total.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lbl_total.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_total.setObjectName("lbl_total")
        self.grid_value.addWidget(self.lbl_total, 1, 0, 1, 1)
        self.lbl_max_power_usage_value = QtWidgets.QLabel(self.centralwidget)
        self.lbl_max_power_usage_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_max_power_usage_value.setObjectName("lbl_max_power_usage_value")
        self.grid_value.addWidget(self.lbl_max_power_usage_value, 0, 1, 1, 1)
        self.lbl_total_value = QtWidgets.QLabel(self.centralwidget)
        self.lbl_total_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_total_value.setObjectName("lbl_total_value")
        self.grid_value.addWidget(self.lbl_total_value, 1, 1, 1, 1)
        self.lbl_max_power_usage = QtWidgets.QLabel(self.centralwidget)
        self.lbl_max_power_usage.setMinimumSize(QtCore.QSize(200, 20))
        self.lbl_max_power_usage.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lbl_max_power_usage.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_max_power_usage.setObjectName("lbl_max_power_usage")
        self.grid_value.addWidget(self.lbl_max_power_usage, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.grid_value)
        self.grid_months = QtWidgets.QGridLayout()
        self.grid_months.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.grid_months.setHorizontalSpacing(5)
        self.grid_months.setVerticalSpacing(0)
        self.grid_months.setObjectName("grid_months")
        self.grid_first_6 = QtWidgets.QGridLayout()
        self.grid_first_6.setContentsMargins(-1, 5, -1, 5)
        self.grid_first_6.setHorizontalSpacing(5)
        self.grid_first_6.setVerticalSpacing(10)
        self.grid_first_6.setObjectName("grid_first_6")
        self.lbl_january = QtWidgets.QLabel(self.centralwidget)
        self.lbl_january.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_january.setObjectName("lbl_january")
        self.grid_first_6.addWidget(self.lbl_january, 0, 0, 1, 1)
        self.lbl_april = QtWidgets.QLabel(self.centralwidget)
        self.lbl_april.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_april.setObjectName("lbl_april")
        self.grid_first_6.addWidget(self.lbl_april, 3, 0, 1, 1)
        self.lbl_february = QtWidgets.QLabel(self.centralwidget)
        self.lbl_february.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_february.setObjectName("lbl_february")
        self.grid_first_6.addWidget(self.lbl_february, 1, 0, 1, 1)
        self.lbl_march = QtWidgets.QLabel(self.centralwidget)
        self.lbl_march.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_march.setObjectName("lbl_march")
        self.grid_first_6.addWidget(self.lbl_march, 2, 0, 1, 1)
        self.lbl_may = QtWidgets.QLabel(self.centralwidget)
        self.lbl_may.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_may.setObjectName("lbl_may")
        self.grid_first_6.addWidget(self.lbl_may, 4, 0, 1, 1)
        self.lbl_june = QtWidgets.QLabel(self.centralwidget)
        self.lbl_june.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_june.setObjectName("lbl_june")
        self.grid_first_6.addWidget(self.lbl_june, 5, 0, 1, 1)
        self.dblSpinBox_january = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dblSpinBox_january.setMinimumSize(QtCore.QSize(0, 20))
        self.dblSpinBox_january.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dblSpinBox_january.setMaximum(9999999999.0)
        self.dblSpinBox_january.setObjectName("dblSpinBox_january")
        self.grid_first_6.addWidget(self.dblSpinBox_january, 0, 1, 1, 1)
        self.dblSpinBox_february = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dblSpinBox_february.setMinimumSize(QtCore.QSize(0, 20))
        self.dblSpinBox_february.setMaximum(9999999999.0)
        self.dblSpinBox_february.setObjectName("dblSpinBox_february")
        self.grid_first_6.addWidget(self.dblSpinBox_february, 1, 1, 1, 1)
        self.dblSpinBox_june = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dblSpinBox_june.setMinimumSize(QtCore.QSize(0, 20))
        self.dblSpinBox_june.setMaximum(9999999999.0)
        self.dblSpinBox_june.setObjectName("dblSpinBox_june")
        self.grid_first_6.addWidget(self.dblSpinBox_june, 5, 1, 1, 1)
        self.dblSpinBox_may = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dblSpinBox_may.setMinimumSize(QtCore.QSize(0, 20))
        self.dblSpinBox_may.setMaximum(9999999999.0)
        self.dblSpinBox_may.setObjectName("dblSpinBox_may")
        self.grid_first_6.addWidget(self.dblSpinBox_may, 4, 1, 1, 1)
        self.dblSpinBox_april = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dblSpinBox_april.setMinimumSize(QtCore.QSize(0, 20))
        self.dblSpinBox_april.setMaximum(9999999999.0)
        self.dblSpinBox_april.setObjectName("dblSpinBox_april")
        self.grid_first_6.addWidget(self.dblSpinBox_april, 3, 1, 1, 1)
        self.dblSpinBox_march = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dblSpinBox_march.setMinimumSize(QtCore.QSize(0, 20))
        self.dblSpinBox_march.setMaximum(9999999999.0)
        self.dblSpinBox_march.setObjectName("dblSpinBox_march")
        self.grid_first_6.addWidget(self.dblSpinBox_march, 2, 1, 1, 1)
        self.grid_months.addLayout(self.grid_first_6, 0, 0, 1, 1)
        self.grid_last_6 = QtWidgets.QGridLayout()
        self.grid_last_6.setContentsMargins(-1, 5, -1, 5)
        self.grid_last_6.setHorizontalSpacing(5)
        self.grid_last_6.setVerticalSpacing(10)
        self.grid_last_6.setObjectName("grid_last_6")
        self.lbl_november = QtWidgets.QLabel(self.centralwidget)
        self.lbl_november.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_november.setObjectName("lbl_november")
        self.grid_last_6.addWidget(self.lbl_november, 4, 0, 1, 1)
        self.lbl_october = QtWidgets.QLabel(self.centralwidget)
        self.lbl_october.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_october.setObjectName("lbl_october")
        self.grid_last_6.addWidget(self.lbl_october, 3, 0, 1, 1)
        self.lbl_august = QtWidgets.QLabel(self.centralwidget)
        self.lbl_august.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_august.setObjectName("lbl_august")
        self.grid_last_6.addWidget(self.lbl_august, 1, 0, 1, 1)
        self.lbl_september = QtWidgets.QLabel(self.centralwidget)
        self.lbl_september.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_september.setObjectName("lbl_september")
        self.grid_last_6.addWidget(self.lbl_september, 2, 0, 1, 1)
        self.lbl_july = QtWidgets.QLabel(self.centralwidget)
        self.lbl_july.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_july.setObjectName("lbl_july")
        self.grid_last_6.addWidget(self.lbl_july, 0, 0, 1, 1)
        self.lbl_december = QtWidgets.QLabel(self.centralwidget)
        self.lbl_december.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_december.setObjectName("lbl_december")
        self.grid_last_6.addWidget(self.lbl_december, 5, 0, 1, 1)
        self.dblSpinBox_july = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dblSpinBox_july.setMinimumSize(QtCore.QSize(0, 20))
        self.dblSpinBox_july.setMaximum(9999999999.0)
        self.dblSpinBox_july.setObjectName("dblSpinBox_july")
        self.grid_last_6.addWidget(self.dblSpinBox_july, 0, 1, 1, 1)
        self.dblSpinBox_august = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dblSpinBox_august.setMinimumSize(QtCore.QSize(0, 20))
        self.dblSpinBox_august.setMaximum(9999999999.0)
        self.dblSpinBox_august.setObjectName("dblSpinBox_august")
        self.grid_last_6.addWidget(self.dblSpinBox_august, 1, 1, 1, 1)
        self.dblSpinBox_september = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dblSpinBox_september.setMinimumSize(QtCore.QSize(0, 20))
        self.dblSpinBox_september.setMaximum(9999999999.0)
        self.dblSpinBox_september.setObjectName("dblSpinBox_september")
        self.grid_last_6.addWidget(self.dblSpinBox_september, 2, 1, 1, 1)
        self.dblSpinBox_november = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dblSpinBox_november.setMinimumSize(QtCore.QSize(0, 20))
        self.dblSpinBox_november.setMaximum(9999999999.0)
        self.dblSpinBox_november.setObjectName("dblSpinBox_november")
        self.grid_last_6.addWidget(self.dblSpinBox_november, 4, 1, 1, 1)
        self.dblSpinBox_december = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dblSpinBox_december.setMinimumSize(QtCore.QSize(0, 20))
        self.dblSpinBox_december.setMaximum(9999999999.0)
        self.dblSpinBox_december.setObjectName("dblSpinBox_december")
        self.grid_last_6.addWidget(self.dblSpinBox_december, 5, 1, 1, 1)
        self.dblSpinBox_october = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dblSpinBox_october.setMinimumSize(QtCore.QSize(0, 20))
        self.dblSpinBox_october.setMaximum(9999999999.0)
        self.dblSpinBox_october.setObjectName("dblSpinBox_october")
        self.grid_last_6.addWidget(self.dblSpinBox_october, 3, 1, 1, 1)
        self.grid_months.addLayout(self.grid_last_6, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.grid_months)
        self.vlayout_data_buttons = QtWidgets.QVBoxLayout()
        self.vlayout_data_buttons.setObjectName("vlayout_data_buttons")
        self.pushbtn_confirm_data = QtWidgets.QPushButton(self.centralwidget)
        self.pushbtn_confirm_data.setMinimumSize(QtCore.QSize(200, 26))
        self.pushbtn_confirm_data.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushbtn_confirm_data.setObjectName("pushbtn_confirm_data")
        self.vlayout_data_buttons.addWidget(self.pushbtn_confirm_data, 0, QtCore.Qt.AlignHCenter)
        self.pushbtn_open_total = QtWidgets.QPushButton(self.centralwidget)
        self.pushbtn_open_total.setMinimumSize(QtCore.QSize(200, 26))
        self.pushbtn_open_total.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushbtn_open_total.setObjectName("pushbtn_open_total")
        self.vlayout_data_buttons.addWidget(self.pushbtn_open_total, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.vlayout_data_buttons)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.action_load_file = QtWidgets.QAction(MainWindow)
        self.action_load_file.setObjectName("action_load_file")
        self.action_save_file = QtWidgets.QAction(MainWindow)
        self.action_save_file.setObjectName("action_save_file")
        self.menu.addAction(self.action_load_file)
        self.menu.addAction(self.action_save_file)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Расход электроэнергии"))
        self.pushbtn_add_shop.setText(_translate("MainWindow", "+"))
        self.pushbtn_del_shop.setText(_translate("MainWindow", "-"))
        self.lbl_total.setText(_translate("MainWindow", "Итог за год:"))
        self.lbl_max_power_usage_value.setText(_translate("MainWindow", "Не найдено"))
        self.lbl_total_value.setText(_translate("MainWindow", "0,00"))
        self.lbl_max_power_usage.setText(_translate("MainWindow", "Максимальное потребление:"))
        self.lbl_january.setText(_translate("MainWindow", "Январь:"))
        self.lbl_april.setText(_translate("MainWindow", "Апрель:"))
        self.lbl_february.setText(_translate("MainWindow", "Февраль:"))
        self.lbl_march.setText(_translate("MainWindow", "Март:"))
        self.lbl_may.setText(_translate("MainWindow", "Май:"))
        self.lbl_june.setText(_translate("MainWindow", "Июнь:"))
        self.dblSpinBox_january.setStatusTip(_translate("MainWindow", "Январь"))
        self.dblSpinBox_february.setStatusTip(_translate("MainWindow", "Февраль"))
        self.dblSpinBox_june.setStatusTip(_translate("MainWindow", "Июнь"))
        self.dblSpinBox_may.setStatusTip(_translate("MainWindow", "Май"))
        self.dblSpinBox_april.setStatusTip(_translate("MainWindow", "Апрель"))
        self.dblSpinBox_march.setStatusTip(_translate("MainWindow", "Март"))
        self.lbl_november.setText(_translate("MainWindow", "Ноябрь:"))
        self.lbl_october.setText(_translate("MainWindow", "Октябрь:"))
        self.lbl_august.setText(_translate("MainWindow", "Август:"))
        self.lbl_september.setText(_translate("MainWindow", "Сентябрь:"))
        self.lbl_july.setText(_translate("MainWindow", "Июль:"))
        self.lbl_december.setText(_translate("MainWindow", "Декабрь:"))
        self.dblSpinBox_july.setStatusTip(_translate("MainWindow", "Июль"))
        self.dblSpinBox_august.setStatusTip(_translate("MainWindow", "Август"))
        self.dblSpinBox_september.setStatusTip(_translate("MainWindow", "Сентябрь"))
        self.dblSpinBox_november.setStatusTip(_translate("MainWindow", "Ноябрь"))
        self.dblSpinBox_december.setStatusTip(_translate("MainWindow", "Декабрь"))
        self.dblSpinBox_october.setStatusTip(_translate("MainWindow", "Октябрь"))
        self.pushbtn_confirm_data.setText(_translate("MainWindow", "Применить изменения"))
        self.pushbtn_open_total.setText(_translate("MainWindow", "Просмотреть итоговые суммы"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.action_load_file.setText(_translate("MainWindow", "Загрузить..."))
        self.action_save_file.setText(_translate("MainWindow", "Выгрузить..."))

