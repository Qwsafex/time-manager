import sys
import datetime
from collections import defaultdict

from PyQt4 import QtCore
from PyQt4 import QtGui
from test1gui import Ui_MainWindow
import collector

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


# Return list [seconds, minutes, hours] from 'time' in seconds
def disassembleTime(time, addZeros=True):
    base = [60, 60]
    res = []
    for b in base:
        res.append(str(time % b))
        if addZeros and len(res[-1]) == 1:
            res[-1] = "0" + res[-1]
        time = time // b

    res.append(str(time))
    if addZeros and len(res[-1]) == 1:
        res[-1] = "0" + res[-1]

    return res


class Plan:
    total = 0

    def __init__(self, plan):
        self.activity = plan[0]
        self.desiredTime = int(plan[1])
        self.completedTime = int(plan[2])

    def getDesc(self):
        compTimeL = disassembleTime(self.completedTime, False)
        desTimeL = disassembleTime(self.desiredTime, False)
        return "({0}h{1}m/{2}h{3}m) {4}".format(
                    compTimeL[2],
                    compTimeL[1],
                    desTimeL[2],
                    desTimeL[1],
                    self.activity)


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.chActButton.clicked.connect(self.manualActivity)
        self.ui.pauseButton.clicked.connect(self.setPause)
        self.ui.planAddButton.clicked.connect(self.onClickAddPlan)
        self.ui.planDelButton.clicked.connect(self.onClickDelPlan)

        self.ui.suggestionList.itemClicked.connect(self.suggestedActivity)

        self.initTimer()
        self.initLog()
        self.readPlans()

        self.pTimerValue = PAUSE_DURATION
        self.paused = False
        self.todayStatistics = defaultdict(int)

    def onClickDelPlan(self):
        delText = self.ui.plansList.selectedItems()[0].text()
        for plan in self.plans:
            if plan.getDesc() == delText:
                self.plans.remove(plan)
                Plan.total -= plan.desiredTime
                self.ui.hoursPlannedLabel.setText(str(Plan.total // 3600))
                activity = plan.activity
                break
        for i in range(self.ui.suggestionList.count()):
            if self.ui.suggestionList.item(i).text() == activity:
                self.ui.suggestionList.takeItem(i)
                break
        for i in range(self.ui.plansList.count()):
            if self.ui.plansList.item(i).text() == delText:
                self.ui.plansList.takeItem(i)
                break

    def onClickAddPlan(self):
        self.addPlan([self.ui.newPlanEdit.text(),
                      self.ui.minutesEdit.value()*60 +
                      self.ui.hoursEdit.value()*3600,
                      0])
        self.ui.newPlanEdit.setText("")
        self.ui.minutesEdit.setValue(0)
        self.ui.hoursEdit.setValue(0)

    def addPlan(self, planInfo):
        newPlan = Plan(planInfo)

        Plan.total += newPlan.desiredTime
        self.ui.hoursPlannedLabel.setText(str(Plan.total // 3600))

        self.plans.append(newPlan)
        planDesc = newPlan.getDesc()
        self.ui.plansList.addItem(planDesc)
        self.ui.suggestionList.addItem(newPlan.activity)

    def readPlans(self):
        planfile = open("TM-data", "r")
        curline = planfile.readline()
        self.plans = []
        while curline != "":
            self.addPlan(curline.split('|'))
            curline = planfile.readline()

    def savePlans(self):
        planfile = open("TM-data", "w")
        for plan in self.plans:
            planfile.write("{0}|{1}|{2}\n".format(plan.activity,
                                                  plan.desiredTime,
                                                  plan.completedTime))
        planfile.close()

    def initLog(self):
        curdate = datetime.date.today().isoformat().split('-')
        year = str(int(curdate[0]) % 100)

        # TODO: "format".format()
        curdate = year + "." + curdate[1] + "." + curdate[2]
        self.logFile = open(curdate+"-TM-log.txt", "a")

    def initTimer(self):
        self.timerValue = 0
        timer = QtCore.QTimer(self)
        self.connect(timer, QtCore.SIGNAL("timeout()"), self.timerTick)
        timer.start(1000)


    def suggestedActivity(self, item):
        self.changeActivity(item.text())

    def setPause(self):
        self.paused = True

    def timerTick(self):
        if self.pTimerValue == 0:
            self.paused = False
            self.pTimerValue = PAUSE_DURATION

        if not self.paused:
            #print("mek")
            timeL = disassembleTime(self.timerValue)
            self.timerValue += 1
        else:
           # print("fek")
            timeL = disassembleTime(self.pTimerValue)
            self.pTimerValue -= 1

      #  print(self.timerValue)
        if timeL[2] == "00":
            self.ui.timerView.setText(timeL[1] + ":" + timeL[0])
        else:
            self.ui.timerView.setText(timeL[2] + ":" + timeL[1] + 
                                      ":" + timeL[0])

        self.ui.timerView.setAlignment(QtCore.Qt.AlignRight | 
                                            QtCore.Qt.AlignVCenter)


    def logActivity(self):
        activity = self.ui.curActView.toPlainText()
        timeSpent = str(self.timerValue)

        for plan in self.plans:
            if activity == plan.activity:
                qitem = self.ui.plansList.findItems(plan.getDesc(),
                                                    QtCore.Qt.MatchExactly)[0]
                plan.completedTime += int(timeSpent)
                qitem.setText(plan.getDesc())
                break

        humanReadable = self.ui.curActView.toPlainText() + " for " + \
                               str(self.timerValue // 60) + " minutes " + \
                               str(self.timerValue % 60) + " seconds"
        resString =  humanReadable + "|" + activity + \
                    "|" + timeSpent + "\n"
        self.logFile.write(resString)
        self.logFile.flush()

    def manualActivity(self):
        self.changeActivity(self.ui.newActEdit.text())
        self.ui.newActEdit.setText("")

    def changeActivity(self, newAct):
        # Update today statistics
        currentAct = self.ui.curActView.toPlainText()
        if currentAct != "":
            self.todayStatistics[currentAct] += self.timerValue
            self.ui.todayStatisticsDisplay.setText(collector.statisticsText(
                                                    self.todayStatistics))

        # Write to logs
        if self.ui.curActView.toPlainText() != "":
            self.logActivity()

        # Reset timer
        self.timerValue = 0

        # Display new activity
        self.ui.curActView.setText(newAct)

        # Write the start time of new activity to log
        if self.ui.curActView.toPlainText() == "":
            return

        curtime = datetime.datetime.now().time()
        minutes = str(curtime.minute)
        if len(minutes) == 1:
            minutes = "0" + minutes
        when = str(curtime.hour) + ":" + minutes
        self.logFile.write(when+"|")
        self.logFile.flush()

    def closeEvent(self, event):
        self.changeActivity("")
        self.savePlans()
        event.accept()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
