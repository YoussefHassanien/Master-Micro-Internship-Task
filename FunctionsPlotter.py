# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'App.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from mplwidget import MplWidget


class Ui_App(object):
    def setupUi(self, App):
        if not App.objectName():
            App.setObjectName(u"App")
        App.resize(725, 559)
        self.gridLayout = QGridLayout(App)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(App)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.graphicsView = MplWidget(App)
        self.graphicsView.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout_3.addWidget(self.graphicsView)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(App)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.textEdit = QTextEdit(App)
        self.textEdit.setMaximumWidth(800)
        self.textEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(App)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.textEdit_2 = QTextEdit(App)
        self.textEdit_2.setMaximumWidth(800)
        self.textEdit_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.verticalLayout_2.addWidget(self.textEdit_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.pushButton = QPushButton(App)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)

        self.verticalLayout_3.addWidget(self.pushButton)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(self.verticalSpacer_4)
        self.label_4 = QLabel(App)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setHidden(True)

        self.verticalLayout_5.addWidget(self.label_4)

        self.textEdit_3 = QTextEdit(App)
        self.textEdit_3.setMaximumWidth(800)
        self.textEdit_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.textEdit_3.setObjectName(u"textEdit_2")
        self.textEdit_3.setDisabled(True)
        self.textEdit_3.setHidden(True)

        self.verticalLayout_5.addWidget(self.textEdit_3)



        self.verticalLayout_3.addLayout(self.verticalLayout_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)


        self.retranslateUi(App)

        QMetaObject.connectSlotsByName(App)
    # setupUi

    def retranslateUi(self, App):
        App.setWindowTitle(QCoreApplication.translate("App", u"Form", None))
        self.label.setText(QCoreApplication.translate("App", u"Functions Plotter", None))
        self.label_2.setText(QCoreApplication.translate("App", u"Function 1", None))
        self.label_3.setText(QCoreApplication.translate("App", u"Function 2", None))
        self.label_4.setText(QCoreApplication.translate("App", u"Solution", None))
        self.pushButton.setText(QCoreApplication.translate("App", u"Plot", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    FunctionsPlotter = QWidget()
    ui = Ui_App()
    ui.setupUi(FunctionsPlotter)
    FunctionsPlotter.show()
    sys.exit(app.exec_())
