# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FlashingTool_Gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(394, 222)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(3, 30, 71, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pathText = QtWidgets.QLineEdit(Form)
        self.pathText.setGeometry(QtCore.QRect(70, 30, 251, 22))
        self.pathText.setObjectName("pathText")
        self.loadButton = QtWidgets.QPushButton(Form)
        self.loadButton.setGeometry(QtCore.QRect(330, 30, 61, 22))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.loadButton.setFont(font)
        self.loadButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.loadButton.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/elProf/Downloads/kisspng-share-icon-computer-icons-button-safari-web-browse-5b3c192a5d6439.0981811715306652583826.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loadButton.setIcon(icon)
        self.loadButton.setIconSize(QtCore.QSize(20, 30))
        self.loadButton.setObjectName("loadButton")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(10, 180, 281, 23))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setBold(False)
        font.setWeight(50)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.startButton = QtWidgets.QPushButton(Form)
        self.startButton.setGeometry(QtCore.QRect(10, 140, 121, 28))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/elProf/Downloads/kisspng-download-computer-icons-clip-art-download-now-button-5abd36f12a8215.5317571915223498091741.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startButton.setIcon(icon1)
        self.startButton.setObjectName("startButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(3, 80, 71, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comPortText = QtWidgets.QLineEdit(Form)
        self.comPortText.setGeometry(QtCore.QRect(70, 80, 91, 25))
        self.comPortText.setObjectName("comPortText")
        self.detectButton = QtWidgets.QPushButton(Form)
        self.detectButton.setGeometry(QtCore.QRect(170, 80, 71, 25))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.detectButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/elProf/Downloads/kisspng-computer-icons-magnifying-glass-desktop-wallpaper-web-5ac77f7c4d23f6.050912181523023740316.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.detectButton.setIcon(icon2)
        self.detectButton.setObjectName("detectButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "HEX FILE"))
        self.pathText.setText(_translate("Form", "BLD_App.hex"))
        self.loadButton.setText(_translate("Form", "Load"))
        self.startButton.setText(_translate("Form", "Start Flashing"))
        self.label_2.setText(_translate("Form", "COM PORT"))
        self.comPortText.setText(_translate("Form", "COM7"))
        self.detectButton.setText(_translate("Form", "Detect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
