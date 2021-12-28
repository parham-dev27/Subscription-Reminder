#!/usr/bin/env Python3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QDate, QTime
import datetime
import dbCommands as DataBase

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.now = datetime.datetime.now()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 591)
        MainWindow.setMinimumSize(QtCore.QSize(360, 591))
        MainWindow.setMaximumSize(QtCore.QSize(360, 591))
        MainWindow.setStyleSheet("background-color: rgb(49, 49, 49);\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, -21, 371, 621))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(0, 20, 361, 591))
        font = QtGui.QFont()
        font.setFamily("PT Mono")
        font.setPointSize(44)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.label.setStyleSheet("color: rgba(148, 33, 146, 230);\n")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.toolsB = QtWidgets.QPushButton(self.page_2)
        self.toolsB.setGeometry(QtCore.QRect(1, 551, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.toolsB.setFont(font)
        self.toolsB.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.toolsB.setStyleSheet("color: rgba(148, 33, 146, 230);\n"
        "background-color: rgb(43, 43, 43);\n"
        "border: 2px solid rgba(148, 33, 146, 230);")
        self.toolsB.setObjectName("toolsB")
        self.viewerB = QtWidgets.QPushButton(self.page_2)
        self.viewerB.setGeometry(QtCore.QRect(180, 551, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.viewerB.setFont(font)
        self.viewerB.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.viewerB.setStyleSheet("color: rgba(148, 33, 146, 230);\n"
        "background-color: rgb(43, 43, 43);\n"
        "border: 2px solid rgba(148, 33, 146, 230);")
        self.viewerB.setObjectName("viewerB")
        self.label2 = QtWidgets.QLabel(self.page_2)
        self.label2.setGeometry(QtCore.QRect(10, 40, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Times")
        font.setPointSize(37)
        self.label2.setFont(font)
        self.label2.setStyleSheet("color: rgba(148, 33, 146, 230);")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.endtimeL = QtWidgets.QLabel(self.page_2)
        self.endtimeL.setGeometry(QtCore.QRect(40, 170, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(21)
        self.endtimeL.setFont(font)
        self.endtimeL.setStyleSheet("color: rgba(148, 33, 146, 230);")
        self.endtimeL.setObjectName("endtimeL")
        self.timeEdit = QtWidgets.QTimeEdit(self.page_2)
        self.timeEdit.setGeometry(QtCore.QRect(140, 170, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.timeEdit.setFont(font)
        self.timeEdit.setStyleSheet("color: rgba(148, 33, 146, 230);\n"
        "background-color: rgb(43, 43, 43);\n"
        "border: 1px solid rgba(148, 33, 146, 230);\n")
        self.timeEdit.setTime(QTime(self.now.hour, self.now.minute, 0))
        self.timeEdit.setDisplayFormat("HH:mm")
        self.timeEdit.setObjectName("timeEdit")
        self.enddateL = QtWidgets.QLabel(self.page_2)
        self.enddateL.setGeometry(QtCore.QRect(40, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(21)
        self.enddateL.setFont(font)
        self.enddateL.setStyleSheet("color: rgba(148, 33, 146, 230);")
        self.enddateL.setObjectName("enddateL")
        self.dateEdit = QtWidgets.QDateEdit(self.page_2)
        self.dateEdit.setGeometry(QtCore.QRect(140, 220, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("color: rgba(148, 33, 146, 230);\n"
        "background-color: rgb(43, 43, 43);\n"
        "border: 1px solid rgba(148, 33, 146, 230);\n")
        self.dateEdit.setDisplayFormat("dd MMM yyyy")
        self.dateEdit.setMinimumDate(QDate(1000, 1, 1))
        self.dateEdit.setMaximumDate(QDate(9999, 12, 31))
        self.dateEdit.setDate(QDate(self.now.year, self.now.month, self.now.day))
        self.dateEdit.setObjectName("dateEdit")
        self.nameL = QtWidgets.QLabel(self.page_2)
        self.nameL.setGeometry(QtCore.QRect(40, 120, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(21)
        self.nameL.setFont(font)
        self.nameL.setToolTip("")
        self.nameL.setStyleSheet("color: rgba(148, 33, 146, 230);")
        self.nameL.setObjectName("nameL")
        self.lineEdit = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit.setGeometry(QtCore.QRect(110, 120, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(17)
        self.lineEdit.setFont(font)
        self.lineEdit.setAcceptDrops(False)
        self.lineEdit.setStyleSheet("color: rgba(148, 33, 146, 230);\n"
        "background-color: rgb(43, 43, 43);\n"
        "border: 1px solid rgba(148, 33, 146, 230);")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(22)
        self.lineEdit.setObjectName("lineEdit")
        self.deleteallB = QtWidgets.QPushButton(self.page_2)
        self.deleteallB.setGeometry(QtCore.QRect(60, 380, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.deleteallB.setFont(font)
        self.deleteallB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteallB.setStyleSheet("color: rgba(148, 33, 146, 230);\n"
        "background-color: rgb(43, 43, 43);\n"
        "border: 2px solid rgba(148, 33, 146, 230);\n"
        "border-radius: 15px;")
        self.deleteallB.setObjectName("deleteallB")
        self.deleteenteredB = QtWidgets.QPushButton(self.page_2)
        self.deleteenteredB.setGeometry(QtCore.QRect(60, 440, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.deleteenteredB.setFont(font)
        self.deleteenteredB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteenteredB.setStyleSheet("color: rgba(148, 33, 146, 230);\n"
        "background-color: rgb(43, 43, 43);\n"
        "border: 2px solid rgba(148, 33, 146, 230);\n"
        "border-radius: 15px;")
        self.deleteenteredB.setObjectName("deleteenteredB")
        self.addB = QtWidgets.QPushButton(self.page_2)
        self.addB.setGeometry(QtCore.QRect(60, 320, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.addB.setFont(font)
        self.addB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addB.setStyleSheet("color: rgba(148, 33, 146, 230);\n"
        "background-color: rgb(43, 43, 43);\n"
        "border: 2px solid rgba(148, 33, 146, 230);\n"
        "border-radius: 15px;")
        self.addB.setObjectName("addB")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.listWidget = QtWidgets.QListWidget(self.page_3)
        self.listWidget.setGeometry(QtCore.QRect(10, 31, 341, 511))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(19)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("color: rgba(148, 33, 146, 230);\n"
        "background-color: rgb(43, 43, 43);\n"
        "border: 2px solid rgba(148, 33, 146, 230);\n")
        self.listWidget.setObjectName("listWidget")
        self.viewerB_2 = QtWidgets.QPushButton(self.page_3)
        self.viewerB_2.setGeometry(QtCore.QRect(180, 551, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.viewerB_2.setFont(font)
        self.viewerB_2.setStyleSheet("color: rgba(148, 33, 146, 230);\n"
        "background-color: rgb(43, 43, 43);\n"
        "border: 2px solid rgba(148, 33, 146, 230);")
        self.viewerB_2.setObjectName("viewerB_2")
        self.toolsB_2 = QtWidgets.QPushButton(self.page_3)
        self.toolsB_2.setGeometry(QtCore.QRect(1, 551, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.toolsB_2.setFont(font)
        self.toolsB_2.setStyleSheet("color: rgba(148, 33, 146, 230);\n"
        "background-color: rgb(43, 43, 43);\n"
        "border: 2px solid rgba(148, 33, 146, 230);")
        self.toolsB_2.setObjectName("toolsB_2")
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QTimer()
        self.timer.timeout.connect(self.startPage)
        self.timer.start(1500)

        self.toolsB_2.clicked.connect(self.toolF)
        self.viewerB.clicked.connect(self.viewerF)
        self.deleteallB.clicked.connect(self.deleteAllF)
        self.addB.clicked.connect(self.addF)
        self.deleteenteredB.clicked.connect(self.deleteEnteredF)

    def deleteEnteredF(self):
        name = str(self.lineEdit.text())
        if name.replace(" ", "") == "":
            self.resetAll()
        else:
            time = self.timeEdit.time()
            date = self.dateEdit.date()
            day = date.day()
            if len(str(day)) == 1:
                day = f'0{day}'
            month = date.month()
            if len(str(month)) == 1:
                month = f'0{month}'
            hour = time.hour()
            if len(str(hour)) == 1:
                hour = f'0{hour}'
            minute = time.minute()
            if len(str(minute)) == 1:
                minute = f'0{minute}'
            info = f'{name} | {day}.{month}.{date.year()} | {hour}:{minute}'
            DataBase.DELETE(info)
            self.resetAll()

    def deleteAllF(self):
        DataBase.DELETE_ALL()

    def resetAll(self):
        self.lineEdit.setText("")
        self.timeEdit.setTime(QTime(self.now.hour, self.now.minute, 0))
        self.dateEdit.setDate(QDate(self.now.year, self.now.month, self.now.day))

    def addF(self):
        name = str(self.lineEdit.text())
        if name.replace(" ", "") == "":
            self.resetAll()
        else:
            time = self.timeEdit.time()
            date = self.dateEdit.date()
            day = date.day()
            if len(str(day)) == 1:
                day = f'0{day}'
            month = date.month()
            if len(str(month)) == 1:
                month = f'0{month}'
            hour = time.hour()
            if len(str(hour)) == 1:
                hour = f'0{hour}'
            minute = time.minute()
            if len(str(minute)) == 1:
                minute = f'0{minute}'
            info = f'{name} | {day}.{month}.{date.year()} | {hour}:{minute}'
            DataBase.ADD(info)
            self.resetAll()

    def startPage(self):
        self.timer.stop()
        self.stackedWidget.setCurrentIndex(1)

    def toolF(self):
        self.stackedWidget.setCurrentIndex(1)
        self.resetAll()

    def viewerF(self):
        self.listWidget.clear()
        for items in DataBase.VIEW():
            for item in items:
                self.listWidget.addItem(str(item))
        self.stackedWidget.setCurrentIndex(2)
        self.resetAll()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Subscription Reminder"))
        self.label.setText(_translate("MainWindow", "Subscription\n"
        "Reminder"))
        self.toolsB.setText(_translate("MainWindow", "Tools"))
        self.viewerB.setText(_translate("MainWindow", "Viewer"))
        self.label2.setText(_translate("MainWindow", "Subscription Reminder"))
        self.endtimeL.setText(_translate("MainWindow", "End time:"))
        self.timeEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Subscription End Time</p></body></html>"))
        self.enddateL.setText(_translate("MainWindow", "End date:"))
        self.dateEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Subscription End Date</p></body></html>"))
        self.nameL.setText(_translate("MainWindow", "Name:"))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Subscription Name</p></body></html>"))
        self.deleteallB.setToolTip(_translate("MainWindow", "<html><head/><body><p>Delete Everything</p></body></html>"))
        self.deleteallB.setText(_translate("MainWindow", "Delete All"))
        self.deleteenteredB.setToolTip(_translate("MainWindow", "<html><head/><body><p></p>Delete Everything With Entered Entries</body></html>"))
        self.deleteenteredB.setText(_translate("MainWindow", "Delete Entered"))
        self.addB.setToolTip(_translate("MainWindow", "<html><head/><body><p>Add With Entered Entries</p></body></html>"))
        self.addB.setText(_translate("MainWindow", "Add"))
        self.viewerB_2.setText(_translate("MainWindow", "Viewer"))
        self.toolsB_2.setText(_translate("MainWindow", "Tools"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
