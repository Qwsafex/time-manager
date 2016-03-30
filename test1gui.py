# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(557, 341)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.chActButton = QtGui.QPushButton(self.centralWidget)
        self.chActButton.setGeometry(QtCore.QRect(280, 180, 111, 31))
        self.chActButton.setObjectName(_fromUtf8("chActButton"))
        self.newActEdit = QtGui.QLineEdit(self.centralWidget)
        self.newActEdit.setGeometry(QtCore.QRect(60, 180, 191, 31))
        self.newActEdit.setObjectName(_fromUtf8("newActEdit"))
        self.timerView = QtGui.QTextEdit(self.centralWidget)
        self.timerView.setGeometry(QtCore.QRect(210, 10, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.timerView.setFont(font)
        self.timerView.setReadOnly(True)
        self.timerView.setObjectName(_fromUtf8("timerView"))
        self.curActView = QtGui.QTextEdit(self.centralWidget)
        self.curActView.setGeometry(QtCore.QRect(110, 90, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.curActView.setFont(font)
        self.curActView.setReadOnly(True)
        self.curActView.setObjectName(_fromUtf8("curActView"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 557, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.chActButton.setText(_translate("MainWindow", "Change activity", None))

