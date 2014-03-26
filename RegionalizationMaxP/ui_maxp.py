# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_maxp.ui'
#
# Created: Tue Mar 25 09:33:45 2014
#      by: PyQt4 UI code generator 4.10
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

class Ui_MaxP(object):
    def setupUi(self, MaxP):
        MaxP.setObjectName(_fromUtf8("MaxP"))
        MaxP.resize(584, 282)
        self.buttonBox = QtGui.QDialogButtonBox(MaxP)
        self.buttonBox.setGeometry(QtCore.QRect(-110, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.listWidget = QtGui.QListWidget(MaxP)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 271, 221))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.textFloor = QtGui.QPlainTextEdit(MaxP)
        self.textFloor.setGeometry(QtCore.QRect(410, 40, 61, 31))
        self.textFloor.setObjectName(_fromUtf8("textFloor"))
        self.textSeed = QtGui.QTextEdit(MaxP)
        self.textSeed.setGeometry(QtCore.QRect(410, 90, 61, 31))
        self.textSeed.setObjectName(_fromUtf8("textSeed"))
        self.label = QtGui.QLabel(MaxP)
        self.label.setGeometry(QtCore.QRect(330, 50, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(MaxP)
        self.label_2.setGeometry(QtCore.QRect(330, 100, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(MaxP)
        self.label_3.setGeometry(QtCore.QRect(360, 10, 101, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.queenButton = QtGui.QRadioButton(MaxP)
        self.queenButton.setGeometry(QtCore.QRect(330, 170, 116, 22))
        self.queenButton.setObjectName(_fromUtf8("queenButton"))
        self.buttonGroup = QtGui.QButtonGroup(MaxP)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.queenButton)
        self.rookButton = QtGui.QRadioButton(MaxP)
        self.rookButton.setGeometry(QtCore.QRect(330, 200, 116, 22))
        self.rookButton.setObjectName(_fromUtf8("rookButton"))
        self.buttonGroup.addButton(self.rookButton)
        self.label_4 = QtGui.QLabel(MaxP)
        self.label_4.setGeometry(QtCore.QRect(360, 140, 111, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(MaxP)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MaxP.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MaxP.reject)
        QtCore.QMetaObject.connectSlotsByName(MaxP)

    def retranslateUi(self, MaxP):
        MaxP.setWindowTitle(_translate("MaxP", "MaxP", None))
        self.label.setText(_translate("MaxP", "Floor", None))
        self.label_2.setText(_translate("MaxP", "Seed", None))
        self.label_3.setText(_translate("MaxP", "Parámetros ", None))
        self.queenButton.setText(_translate("MaxP", "Queen", None))
        self.rookButton.setText(_translate("MaxP", "Rook", None))
        self.label_4.setText(_translate("MaxP", "Tipo de vecindad", None))

