# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sum_month.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(325, 300)
        Dialog.setMinimumSize(QtCore.QSize(325, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 350))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(15)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)
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
        self.lbl_january = QtWidgets.QLabel(Dialog)
        self.lbl_january.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_january.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_january.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_january.setObjectName("lbl_january")
        self.grid_first_6.addWidget(self.lbl_january, 0, 0, 1, 1)
        self.lbl_february = QtWidgets.QLabel(Dialog)
        self.lbl_february.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_february.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_february.setObjectName("lbl_february")
        self.grid_first_6.addWidget(self.lbl_february, 1, 0, 1, 1)
        self.lbl_march = QtWidgets.QLabel(Dialog)
        self.lbl_march.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_march.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_march.setObjectName("lbl_march")
        self.grid_first_6.addWidget(self.lbl_march, 2, 0, 1, 1)
        self.lbl_may = QtWidgets.QLabel(Dialog)
        self.lbl_may.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_may.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_may.setObjectName("lbl_may")
        self.grid_first_6.addWidget(self.lbl_may, 4, 0, 1, 1)
        self.lbl_april = QtWidgets.QLabel(Dialog)
        self.lbl_april.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_april.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_april.setObjectName("lbl_april")
        self.grid_first_6.addWidget(self.lbl_april, 3, 0, 1, 1)
        self.lbl_june = QtWidgets.QLabel(Dialog)
        self.lbl_june.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_june.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_june.setObjectName("lbl_june")
        self.grid_first_6.addWidget(self.lbl_june, 5, 0, 1, 1)
        self.lbl_data_april = QtWidgets.QLabel(Dialog)
        self.lbl_data_april.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_data_april.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_data_april.setObjectName("lbl_data_april")
        self.grid_first_6.addWidget(self.lbl_data_april, 3, 1, 1, 1)
        self.lbl_data_january = QtWidgets.QLabel(Dialog)
        self.lbl_data_january.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_data_january.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_data_january.setObjectName("lbl_data_january")
        self.grid_first_6.addWidget(self.lbl_data_january, 0, 1, 1, 1)
        self.lbl_data_february = QtWidgets.QLabel(Dialog)
        self.lbl_data_february.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_data_february.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_data_february.setObjectName("lbl_data_february")
        self.grid_first_6.addWidget(self.lbl_data_february, 1, 1, 1, 1)
        self.lbl_data_march = QtWidgets.QLabel(Dialog)
        self.lbl_data_march.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_data_march.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_data_march.setObjectName("lbl_data_march")
        self.grid_first_6.addWidget(self.lbl_data_march, 2, 1, 1, 1)
        self.lbl_data_may = QtWidgets.QLabel(Dialog)
        self.lbl_data_may.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_data_may.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_data_may.setObjectName("lbl_data_may")
        self.grid_first_6.addWidget(self.lbl_data_may, 4, 1, 1, 1)
        self.lbl_data_june = QtWidgets.QLabel(Dialog)
        self.lbl_data_june.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_data_june.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_data_june.setObjectName("lbl_data_june")
        self.grid_first_6.addWidget(self.lbl_data_june, 5, 1, 1, 1)
        self.grid_months.addLayout(self.grid_first_6, 0, 0, 1, 1)
        self.grid_last_6 = QtWidgets.QGridLayout()
        self.grid_last_6.setContentsMargins(-1, 5, -1, 5)
        self.grid_last_6.setHorizontalSpacing(5)
        self.grid_last_6.setVerticalSpacing(10)
        self.grid_last_6.setObjectName("grid_last_6")
        self.lbl_november = QtWidgets.QLabel(Dialog)
        self.lbl_november.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_november.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_november.setObjectName("lbl_november")
        self.grid_last_6.addWidget(self.lbl_november, 4, 0, 1, 1)
        self.lbl_october = QtWidgets.QLabel(Dialog)
        self.lbl_october.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_october.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_october.setObjectName("lbl_october")
        self.grid_last_6.addWidget(self.lbl_october, 3, 0, 1, 1)
        self.lbl_august = QtWidgets.QLabel(Dialog)
        self.lbl_august.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_august.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_august.setObjectName("lbl_august")
        self.grid_last_6.addWidget(self.lbl_august, 1, 0, 1, 1)
        self.lbl_september = QtWidgets.QLabel(Dialog)
        self.lbl_september.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_september.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_september.setObjectName("lbl_september")
        self.grid_last_6.addWidget(self.lbl_september, 2, 0, 1, 1)
        self.lbl_july = QtWidgets.QLabel(Dialog)
        self.lbl_july.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_july.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_july.setObjectName("lbl_july")
        self.grid_last_6.addWidget(self.lbl_july, 0, 0, 1, 1)
        self.lbl_december = QtWidgets.QLabel(Dialog)
        self.lbl_december.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_december.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_december.setObjectName("lbl_december")
        self.grid_last_6.addWidget(self.lbl_december, 5, 0, 1, 1)
        self.lbl_data_july = QtWidgets.QLabel(Dialog)
        self.lbl_data_july.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_data_july.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_data_july.setObjectName("lbl_data_july")
        self.grid_last_6.addWidget(self.lbl_data_july, 0, 1, 1, 1)
        self.lbl_data_august = QtWidgets.QLabel(Dialog)
        self.lbl_data_august.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_data_august.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_data_august.setObjectName("lbl_data_august")
        self.grid_last_6.addWidget(self.lbl_data_august, 1, 1, 1, 1)
        self.lbl_data_september = QtWidgets.QLabel(Dialog)
        self.lbl_data_september.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_data_september.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_data_september.setObjectName("lbl_data_september")
        self.grid_last_6.addWidget(self.lbl_data_september, 2, 1, 1, 1)
        self.lbl_data_october = QtWidgets.QLabel(Dialog)
        self.lbl_data_october.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_data_october.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_data_october.setObjectName("lbl_data_october")
        self.grid_last_6.addWidget(self.lbl_data_october, 3, 1, 1, 1)
        self.lbl_data_november = QtWidgets.QLabel(Dialog)
        self.lbl_data_november.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_data_november.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_data_november.setObjectName("lbl_data_november")
        self.grid_last_6.addWidget(self.lbl_data_november, 4, 1, 1, 1)
        self.lbl_data_december = QtWidgets.QLabel(Dialog)
        self.lbl_data_december.setMinimumSize(QtCore.QSize(70, 20))
        self.lbl_data_december.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_data_december.setObjectName("lbl_data_december")
        self.grid_last_6.addWidget(self.lbl_data_december, 5, 1, 1, 1)
        self.grid_months.addLayout(self.grid_last_6, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.grid_months)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Сумма по месяцам"))
        self.lbl_january.setText(_translate("Dialog", "Январь:"))
        self.lbl_february.setText(_translate("Dialog", "Февраль:"))
        self.lbl_march.setText(_translate("Dialog", "Март:"))
        self.lbl_may.setText(_translate("Dialog", "Май:"))
        self.lbl_april.setText(_translate("Dialog", "Апрель:"))
        self.lbl_june.setText(_translate("Dialog", "Июнь:"))
        self.lbl_data_april.setText(_translate("Dialog", "0,00"))
        self.lbl_data_january.setText(_translate("Dialog", "0,00"))
        self.lbl_data_february.setText(_translate("Dialog", "0,00"))
        self.lbl_data_march.setText(_translate("Dialog", "0,00"))
        self.lbl_data_may.setText(_translate("Dialog", "0,00"))
        self.lbl_data_june.setText(_translate("Dialog", "0,00"))
        self.lbl_november.setText(_translate("Dialog", "Ноябрь:"))
        self.lbl_october.setText(_translate("Dialog", "Октябрь:"))
        self.lbl_august.setText(_translate("Dialog", "Август:"))
        self.lbl_september.setText(_translate("Dialog", "Сентябрь:"))
        self.lbl_july.setText(_translate("Dialog", "Июль:"))
        self.lbl_december.setText(_translate("Dialog", "Декабрь:"))
        self.lbl_data_july.setText(_translate("Dialog", "0,00"))
        self.lbl_data_august.setText(_translate("Dialog", "0,00"))
        self.lbl_data_september.setText(_translate("Dialog", "0,00"))
        self.lbl_data_october.setText(_translate("Dialog", "0,00"))
        self.lbl_data_november.setText(_translate("Dialog", "0,00"))
        self.lbl_data_december.setText(_translate("Dialog", "0,00"))

