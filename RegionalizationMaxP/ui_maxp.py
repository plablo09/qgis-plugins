# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_maxp.ui'
#
# Created: Tue Mar  4 11:18:20 2014
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
        self.textFloor.setGeometry(QtCore.QRect(400, 40, 151, 41))
        self.textFloor.setObjectName(_fromUtf8("textFloor"))
        self.textSeed = QtGui.QTextEdit(MaxP)
        self.textSeed.setGeometry(QtCore.QRect(400, 130, 141, 41))
        self.textSeed.setObjectName(_fromUtf8("textSeed"))
        self.label = QtGui.QLabel(MaxP)
        self.label.setGeometry(QtCore.QRect(320, 50, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(MaxP)
        self.label_2.setGeometry(QtCore.QRect(320, 140, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(MaxP)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MaxP.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MaxP.reject)
        QtCore.QMetaObject.connectSlotsByName(MaxP)

    def retranslateUi(self, MaxP):
        MaxP.setWindowTitle(_translate("MaxP", "MaxP", None))
        self.label.setText(_translate("MaxP", "Floor", None))
        self.label_2.setText(_translate("MaxP", "Seed", None))

