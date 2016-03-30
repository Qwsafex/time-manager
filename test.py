import sys
	
from PyQt4 import QtCore
from PyQt4 import QtGui
from test1gui import Ui_MainWindow

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.chActButton.clicked.connect(self.changeActivity)

        self.timerValue = 0
        timer = QtCore.QTimer(self)
        self.connect(timer, QtCore.SIGNAL("timeout()"), self.updTimer)
        timer.start(1000)

        self.logFile = open("time-manager-log.txt", "a")

    def updTimer(self):
        minutes = str(self.timerValue//60)
        seconds = str(self.timerValue%60)
        if len(seconds) == 1:
            seconds = "0" + seconds
        self.ui.timerView.setText(minutes + ":" + seconds)
        self.timerValue += 1


    def logString(self):
        activity = self.ui.curActView.toPlainText()
        timeSpent = str(self.timerValue)
        humanReadable = self.ui.curActView.toPlainText() + " for " + \
                               str(self.timerValue//60) + " minutes " + \
                               str(self.timerValue % 60) + " seconds"
        resString = humanReadable + "|" + activity + "|" + timeSpent + "\n"
        return resString

    def changeActivity(self):
    	# Write to logs
        if self.ui.curActView.toPlainText() != "":
            self.logFile.write(self.logString())

    	# Reset timer
        self.timerValue = 0

    	# Display new activity
        self.ui.curActView.setText(self.ui.newActEdit.text())
        self.ui.newActEdit.setText("")

    def closeEvent(self, event):
        self.changeActivity()
        event.accept()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
