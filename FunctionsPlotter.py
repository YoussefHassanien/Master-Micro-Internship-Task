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
        self.windowIcon = QIcon()
        self.windowIcon.addPixmap('./Assets/wave-graph.png')
        App.setWindowIcon(self.windowIcon)
        self.gridLayout = QGridLayout(App)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.titleLabel = QLabel(App)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.titleLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.plottingGraph = MplWidget(App)
        self.plottingGraph.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.plottingGraph.setObjectName(u"plottingGraph")

        self.horizontalLayout_3.addWidget(self.plottingGraph)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.functionOneLabel = QLabel(App)
        self.functionOneLabel.setObjectName(u"functionOneLabel")
        basicFont = QFont()
        basicFont.setPointSize(10)
        basicFont.setBold(True)
        basicFont.setWeight(75)
        errorFont = QFont()
        errorFont.setPointSize(8)
        errorFont.setBold(False)
        errorFont.setWeight(60)
        self.functionOneLabel.setFont(basicFont)

        self.verticalLayout.addWidget(self.functionOneLabel)
        self.functionOneErrorLabel = QLabel(App)
        self.functionOneErrorLabel.setObjectName(u"functionOneLabel")
        self.functionOneErrorLabel.setFont(errorFont)
        self.functionOneErrorLabel.setHidden(True)
        self.functionOneErrorLabel.setStyleSheet('color: rgb(155,0,0)')
        self.verticalLayout.addWidget(self.functionOneErrorLabel)
        self.functionOneTextEdit = QTextEdit(App)
        self.functionOneTextEdit.setMaximumWidth(800)
        self.functionOneTextEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.functionOneTextEdit.setObjectName(u"functionOneTextEdit")
        self.verticalLayout.addWidget(self.functionOneTextEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.functionTwoLabel = QLabel(App)
        self.functionTwoLabel.setObjectName(u"functionTwoLabel")
        self.functionTwoLabel.setFont(basicFont)

        self.verticalLayout_2.addWidget(self.functionTwoLabel)

        self.functionTwoErrorLabel = QLabel(App)
        self.functionTwoErrorLabel.setObjectName(u"functionOneLabel")
        self.functionTwoErrorLabel.setFont(errorFont)
        self.functionTwoErrorLabel.setHidden(True)
        self.functionTwoErrorLabel.setStyleSheet('color: rgb(155,0,0)')
        self.verticalLayout_2.addWidget(self.functionTwoErrorLabel)

        self.functionTwoTextEdit = QTextEdit(App)
        self.functionTwoTextEdit.setMaximumWidth(800)
        self.functionTwoTextEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.functionTwoTextEdit.setObjectName(u"functionTwoTextEdit")

        self.verticalLayout_2.addWidget(self.functionTwoTextEdit)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.plotButton = QPushButton(App)
        self.plotButton.setObjectName(u"plotButton")
        self.plotButton.setFont(basicFont)
        self.plotButtonIcon = QIcon()
        self.plotButtonIcon.addPixmap('./Assets/drawing.png')
        self.plotButton.setIcon(self.plotButtonIcon)
        self.verticalLayout_3.addWidget(self.plotButton)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(self.verticalSpacer_4)
        self.solutionLabel = QLabel(App)
        self.solutionLabel.setObjectName(u"solutionLabel")
        self.solutionLabel.setFont(basicFont)
        self.solutionLabel.setStyleSheet('color: rgb(0,155,0)')
        self.solutionLabel.setHidden(True)

        self.verticalLayout_5.addWidget(self.solutionLabel)


        self.verticalLayout_3.addLayout(self.verticalLayout_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)


        self.retranslateUi(App)

        QMetaObject.connectSlotsByName(App)
    # setupUi

    def retranslateUi(self, App):
        App.setWindowTitle(QCoreApplication.translate("App", u"Functions Plotter", None))
        self.titleLabel.setText(QCoreApplication.translate("App", u"Functions Plotter", None))
        self.functionOneLabel.setText(QCoreApplication.translate("App", u"Function 1", None))
        self.functionTwoLabel.setText(QCoreApplication.translate("App", u"Function 2", None))
        self.solutionLabel.setText(QCoreApplication.translate("App", u"Solution", None))
        self.plotButton.setText(QCoreApplication.translate("App", u"Plot", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    FunctionsPlotter = QWidget()
    ui = Ui_App()
    ui.setupUi(FunctionsPlotter)
    FunctionsPlotter.show()
    sys.exit(app.exec_())
