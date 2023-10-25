# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ecg_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(778, 605)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        MainWindow.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(124, 27, 214, 255), stop:0.505682 rgba(5, 113, 244, 255), stop:0.926136 rgba(55, 185, 239, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, -10, 691, 131))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setStyleSheet("font: 12pt \"Montserrat\";\n"
                                 "background: transparent;")
        self.label.setObjectName("label")
        self.btn_calc_pulse = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.btn_calc_pulse.setGeometry(QtCore.QRect(510, 490, 231, 51))
        self.btn_calc_pulse.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_calc_pulse.setFont(font)
        self.btn_calc_pulse.setTabletTracking(False)
        self.btn_calc_pulse.setStatusTip("")
        self.btn_calc_pulse.setWhatsThis("")
        self.btn_calc_pulse.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../PycharmProjects/desktop_app/static/icon_pulse.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btn_calc_pulse.setIcon(icon)
        self.btn_calc_pulse.setIconSize(QtCore.QSize(30, 30))
        self.btn_calc_pulse.setShortcut("")
        self.btn_calc_pulse.setObjectName("btn_calc_pulse")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 310, 721, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("background: transparent;\n"
                                   "")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.pulse = QtWidgets.QLineEdit(self.layoutWidget)
        self.pulse.setStyleSheet("background: transparent;\n"
                                 "border: 2px solid \'black\';\n"
                                 "border-radius: 10;\n"
                                 "color:black;\n"
                                 "font: 16pt \"Montserrat\";")
        self.pulse.setObjectName("pulse")
        self.gridLayout.addWidget(self.pulse, 2, 1, 1, 1)
        self.dist_between_teeth = QtWidgets.QLineEdit(self.layoutWidget)
        self.dist_between_teeth.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dist_between_teeth.setStyleSheet("background: transparent;\n"
                                              "border: 2px solid \'black\';\n"
                                              "border-radius: 10;\n"
                                              "color: black;\n"
                                              "font: 16pt \"Montserrat\";")
        self.dist_between_teeth.setText("")
        self.dist_between_teeth.setObjectName("dist_between_teeth")
        self.gridLayout.addWidget(self.dist_between_teeth, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("background: transparent;\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.ecg_removal_rate = QtWidgets.QLineEdit(self.layoutWidget)
        self.ecg_removal_rate.setAcceptDrops(False)
        self.ecg_removal_rate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ecg_removal_rate.setStyleSheet("background: transparent;\n"
                                            "border: 2px solid \'black\';\n"
                                            "border-radius: 10;\n"
                                            "color:black;\n"
                                            "font: 16pt \"Montserrat\";")
        self.ecg_removal_rate.setText("")
        self.ecg_removal_rate.setObjectName("ecg_removal_rate")
        self.gridLayout.addWidget(self.ecg_removal_rate, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("background: transparent;\n"
                                   "")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(180, 80, 391, 221))
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setStyleSheet("background:transparent;")
        self.graphicsView.setInteractive(True)
        self.graphicsView.setObjectName("graphicsView")
        self.layoutWidget.raise_()
        self.btn_calc_pulse.raise_()
        self.label.raise_()
        self.graphicsView.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 778, 21))
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
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:24pt;\">Калькулятор пульса по результатам ЭКГ</span></p></body></html>"))
        self.btn_calc_pulse.setText(_translate("MainWindow", "Рассчитать пульс"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:18pt;\">Скорость снятия кардиограммы</span></p></body></html>"))
        self.dist_between_teeth.setToolTip(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.dist_between_teeth.setWhatsThis(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">ygfhgh</p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:18pt;\">Расстояние между зубцами</span></p></body></html>"))
        self.ecg_removal_rate.setToolTip(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.ecg_removal_rate.setWhatsThis(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">ygfhgh</p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:18pt;\">Пульс</span></p></body></html>"))


