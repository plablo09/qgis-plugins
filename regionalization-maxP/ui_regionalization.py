# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_regionalization.ui'
#
# Created: Mon Mar  3 18:45:36 2014
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

class Ui_Regionalization(object):
    def setupUi(self, Regionalization):
        Regionalization.setObjectName(_fromUtf8("Regionalization"))
        Regionalization.resize(643, 320)
        self.buttonBox = QtGui.QDialogButtonBox(Regionalization)
        self.buttonBox.setGeometry(QtCore.QRect(270, 270, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.listWidget = QtGui.QListWidget(Regionalization)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 401, 271))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))

        self.retranslateUi(Regionalization)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Regionalization.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Regionalization.reject)
        QtCore.QMetaObject.connectSlotsByName(Regionalization)

    def retranslateUi(self, Regionalization):
        Regionalization.setWindowTitle(_translate("Regionalization", "Regionalization", None))

