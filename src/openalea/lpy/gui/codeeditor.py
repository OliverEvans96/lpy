# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'codeeditor.ui'
#
# Created: Fri Jul 25 16:50:47 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CodeEditor(object):
    def setupUi(self, CodeEditor):
        CodeEditor.setObjectName("CodeEditor")
        CodeEditor.resize(506,541)
        self.verticalLayout_2 = QtGui.QVBoxLayout(CodeEditor)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filenames = QTabBar(CodeEditor)
        self.filenames.setObjectName("filenames")
        self.verticalLayout.addWidget(self.filenames)
        self.codeeditor = LpyCodeEditor(CodeEditor)
        self.codeeditor.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.codeeditor.setFont(font)
        self.codeeditor.setTabStopWidth(20)
        self.codeeditor.setObjectName("codeeditor")
        self.verticalLayout.addWidget(self.codeeditor)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.frameFind = QtGui.QFrame(CodeEditor)
        self.frameFind.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameFind.setFrameShadow(QtGui.QFrame.Raised)
        self.frameFind.setObjectName("frameFind")
        self.gridLayout = QtGui.QGridLayout(self.frameFind)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.findNextButton = QtGui.QPushButton(self.frameFind)
        self.findNextButton.setObjectName("findNextButton")
        self.gridLayout.addWidget(self.findNextButton,0,3,1,1)
        self.closeFind = QtGui.QToolButton(self.frameFind)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.ButtonText,brush)
        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.ButtonText,brush)
        brush = QtGui.QBrush(QtGui.QColor(118,116,108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.ButtonText,brush)
        self.closeFind.setPalette(palette)
        self.closeFind.setObjectName("closeFind")
        self.gridLayout.addWidget(self.closeFind,0,0,1,1)
        self.label_8 = QtGui.QLabel(self.frameFind)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8,0,1,1,1)
        self.wholeWordButton = QtGui.QRadioButton(self.frameFind)
        self.wholeWordButton.setAutoExclusive(False)
        self.wholeWordButton.setObjectName("wholeWordButton")
        self.gridLayout.addWidget(self.wholeWordButton,1,4,1,1)
        self.matchCaseButton = QtGui.QRadioButton(self.frameFind)
        self.matchCaseButton.setAutoExclusive(False)
        self.matchCaseButton.setObjectName("matchCaseButton")
        self.gridLayout.addWidget(self.matchCaseButton,1,3,1,1)
        spacerItem = QtGui.QSpacerItem(61,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem,0,5,1,1)
        self.replaceEdit = QtGui.QLineEdit(self.frameFind)
        self.replaceEdit.setObjectName("replaceEdit")
        self.gridLayout.addWidget(self.replaceEdit,0,2,1,1)
        spacerItem1 = QtGui.QSpacerItem(177,17,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1,1,0,1,3)
        self.findPreviousButton = QtGui.QPushButton(self.frameFind)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.findPreviousButton.sizePolicy().hasHeightForWidth())
        self.findPreviousButton.setSizePolicy(sizePolicy)
        self.findPreviousButton.setObjectName("findPreviousButton")
        self.gridLayout.addWidget(self.findPreviousButton,0,4,1,1)
        spacerItem2 = QtGui.QSpacerItem(61,17,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2,1,5,1,1)
        self.verticalLayout_2.addWidget(self.frameFind)
        self.frameReplace = QtGui.QFrame(CodeEditor)
        self.frameReplace.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameReplace.setFrameShadow(QtGui.QFrame.Raised)
        self.frameReplace.setObjectName("frameReplace")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frameReplace)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_9 = QtGui.QLabel(self.frameReplace)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.findEdit = QtGui.QLineEdit(self.frameReplace)
        self.findEdit.setObjectName("findEdit")
        self.horizontalLayout.addWidget(self.findEdit)
        self.replaceButton = QtGui.QPushButton(self.frameReplace)
        self.replaceButton.setObjectName("replaceButton")
        self.horizontalLayout.addWidget(self.replaceButton)
        self.replaceAllButton = QtGui.QPushButton(self.frameReplace)
        self.replaceAllButton.setObjectName("replaceAllButton")
        self.horizontalLayout.addWidget(self.replaceAllButton)
        spacerItem3 = QtGui.QSpacerItem(142,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.frameReplace)

        self.retranslateUi(CodeEditor)
        QtCore.QObject.connect(self.closeFind,QtCore.SIGNAL("pressed()"),self.frameFind.hide)
        QtCore.QObject.connect(self.closeFind,QtCore.SIGNAL("pressed()"),self.frameReplace.hide)
        QtCore.QMetaObject.connectSlotsByName(CodeEditor)

    def retranslateUi(self, CodeEditor):
        CodeEditor.setWindowTitle(QtGui.QApplication.translate("CodeEditor", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.findNextButton.setText(QtGui.QApplication.translate("CodeEditor", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.closeFind.setText(QtGui.QApplication.translate("CodeEditor", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("CodeEditor", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.wholeWordButton.setText(QtGui.QApplication.translate("CodeEditor", "Whole word", None, QtGui.QApplication.UnicodeUTF8))
        self.matchCaseButton.setText(QtGui.QApplication.translate("CodeEditor", "Match Case", None, QtGui.QApplication.UnicodeUTF8))
        self.findPreviousButton.setText(QtGui.QApplication.translate("CodeEditor", "Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("CodeEditor", "Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceButton.setText(QtGui.QApplication.translate("CodeEditor", "Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceAllButton.setText(QtGui.QApplication.translate("CodeEditor", "Rep. All", None, QtGui.QApplication.UnicodeUTF8))

from lpycodeeditor import LpyCodeEditor
from PyQt4.QtGui import QTabBar