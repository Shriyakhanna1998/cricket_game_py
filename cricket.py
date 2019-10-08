# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cricket.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QInputDialog, QMessageBox
import sqlite3
from Evaluate import Ui_Form

class Ui_MainWindow(QWidget):
    res=0
    count=0
    countBAT=0
    countBWL=0
    countAR=0
    countWK=0
    batcount=0
    bwlcount=0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(677, 600)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 651, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.selections = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.selections.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.selections.setObjectName("selections")
        self.horizontalLayout_4.addWidget(self.selections)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(379, 160, 281, 21))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.points_used = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.points_used.setObjectName("points_used")
        self.horizontalLayout_10.addWidget(self.points_used)
        self.used = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.used.setStyleSheet("color: rgb(52, 101, 164);")
        self.used.setObjectName("used")
        self.horizontalLayout_10.addWidget(self.used)
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setGeometry(QtCore.QRect(10, 50, 651, 80))
        self.verticalWidget.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget_2.setGeometry(QtCore.QRect(9, 39, 651, 91))
        self.horizontalWidget_2.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.batsmen = QtWidgets.QLabel(self.horizontalWidget_2)
        self.batsmen.setObjectName("batsmen")
        self.horizontalLayout.addWidget(self.batsmen)
        self.no_batsmen = QtWidgets.QLabel(self.horizontalWidget_2)
        self.no_batsmen.setStyleSheet("color: rgb(52, 101, 164);")
        self.no_batsmen.setObjectName("no_batsmen")
        self.horizontalLayout.addWidget(self.no_batsmen)
        self.bowlers = QtWidgets.QLabel(self.horizontalWidget_2)
        self.bowlers.setObjectName("bowlers")
        self.horizontalLayout.addWidget(self.bowlers)
        self.no_bowlers = QtWidgets.QLabel(self.horizontalWidget_2)
        self.no_bowlers.setStyleSheet("color: rgb(52, 101, 164);")
        self.no_bowlers.setObjectName("no_bowlers")
        self.horizontalLayout.addWidget(self.no_bowlers)
        self.all_rounders = QtWidgets.QLabel(self.horizontalWidget_2)
        self.all_rounders.setObjectName("all_rounders")
        self.horizontalLayout.addWidget(self.all_rounders)
        self.no_all_rounders = QtWidgets.QLabel(self.horizontalWidget_2)
        self.no_all_rounders.setStyleSheet("color: rgb(52, 101, 164);")
        self.no_all_rounders.setObjectName("no_all_rounders")
        self.horizontalLayout.addWidget(self.no_all_rounders)
        self.wicket_keepers = QtWidgets.QLabel(self.horizontalWidget_2)
        self.wicket_keepers.setObjectName("wicket_keepers")
        self.horizontalLayout.addWidget(self.wicket_keepers)
        self.no_wicket_keeper = QtWidgets.QLabel(self.horizontalWidget_2)
        self.no_wicket_keeper.setStyleSheet("color: rgb(52, 101, 164);")
        self.no_wicket_keeper.setObjectName("no_wicket_keeper")
        self.horizontalLayout.addWidget(self.no_wicket_keeper)
        self.players = QtWidgets.QListWidget(self.centralwidget)
        self.players.setGeometry(QtCore.QRect(10, 250, 311, 341))
        self.players.setObjectName("players")
        self.team_players = QtWidgets.QListWidget(self.centralwidget)
        self.team_players.setGeometry(QtCore.QRect(380, 250, 261, 331))
        self.team_players.setObjectName("team_players")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 199, 311, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BAT = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.BAT.setEnabled(False)
        self.BAT.setCheckable(True)
        self.BAT.setChecked(False)
        self.BAT.setObjectName("BAT")
        self.horizontalLayout_2.addWidget(self.BAT)
        self.BOW = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.BOW.setEnabled(False)
        self.BOW.setObjectName("BOW")
        self.horizontalLayout_2.addWidget(self.BOW)
        self.AR = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.AR.setEnabled(False)
        self.AR.setObjectName("AR")
        self.horizontalLayout_2.addWidget(self.AR)
        self.WK = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.WK.setEnabled(False)
        self.WK.setObjectName("WK")
        self.horizontalLayout_2.addWidget(self.WK)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 160, 311, 27))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.points_available = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.points_available.setObjectName("points_available")
        self.horizontalLayout_3.addWidget(self.points_available)
        self.available = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.available.setStyleSheet("color: rgb(52, 101, 164);")
        self.available.setObjectName("available")
        self.horizontalLayout_3.addWidget(self.available)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(380, 199, 261, 61))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.team_name = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.team_name.setObjectName("team_name")
        self.horizontalLayout_5.addWidget(self.team_name)
        self.name = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.name.setStyleSheet("color: rgb(52, 101, 164);")
        self.name.setObjectName("name")
        self.horizontalLayout_5.addWidget(self.name)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 677, 22))
        self.menubar.setObjectName("menubar")
        self.menuMange_Teams = QtWidgets.QMenu(self.menubar)
        self.menuMange_Teams.setObjectName("menuMange_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.NEW_Team = QtWidgets.QAction(MainWindow)
        self.NEW_Team.setObjectName("NEW_Team")
        self.OPEN_Teams = QtWidgets.QAction(MainWindow)
        self.OPEN_Teams.setObjectName("OPEN_Teams")
        self.SAVE_Team = QtWidgets.QAction(MainWindow)
        self.SAVE_Team.setObjectName("SAVE_Team")
        self.EVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.EVALUATE_Team.setObjectName("EVALUATE_Team")
        self.menuMange_Teams.addAction(self.NEW_Team)
        self.menuMange_Teams.addAction(self.OPEN_Teams)
        self.menuMange_Teams.addAction(self.SAVE_Team)
        self.menuMange_Teams.addAction(self.EVALUATE_Team)
        self.menubar.addAction(self.menuMange_Teams.menuAction())
        self.NEW_Team.triggered.connect(self.showDialog)
        self.SAVE_Team.triggered.connect(self.showDialog2)
        self.OPEN_Teams.triggered.connect(self.showDialog3)
        self.BAT.clicked.connect(self.fetchBatsmen)
        self.BOW.clicked.connect(self.fetchBowlers)
        self.AR.clicked.connect(self.fetchAR)
        self.WK.clicked.connect(self.fetchWK)
        self.players.itemDoubleClicked.connect(self.removeList1)
        self.team_players.itemDoubleClicked.connect(self.removeList2)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.EVALUATE_Team.triggered.connect(self.showEvaluate)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selections.setText(_translate("MainWindow", "Your Selections"))
        self.points_used.setText(_translate("MainWindow", "Points Used"))
        self.used.setText(_translate("MainWindow", "####"))
        self.batsmen.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.no_batsmen.setText(_translate("MainWindow", "##"))
        self.bowlers.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.no_bowlers.setText(_translate("MainWindow", "##"))
        self.all_rounders.setText(_translate("MainWindow", "All Rounders(AR)"))
        self.no_all_rounders.setText(_translate("MainWindow", "##"))
        self.wicket_keepers.setText(_translate("MainWindow", "Wicket-keepers(WK)"))
        self.no_wicket_keeper.setText(_translate("MainWindow", "##"))
        self.BAT.setText(_translate("MainWindow", "BAT"))
        self.BOW.setText(_translate("MainWindow", "BOW"))
        self.AR.setText(_translate("MainWindow", "AR"))
        self.WK.setText(_translate("MainWindow", "WK"))
        self.points_available.setText(_translate("MainWindow", "Points Available"))
        self.available.setText(_translate("MainWindow", "####"))
        self.team_name.setText(_translate("MainWindow", "Team Name"))
        self.name.setText(_translate("MainWindow", "Displayed here"))
        self.menuMange_Teams.setTitle(_translate("MainWindow", "Mange Teams"))
        self.NEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.OPEN_Teams.setText(_translate("MainWindow", "OPEN Team"))
        self.SAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.EVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
    def showDialog(self):
        team, name1=QInputDialog.getText(self, 'Team name', 'Enter the Name')
        self.name.setText(str(team))
        if self.name.text() == '' :
            msg = QMessageBox()
            msg.setText("The Team must have a name.")
            msg.exec()
        else :
            self.BAT.setEnabled(True)
            self.BOW.setEnabled(True)
            self.AR.setEnabled(True)
            self.WK.setEnabled(True)
            self.available.setText('1000')
            self.used.setText('0')
    def fetchBatsmen(self):
        self.players.clear()
        player=sqlite3.connect("cricket.db")
        curplay=player.cursor()
        curplay.execute("SELECT Player from stats WHERE Ctg='BAT'")
        results=curplay.fetchall()
        for result in results:
            self.players.addItem(result[0])
    def fetchBowlers(self):
        self.players.clear()
        player=sqlite3.connect("cricket.db")
        curplay=player.cursor()
        curplay.execute("SELECT Player from stats WHERE Ctg='BWL'")
        results=curplay.fetchall()
        for result in results:
            self.players.addItem(result[0])

    def fetchAR(self):
        self.players.clear()
        player=sqlite3.connect("cricket.db")
        curplay=player.cursor()
        curplay.execute("SELECT Player from stats WHERE Ctg='AR'")
        results=curplay.fetchall()
        for result in results:
            self.players.addItem(result[0])
    def fetchWK(self):
        self.players.clear()
        player=sqlite3.connect("cricket.db")
        curplay=player.cursor()
        curplay.execute("SELECT Player from stats WHERE Ctg='WK'")
        results=curplay.fetchall()
        for result in results:
            self.players.addItem(result[0])
    def removeList1(self, item):
        self.batcount = 1
        self.bwlcount = 1
        if self.team_players.count() <= 10:
            self.players.takeItem(self.players.row(item))
            if item.text() == 'Bumrah' or item.text() == 'Umesh':
                self.count=self.count+1
                if self.count > 1:
                    self.players.addItem(item.text())
                    self.msg = QMessageBox()
                    self.msg.setText("The wicket keeper cannot be more than 1 in the team.")
                    self.msg.exec()
                else:
                    self.calculatePoints(item.text())
            else :
                self.calculatePoints(item.text())
                
        else:
            msg = QMessageBox()
            msg.setText("The Players cannot be more than 11")
            msg.exec()
    def calculatePoints(self, item):
        value=sqlite3.connect("cricket.db")
        curvalue=value.cursor()
        sql="SELECT Value from stats WHERE Player='"+item+"';"
        curvalue.execute(sql)
        val=curvalue.fetchone()
        for result in val:
            result=(int)(result)
        self.res=result+self.res
        avail=1000-self.res
        self.used.setText((str)(self.res))
        self.available.setText((str)(avail))
        number="SELECT Ctg from stats WHERE Player='"+item+"';"
        curvalue.execute(number)
        value=curvalue.fetchall()
        self.team_players.addItem(item)
        for catog in value:
            catog=(str)(catog[0])
            if catog == 'BAT' :
                self.countBAT=self.countBAT+1
            elif catog == 'BWL' :
                self.countBWL=self.countBWL+1
            elif catog == 'AR' :
                self.countAR=self.countAR+1
            elif catog == 'WK' :
                self.countWK=self.countWK+1
        self.no_batsmen.setText((str)(self.countBAT))
        self.no_bowlers.setText((str)(self.countBWL))
        self.no_all_rounders.setText((str)(self.countAR))
        self.no_wicket_keeper.setText((str)(self.countWK))
    def removeList2(self, item):
        self.team_players.takeItem(self.team_players.row(item))
        self.players.addItem(item.text())
    def showDialog2(self):
        data=sqlite3.connect("cricket.db")
        curdata=data.cursor()
        self.team_name = self.name.text()
        row = 0
        while row < self.team_players.count():
            sql="SELECT Value from stats WHERE Player='"+self.team_players.item(row).text()+"';"
            curdata.execute(sql)
            val=curdata.fetchone()
            for result in val:
                result=(int)(result)
            curdata.execute("INSERT INTO teams(Name, Players, Value) VALUES(?,?,?);",(self.team_name, self.team_players.item(row).text(), result))
            data.commit()
            row = row+1
        msg = QMessageBox()
        msg.setText("Your Team has been successfully saved. ")
        msg.exec()
    def showDialog3(self):
        i=0
        item=[]
        self.team_players.clear()
        data=sqlite3.connect("cricket.db")
        curdata=data.cursor()
        sql="SELECT DISTINCT name FROM teams;"
        curdata.execute(sql)
        data1=curdata.fetchall()
        for teamName in data1:
            item.append((str)(teamName[0]))
        item=tuple(item)
        team_name, open_team = QInputDialog.getItem(self, "Open team name", "list of team names", item)
        self.name.setText(team_name)
        fetch_data="SELECT Players from teams WHERE name='"+team_name+"';"
        curdata.execute(fetch_data)
        fetch=curdata.fetchall()
        for result in fetch:
            self.calculatePoints(result[0])
        i=i+1
    def showEvaluate(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

