# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BukuTelefon.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 230, 55, 16))
        self.label_6.setObjectName("label_6")
        self.lineEditID = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditID.setGeometry(QtCore.QRect(110, 30, 361, 22))
        self.lineEditID.setObjectName("lineEditID")
        self.lineEditNAMA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNAMA.setGeometry(QtCore.QRect(110, 70, 361, 22))
        self.lineEditNAMA.setObjectName("lineEditNAMA")
        self.lineEditKELAS = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditKELAS.setGeometry(QtCore.QRect(110, 110, 361, 22))
        self.lineEditKELAS.setObjectName("lineEditKELAS")
        self.lineEditKOTA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditKOTA.setGeometry(QtCore.QRect(110, 150, 361, 22))
        self.lineEditKOTA.setObjectName("lineEditKOTA")
        self.lineEditTELEFON = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTELEFON.setGeometry(QtCore.QRect(110, 190, 361, 22))
        self.lineEditTELEFON.setObjectName("lineEditTELEFON")
        self.lineEditEMAIL = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEMAIL.setGeometry(QtCore.QRect(110, 230, 361, 22))
        self.lineEditEMAIL.setObjectName("lineEditEMAIL")
        self.pushButtonSIMPAN = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSIMPAN.setGeometry(QtCore.QRect(530, 40, 181, 28))
        self.pushButtonSIMPAN.setObjectName("pushButtonSIMPAN")
        self.pushButtonHAPUS = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHAPUS.setGeometry(QtCore.QRect(530, 90, 181, 28))
        self.pushButtonHAPUS.setObjectName("pushButtonHAPUS")
        self.pushButtonPERBARUI = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPERBARUI.setGeometry(QtCore.QRect(530, 140, 181, 28))
        self.pushButtonPERBARUI.setObjectName("pushButtonPERBARUI")
        self.pushButtonDAFTAR = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDAFTAR.setGeometry(QtCore.QRect(530, 190, 181, 28))
        self.pushButtonDAFTAR.setObjectName("pushButtonDAFTAR")
        self.tableWidgetDaftar = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetDaftar.setGeometry(QtCore.QRect(10, 280, 781, 271))
        self.tableWidgetDaftar.setRowCount(0)
        self.tableWidgetDaftar.setColumnCount(0)
        self.tableWidgetDaftar.setObjectName("tableWidgetDaftar")
        self.tableWidgetDaftar.horizontalHeader().setHighlightSections(False)
        self.tableWidgetDaftar.verticalHeader().setHighlightSections(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "NAMA"))
        self.label_3.setText(_translate("MainWindow", "KELAS"))
        self.label_4.setText(_translate("MainWindow", "KOTA"))
        self.label_5.setText(_translate("MainWindow", "TELEFON"))
        self.label_6.setText(_translate("MainWindow", "EMAIL"))
        self.pushButtonSIMPAN.setText(_translate("MainWindow", "SIMPAN"))
        self.pushButtonHAPUS.setText(_translate("MainWindow", "HAPUS"))
        self.pushButtonPERBARUI.setText(_translate("MainWindow", "PERBARUI"))
        self.pushButtonDAFTAR.setText(_translate("MainWindow", "DAFTAR"))
