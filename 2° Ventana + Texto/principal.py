# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sys,datetime

hora_actual = datetime.datetime.now()

# Variables a usar

hora     = int(hora_actual.hour)
minutos  = int(hora_actual.minute)
segundos = int(hora_actual.second)

tiempo = hora,minutos,segundos



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/arepacoin.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(466, 296, 121, 41))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        self.menuMen = QtWidgets.QMenu(self.menubar)
        self.menuMen.setObjectName("menuMen")
        self.menuA_yuda = QtWidgets.QMenu(self.menubar)
        self.menuA_yuda.setObjectName("menuA_yuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.action_Cerrar = QtWidgets.QAction(MainWindow)
        self.action_Cerrar.setObjectName("action_Cerrar")
        self.actionA_cerca_de = QtWidgets.QAction(MainWindow)
        self.actionA_cerca_de.setObjectName("actionA_cerca_de")
        self.menuMen.addAction(self.actionAbrir)
        self.menuMen.addAction(self.action_Cerrar)
        self.menuA_yuda.addAction(self.actionA_cerca_de)
        self.menubar.addAction(self.menuMen.menuAction())
        self.menubar.addAction(self.menuA_yuda.menuAction())

        self.retranslateUi(MainWindow)
        self.action_Cerrar.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", str(tiempo)))
        self.menuMen.setTitle(_translate("MainWindow", "&Menú"))
        self.menuA_yuda.setTitle(_translate("MainWindow", "Ay&uda"))
        self.actionAbrir.setText(_translate("MainWindow", "&Abrir"))
        self.action_Cerrar.setText(_translate("MainWindow", "&Cerrar"))
        self.actionA_cerca_de.setText(_translate("MainWindow", "A&cerca de ..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

