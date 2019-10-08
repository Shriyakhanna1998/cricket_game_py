# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QInputDialog
import sqlite3

class Ui_Form(QWidget):
    total_points=0
    total=0
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(497, 503)
        Form.setStyleSheet("background-color: rgb(136, 138, 133);\n""background-color: rgb(186, 189, 182);")
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.evaluate = QtWidgets.QLabel(Form)
        self.evaluate.setGeometry(QtCore.QRect(120, 10, 281, 31))
        self.evaluate.setObjectName("evaluate")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 481, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.combo2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.combo2.setObjectName("combo2")
        self.combo2.addItem("")
        self.horizontalLayout.addWidget(self.combo2)
        self.combo1 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.combo1.setObjectName("combo1")
        self.combo1.addItem("")
        self.horizontalLayout.addWidget(self.combo1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(30, 130, 441, 31))
        self.line.setStyleSheet("color: rgb(0, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.list1 = QtWidgets.QListWidget(self.centralwidget)
        self.list1.setGeometry(QtCore.QRect(20, 190, 191, 251))
        self.list1.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.list1.setObjectName("list1")
        self.list2 = QtWidgets.QListWidget(self.centralwidget)
        self.list2.setGeometry(QtCore.QRect(280, 190, 191, 251))
        self.list2.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.list2.setObjectName("list2")
        self.players = QtWidgets.QLabel(Form)
        self.players.setGeometry(QtCore.QRect(20, 160, 67, 17))
        self.players.setObjectName("players")
        self.points = QtWidgets.QLabel(Form)
        self.points.setGeometry(QtCore.QRect(280, 160, 67, 17))
        self.points.setObjectName("points")
        self.pts = QtWidgets.QLabel(Form)
        self.pts.setGeometry(QtCore.QRect(380, 160, 67, 17))
        self.pts.setObjectName("pts")
        self.calculate = QtWidgets.QPushButton(Form)
        self.calculate.setEnabled(False)
        self.calculate.setGeometry(QtCore.QRect(180, 460, 141, 25))
        self.calculate.setStyleSheet("background-color: rgb(136, 138, 133);\n""background-color: rgb(136, 138, 133);")
        self.calculate.setObjectName("calculate")
        self.selectTeam()
        self.combo2.activated.connect(self.selectTeamItem)
        self.selectMatch()
        self.combo1.activated.connect(self.selectMatchItem)
        self.calculate.clicked.connect(self.score)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.evaluate.setText(_translate("Form", "Evaluate the score of Your Fantasy Team"))
        self.combo2.setItemText(0, _translate("Form", "Select Team"))
        self.combo1.setItemText(0, _translate("Form", "Select Match"))
        self.players.setText(_translate("Form", "Players"))
        self.points.setText(_translate("Form", "Points"))
        self.pts.setText(_translate("Form", "##"))
        self.calculate.setText(_translate("Form", "Calculate Score"))

    def selectTeam(self):
        self.combo1.setEnabled(False)
        select=sqlite3.connect("cricket.db")
        curselect=select.cursor()
        name_team="SELECT DISTINCT Name FROM teams;"
        curselect.execute(name_team)
        results=curselect.fetchall()
        for result in results:
            result=(str)(result[0])
            self.combo2.addItem(result)
    def selectTeamItem(self):
        self.list2.clear()
        select=sqlite3.connect("cricket.db")
        curselect=select.cursor()
        selected=self.combo2.currentText()
        if selected == 'Select Team':
            self.list1.clear()
            self.combo1.setEnabled(False)
            msg = QMessageBox()
            msg.setText("Please Select your Team.")
            msg.exec()
        else:
            self.combo1.setEnabled(True)
            self.list1.clear()
            players_team="SELECT Players FROM teams WHERE Name='"+selected+"';"
            curselect.execute(players_team)
            fetch_players=curselect.fetchall()
            for fetch_player in fetch_players:
                self.list1.addItem((str)(fetch_player[0]))
    def selectMatch(self):
        self.combo1.addItem('Match1')
        self.combo1.addItem('Match2')
        self.combo1.addItem('Match3')
        self.combo1.addItem('Match4')
        self.combo1.addItem('Match5')
        self.combo1.addItem('Match6')
        self.combo1.addItem('Match7')
        
    def selectMatchItem(self):
        self.total=0
        selected_match=self.combo1.currentText()
        if selected_match == 'Select Match':
            msg1 = QMessageBox()
            msg1.setText("Please Select a Match.")
            msg1.exec()
        else:
            self.calculatePoints()
    def calculatePoints(self):
        self.list2.clear()
        self.total_points=0
        team=self.combo2.currentText()
        select=sqlite3.connect("cricket.db")
        curselect=select.cursor()
        fetch_players="SELECT Players from teams WHERE Name='"+team+"';"
        curselect.execute(fetch_players)
        fetch=curselect.fetchall()
        for fet in fetch:
            self.total_points=0
            self.batting((str)(fet[0]))
            self.bowling((str)(fet[0]))

    def batting(self, player):
        select=sqlite3.connect("cricket.db")
        curselect=select.cursor()
        fetch_info="SELECT Scored, Faced, Fours, Sixes,Catches ,Stumping, RO from match WHERE Player='"+player+"';"
        curselect.execute(fetch_info)
        fetch=curselect.fetchall()
        pts=0
        strike_rate=0
        for fet in fetch:
            runs=(int)((str)(fet[0]))
            balls=(int)((str)(fet[1]))
            fours=(int)((str)(fet[2]))
            sixes=(int)((str)(fet[3]))
            Catches=(int)((str)(fet[4]))
            Stump=(int)((str)(fet[5]))
            run_out=(int)((str)(fet[6]))
            pts=runs/2
            if runs>=50 and runs<100:
                pts=pts+5
            if runs>=150 and runs<200:
                pts=pts+5
            if runs>=100 and runs<150:
                pts=pts+10
            if balls != 0:
                strike_rate=(runs/balls)*100
            if strike_rate>=80 and strike_rate<=100:
                pts=pts+2
            if strike_rate>100:
                pts=pts+4
            pts=pts+fours
            pts=pts+(sixes*2)
            pts=pts+10*(Catches+Stump+run_out)
        self.total_points=self.total_points+(int)(pts)
        self.total=self.total+self.total_points
        
    def bowling(self,player):
        select=sqlite3.connect("cricket.db")
        curselect=select.cursor()
        fetch_info="SELECT Scored, Faced, Wkts from match WHERE Player='"+player+"';"
        curselect.execute(fetch_info)
        fetch=curselect.fetchall()
        pts=0
        economy_rate=0
        for fet in fetch:
            runs=(int)((str)(fet[0]))
            balls=(int)((str)(fet[1]))
            wickets=(int)((str)(fet[2]))
            pts=wickets
            if wickets>=3 and wickets<5:
                pts=pts+5
            elif wickets>=5:
                pts=pts+10
            if balls != 0 and runs!=0 :
                over=balls/6
                economy_rate=runs/over
            if economy_rate>=3.5 and economy_rate<=4.5:
                pts=pts+4
            elif economy_rate>=2.0 and economy_rate<3.5:
                pts=pts+7
            elif economy_rate<2.0:
                pts=pts+10
        self.total_points=self.total_points+(int)(pts)
        self.total=self.total+self.total_points
        self.Evaluate()
    def Evaluate(self):
        self.list2.addItem((str)(self.total_points))
        if self.list2.count() == 11:
            self.calculate.setEnabled(True)
    def score(self):
        self.pts.setText((str)(self.total))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
