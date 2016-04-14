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
        MainWindow.resize(750, 441)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 741, 391))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Current = QtGui.QWidget()
        self.Current.setObjectName(_fromUtf8("Current"))
        self.timerView = QtGui.QTextEdit(self.Current)
        self.timerView.setGeometry(QtCore.QRect(80, 20, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.timerView.setFont(font)
        self.timerView.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.timerView.setReadOnly(True)
        self.timerView.setObjectName(_fromUtf8("timerView"))
        self.pauseButton = QtGui.QPushButton(self.Current)
        self.pauseButton.setGeometry(QtCore.QRect(110, 100, 99, 27))
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.curActView = QtGui.QTextEdit(self.Current)
        self.curActView.setGeometry(QtCore.QRect(20, 160, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.curActView.setFont(font)
        self.curActView.setReadOnly(True)
        self.curActView.setObjectName(_fromUtf8("curActView"))
        self.chActButton = QtGui.QPushButton(self.Current)
        self.chActButton.setGeometry(QtCore.QRect(540, 290, 111, 31))
        self.chActButton.setObjectName(_fromUtf8("chActButton"))
        self.newActEdit = QtGui.QLineEdit(self.Current)
        self.newActEdit.setGeometry(QtCore.QRect(500, 250, 191, 31))
        self.newActEdit.setObjectName(_fromUtf8("newActEdit"))
        self.suggestionList = QtGui.QListWidget(self.Current)
        self.suggestionList.setGeometry(QtCore.QRect(500, 20, 191, 211))
        self.suggestionList.setObjectName(_fromUtf8("suggestionList"))
        self.tabWidget.addTab(self.Current, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.plansList = QtGui.QListWidget(self.tab_2)
        self.plansList.setGeometry(QtCore.QRect(40, 20, 191, 271))
        self.plansList.setObjectName(_fromUtf8("plansList"))
        self.newPlanEdit = QtGui.QTextEdit(self.tab_2)
        self.newPlanEdit.setGeometry(QtCore.QRect(280, 70, 161, 31))
        self.newPlanEdit.setObjectName(_fromUtf8("newPlanEdit"))
        self.planAddButton = QtGui.QPushButton(self.tab_2)
        self.planAddButton.setGeometry(QtCore.QRect(380, 120, 99, 27))
        self.planAddButton.setObjectName(_fromUtf8("planAddButton"))
        self.hoursEdit = QtGui.QSpinBox(self.tab_2)
        self.hoursEdit.setGeometry(QtCore.QRect(450, 70, 48, 27))
        self.hoursEdit.setObjectName(_fromUtf8("hoursEdit"))
        self.minutesEdit = QtGui.QSpinBox(self.tab_2)
        self.minutesEdit.setGeometry(QtCore.QRect(520, 70, 48, 27))
        self.minutesEdit.setObjectName(_fromUtf8("minutesEdit"))
        self.hoursLabel = QtGui.QLabel(self.tab_2)
        self.hoursLabel.setGeometry(QtCore.QRect(500, 70, 21, 31))
        self.hoursLabel.setObjectName(_fromUtf8("hoursLabel"))
        self.hoursLabel_2 = QtGui.QLabel(self.tab_2)
        self.hoursLabel_2.setGeometry(QtCore.QRect(570, 70, 41, 31))
        self.hoursLabel_2.setObjectName(_fromUtf8("hoursLabel_2"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(310, 250, 67, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 750, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Time Manager", None))
        self.pauseButton.setText(_translate("MainWindow", "Pause", None))
        self.chActButton.setText(_translate("MainWindow", "Change activity", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Current), _translate("MainWindow", "Current", None))
        self.planAddButton.setText(_translate("MainWindow", "Add plan", None))
        self.hoursLabel.setText(_translate("MainWindow", "hh", None))
        self.hoursLabel_2.setText(_translate("MainWindow", "mm", None))
        self.label.setText(_translate("MainWindow", "0 hours total", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Plans", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Statistics", None))

