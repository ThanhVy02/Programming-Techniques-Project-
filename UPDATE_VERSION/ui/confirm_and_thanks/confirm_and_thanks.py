# Form implementation generated from reading ui file 'D:\K24406H\PROJECT\ui\confirm_and_thanks\confirm_and_thanks.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(396, 311)
        Dialog.setWindowTitle("")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 401, 311))
        self.label.setStyleSheet("background-color: rgb(120, 99, 84);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setGeometry(QtCore.QRect(80, 10, 231, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("color: rgb(237, 236, 232);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(parent=Dialog)
        self.frame_2.setGeometry(QtCore.QRect(0, -1, 71, 311))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(parent=Dialog)
        self.frame_3.setGeometry(QtCore.QRect(330, 0, 71, 311))
        font = QtGui.QFont()
        font.setFamily("Niagara Solid")
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(parent=Dialog)
        self.frame_4.setGeometry(QtCore.QRect(160, 90, 171, 181))
        self.frame_4.setStyleSheet("background-color: rgb(78, 34, 28);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(parent=Dialog)
        self.frame_5.setGeometry(QtCore.QRect(90, 70, 211, 181))
        self.frame_5.setStyleSheet("background-color: rgb(204, 185, 178);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.pushButtonHome = QtWidgets.QPushButton(parent=self.frame_5)
        self.pushButtonHome.setGeometry(QtCore.QRect(60, 80, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButtonHome.setFont(font)
        self.pushButtonHome.setStyleSheet("QPushButton {\n"
"    background-color: #e8e7e6;\n"
"    color: #737373; \n"
"    border: none;\n"
"    border-radius: 8px; \n"
"    padding: 5px 20px; \n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c2c0bd;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #918d88; \n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\K24406H\\PROJECT\\ui\\confirm_and_thanks\\../images/image(3).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonHome.setIcon(icon)
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.pushButtonExit = QtWidgets.QPushButton(parent=self.frame_5)
        self.pushButtonExit.setGeometry(QtCore.QRect(60, 120, 91, 21))
        self.pushButtonExit.setStyleSheet("QPushButton {\n"
"    font: 12pt \"NSimSun\";\n"
"    background-color: #e8e7e6;\n"
"    color: #737373; \n"
"    border: none;\n"
"    border-radius: 8px; \n"
"    padding: 5px 20px; \n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c2c0bd;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #918d88; \n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\K24406H\\PROJECT\\ui\\confirm_and_thanks\\../images/image(4).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonExit.setIcon(icon1)
        self.pushButtonExit.setObjectName("pushButtonExit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("Dialog", "ETERNA LUXE"))
        self.label_2.setText(_translate("Dialog", "THANK YOU FOR BOOKING US."))
        self.pushButtonHome.setText(_translate("Dialog", "HOME"))
        self.pushButtonExit.setText(_translate("Dialog", "EXIT"))
