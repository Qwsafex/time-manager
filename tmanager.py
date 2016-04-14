import sys
import datetime
	
from PyQt4 import QtCore
from PyQt4 import QtGui
from test1gui import Ui_MainWindow

PAUSE_DURATION = 120

'''
class keyEnterReceiver(QtCore.QObject):
    def eventFilter(self, obj, event):
        print(event.type())
        if event.type() == QtCore.QEvent.KeyPress:
            if (event.key() == QtCore.Key_Enter) or (event.key() == QtCore.Key_Return):
                print("heh")    
                return True
            else:
                return QtCore.QObject.eventFilter(obj, event);
        else:
            return QtCore.QObject.eventFilter(obj, event);
#        return False
'''

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.chActButton.clicked.connect(self.manualActivity)
        self.ui.pauseButton.clicked.connect(self.setPause)

        self.ui.suggestionList.itemClicked.connect(self.suggestedActivity)

        self.timerValue = 0
        timer = QtCore.QTimer(self)
        self.connect(timer, QtCore.SIGNAL("timeout()"), self.timerTick)
        timer.start(1000)

        curdate = datetime.date.today().isoformat().split('-')
        year = str(int(curdate[0]) % 100)

        # TODO: "format".format()
        curdate = year + "." + curdate[1] + "." + curdate[2]
        self.logFile = open(curdate+"-TM-log.txt", "a")
        #self.logFile = open("kek.txt", "a")

        self.pTimerValue = PAUSE_DURATION
        self.paused = False

        self.ui.label.setText("oh heheheh")


    def suggestedActivity(self, item):
        self.changeActivity(item.text())

    def setPause(self):
        self.paused = True

    # Return list [seconds, minutes, hours, days] from 'time' in seconds
    def disassembleTime(self, time):
        base = [60,60,24]
        res = []
        for b in base:
            res.append(str(time % b))
            if len(res[-1]) == 1:
                res[-1] = "0" + res[-1]
            time = time // b
        res.append(time)
        return res

    def timerTick(self):
        if self.pTimerValue == 0:
            self.paused = False
            self.pTimerValue = PAUSE_DURATION

        if not self.paused:
            #print("mek")
            timeL = self.disassembleTime(self.timerValue)
            self.timerValue += 1
        else:
           # print("fek")
            timeL = self.disassembleTime(self.pTimerValue)
            self.pTimerValue -= 1

      #  print(self.timerValue)
        if timeL[2] == "00":
            self.ui.timerView.setText(timeL[1] + ":" + timeL[0])
        else:
            self.ui.timerView.setText(timeL[2] + ":" + timeL[1] + 
                                      ":" + timeL[0])
        self.ui.timerView.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)


    def logString(self):
        activity = self.ui.curActView.toPlainText()
        timeSpent = str(self.timerValue)
        humanReadable = self.ui.curActView.toPlainText() + " for " + \
                               str(self.timerValue // 60) + " minutes " + \
                               str(self.timerValue % 60) + " seconds"
        resString =  humanReadable + "|" + activity + \
                    "|" + timeSpent + "\n"
        return resString

    def manualActivity(self):
        self.changeActivity(self.ui.newActEdit.text())
        self.ui.newActEdit.setText("")

    def changeActivity(self, newAct):
    	# Write to logs
        if self.ui.curActView.toPlainText() != "":
            self.logFile.write(self.logString())
            self.logFile.flush()

    	# Reset timer
        self.timerValue = 0

        # Display new activity
        self.ui.curActView.setText(newAct)

        #Write the start time of new activity to log
        if self.ui.curActView.toPlainText() == "":
            return

        curtime = datetime.datetime.now().time()
        minutes = str(curtime.minute)
        if len(minutes) == 1:
            minutes = "0" + minutes
        when = str(curtime.hour) + ":" + minutes
        self.logFile.write(when+"|");
        self.logFile.flush()

    def closeEvent(self, event):
        self.changeActivity("")
        event.accept()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
