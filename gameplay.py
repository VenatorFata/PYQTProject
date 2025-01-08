# Form implementation generated from reading ui file 'gameplay.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(876, 568)
        self.progressBar = QtWidgets.QProgressBar(parent=Form)
        self.progressBar.setGeometry(QtCore.QRect(50, 20, 771, 61))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.fluidRefillButton = QtWidgets.QPushButton(parent=Form)
        self.fluidRefillButton.setGeometry(QtCore.QRect(650, 310, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setBold(True)
        font.setWeight(75)
        self.fluidRefillButton.setFont(font)
        self.fluidRefillButton.setObjectName("fluidRefillButton")
        self.RPMbox = QtWidgets.QSpinBox(parent=Form)
        self.RPMbox.setGeometry(QtCore.QRect(420, 240, 141, 131))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.RPMbox.setFont(font)
        self.RPMbox.setMinimum(20)
        self.RPMbox.setMaximum(120)
        self.RPMbox.setSingleStep(5)
        self.RPMbox.setProperty("value", 20)
        self.RPMbox.setObjectName("RPMbox")
        self.comboDrillHead = QtWidgets.QComboBox(parent=Form)
        self.comboDrillHead.setGeometry(QtCore.QRect(120, 320, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboDrillHead.setFont(font)
        self.comboDrillHead.setObjectName("comboDrillHead")
        self.comboDrillHead.addItem("")
        self.comboDrillHead.addItem("")
        self.comboDrillHead.addItem("")
        self.changeDrillHead = QtWidgets.QPushButton(parent=Form)
        self.changeDrillHead.setGeometry(QtCore.QRect(40, 280, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(10)
        self.changeDrillHead.setFont(font)
        self.changeDrillHead.setObjectName("changeDrillHead")
        self.timeLCD = QtWidgets.QLCDNumber(parent=Form)
        self.timeLCD.setGeometry(QtCore.QRect(783, 470, 81, 81))
        self.timeLCD.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.timeLCD.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.timeLCD.setObjectName("timeLCD")
        self.endButton = QtWidgets.QPushButton(parent=Form)
        self.endButton.setGeometry(QtCore.QRect(350, 500, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(12)
        self.endButton.setFont(font)
        self.endButton.setObjectName("endButton")
        self.acceptDrillHead = QtWidgets.QPushButton(parent=Form)
        self.acceptDrillHead.setEnabled(False)
        self.acceptDrillHead.setGeometry(QtCore.QRect(40, 320, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(10)
        self.acceptDrillHead.setFont(font)
        self.acceptDrillHead.setObjectName("acceptDrillHead")
        self.startButton = QtWidgets.QPushButton(parent=Form)
        self.startButton.setGeometry(QtCore.QRect(350, 440, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(12)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.heavyStatus = QtWidgets.QProgressBar(parent=Form)
        self.heavyStatus.setGeometry(QtCore.QRect(200, 240, 81, 31))
        self.heavyStatus.setMaximum(30)
        self.heavyStatus.setProperty("value", 0)
        self.heavyStatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.heavyStatus.setTextVisible(False)
        self.heavyStatus.setObjectName("heavyStatus")
        self.heavyRepair = QtWidgets.QPushButton(parent=Form)
        self.heavyRepair.setGeometry(QtCore.QRect(290, 240, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(8)
        self.heavyRepair.setFont(font)
        self.heavyRepair.setObjectName("heavyRepair")
        self.repairButtonGroup = QtWidgets.QButtonGroup(Form)
        self.repairButtonGroup.setObjectName("repairButtonGroup")
        self.repairButtonGroup.addButton(self.heavyRepair)
        self.heavyLabel = QtWidgets.QLabel(parent=Form)
        self.heavyLabel.setGeometry(QtCore.QRect(180, 240, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(12)
        self.heavyLabel.setFont(font)
        self.heavyLabel.setObjectName("heavyLabel")
        self.mediumLabel = QtWidgets.QLabel(parent=Form)
        self.mediumLabel.setGeometry(QtCore.QRect(180, 290, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(12)
        self.mediumLabel.setFont(font)
        self.mediumLabel.setObjectName("mediumLabel")
        self.lightLabel = QtWidgets.QLabel(parent=Form)
        self.lightLabel.setGeometry(QtCore.QRect(180, 340, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(12)
        self.lightLabel.setFont(font)
        self.lightLabel.setObjectName("lightLabel")
        self.mediumStatus = QtWidgets.QProgressBar(parent=Form)
        self.mediumStatus.setGeometry(QtCore.QRect(200, 290, 81, 31))
        self.mediumStatus.setMaximum(20)
        self.mediumStatus.setProperty("value", 0)
        self.mediumStatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mediumStatus.setTextVisible(False)
        self.mediumStatus.setObjectName("mediumStatus")
        self.lightStatus = QtWidgets.QProgressBar(parent=Form)
        self.lightStatus.setGeometry(QtCore.QRect(200, 340, 81, 31))
        self.lightStatus.setMaximum(10)
        self.lightStatus.setProperty("value", 0)
        self.lightStatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lightStatus.setTextVisible(False)
        self.lightStatus.setObjectName("lightStatus")
        self.mediumRepair = QtWidgets.QPushButton(parent=Form)
        self.mediumRepair.setGeometry(QtCore.QRect(290, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(8)
        self.mediumRepair.setFont(font)
        self.mediumRepair.setObjectName("mediumRepair")
        self.repairButtonGroup.addButton(self.mediumRepair)
        self.lightRepair = QtWidgets.QPushButton(parent=Form)
        self.lightRepair.setGeometry(QtCore.QRect(290, 340, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(8)
        self.lightRepair.setFont(font)
        self.lightRepair.setObjectName("lightRepair")
        self.repairButtonGroup.addButton(self.lightRepair)
        self.timeLabel = QtWidgets.QLabel(parent=Form)
        self.timeLabel.setGeometry(QtCore.QRect(610, 480, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(12)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")
        self.drillLabel = QtWidgets.QLabel(parent=Form)
        self.drillLabel.setGeometry(QtCore.QRect(40, 180, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(10)
        self.drillLabel.setFont(font)
        self.drillLabel.setObjectName("drillLabel")
        self.drillLabel_3 = QtWidgets.QLabel(parent=Form)
        self.drillLabel_3.setGeometry(QtCore.QRect(350, 180, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(10)
        self.drillLabel_3.setFont(font)
        self.drillLabel_3.setObjectName("drillLabel_3")
        self.drillLabel_4 = QtWidgets.QLabel(parent=Form)
        self.drillLabel_4.setGeometry(QtCore.QRect(630, 220, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(10)
        self.drillLabel_4.setFont(font)
        self.drillLabel_4.setObjectName("drillLabel_4")
        self.tasksLabel = QtWidgets.QLabel(parent=Form)
        self.tasksLabel.setGeometry(QtCore.QRect(10, 500, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(12)
        self.tasksLabel.setFont(font)
        self.tasksLabel.setObjectName("tasksLabel")
        self.depthLabel = QtWidgets.QLabel(parent=Form)
        self.depthLabel.setGeometry(QtCore.QRect(10, 530, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(10)
        self.depthLabel.setFont(font)
        self.depthLabel.setObjectName("depthLabel")
        self.drillLabel_2 = QtWidgets.QLabel(parent=Form)
        self.drillLabel_2.setGeometry(QtCore.QRect(40, 200, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(10)
        self.drillLabel_2.setFont(font)
        self.drillLabel_2.setObjectName("drillLabel_2")
        self.fluidBar = QtWidgets.QProgressBar(parent=Form)
        self.fluidBar.setGeometry(QtCore.QRect(630, 270, 181, 23))
        self.fluidBar.setMaximum(20)
        self.fluidBar.setProperty("value", 0)
        self.fluidBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fluidBar.setTextVisible(False)
        self.fluidBar.setObjectName("fluidBar")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(500, 90, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fluidRefillButton.setText(_translate("Form", "Запрос бур. жидкости"))
        self.comboDrillHead.setItemText(0, _translate("Form", "Т"))
        self.comboDrillHead.setItemText(1, _translate("Form", "С"))
        self.comboDrillHead.setItemText(2, _translate("Form", "М"))
        self.changeDrillHead.setText(_translate("Form", "Сменить долото"))
        self.endButton.setText(_translate("Form", "Завершить бурение"))
        self.acceptDrillHead.setText(_translate("Form", "Выбрать"))
        self.startButton.setText(_translate("Form", "Начать бурение"))
        self.heavyRepair.setText(_translate("Form", "Починить долото"))
        self.heavyLabel.setText(_translate("Form", "Т"))
        self.mediumLabel.setText(_translate("Form", "С"))
        self.lightLabel.setText(_translate("Form", "М"))
        self.mediumRepair.setText(_translate("Form", "Починить долото"))
        self.lightRepair.setText(_translate("Form", "Починить долото"))
        self.timeLabel.setText(_translate("Form", "Времени осталось:"))
        self.drillLabel.setText(_translate("Form", "Требуемое долото:"))
        self.drillLabel_3.setText(_translate("Form", "Требуемое кол-во Об/мин:"))
        self.drillLabel_4.setText(_translate("Form", "Осталось бур. жидкости:"))
        self.tasksLabel.setText(_translate("Form", "Задача"))
        self.depthLabel.setText(_translate("Form", "Требуемая глубина -"))
        self.drillLabel_2.setText(_translate("Form", "Текущее долото:"))
        self.label.setText(_translate("Form", "Работник:"))
