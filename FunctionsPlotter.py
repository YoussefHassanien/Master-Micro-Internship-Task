from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import numpy as np
from mplwidget import MplWidget
from scipy.optimize import brentq

class Ui_App(object):
    def setupUi(self, App):
        if not App.objectName():
            App.setObjectName(u"App")
        self.windowIcon = QIcon()
        self.windowIcon.addPixmap('./Assets/wave-graph.png')
        
        App.resize(725, 559)
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
        self.plottingGraph.setMinimumWidth(500)
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
        self.functionOneLabel.setFont(basicFont)
        self.verticalLayout.addWidget(self.functionOneLabel)

        self.functionOneErrorLabel = QLabel(App)
        self.functionOneErrorLabel.setObjectName(u"functionOneErrorLabel")
        errorFont = QFont()
        errorFont.setPointSize(8)
        errorFont.setBold(False)
        self.functionOneErrorLabel.setFont(errorFont)
        self.functionOneErrorLabel.setStyleSheet('color: rgb(155, 0, 0)')
        self.functionOneErrorLabel.setHidden(True)
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
        self.functionTwoErrorLabel.setObjectName(u"functionTwoErrorLabel")
        self.functionTwoErrorLabel.setFont(errorFont)
        self.functionTwoErrorLabel.setStyleSheet('color: rgb(155, 0, 0)')
        self.functionTwoErrorLabel.setHidden(True)
        self.verticalLayout_2.addWidget(self.functionTwoErrorLabel)

        self.functionTwoTextEdit = QTextEdit(App)
        self.functionTwoTextEdit.setMaximumWidth(800)
        self.functionTwoTextEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.functionTwoTextEdit.setObjectName(u"functionTwoTextEdit")
        self.verticalLayout_2.addWidget(self.functionTwoTextEdit)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(self.verticalSpacer_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.plotButton = QPushButton(App, clicked = lambda: self.plotFunctions())
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
        self.solutionLabel.setHidden(True)
        self.verticalLayout_5.addWidget(self.solutionLabel)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(App)
        QMetaObject.connectSlotsByName(App)

    def retranslateUi(self, App):
        App.setWindowTitle(QCoreApplication.translate("App", u"Functions Plotter", None))
        self.titleLabel.setText(QCoreApplication.translate("App", u"Functions Plotter", None))
        self.functionOneLabel.setText(QCoreApplication.translate("App", u"Function 1", None))
        self.functionTwoLabel.setText(QCoreApplication.translate("App", u"Function 2", None))
        self.plotButton.setText(QCoreApplication.translate("App", u"Plot", None))
        self.solutionLabel.setText(QCoreApplication.translate("App", u"Solution", None))

    def plotFunctions(self):
            self.plottingGraph.canvas.axes.clear()
            self.plottingGraph.canvas.axes.set_xlabel('X-Axis', labelpad=8, fontweight='bold')  
            self.plottingGraph.canvas.axes.set_ylabel('Y-Axis', labelpad=8, fontweight='bold') 
            self.solutionLabel.setHidden(True)
            x = np.linspace(-10, 10, 1000)
            env = {
                'log10': np.log10,
                'sqrt': np.sqrt,
                'x': x
            }
            func1_valid, y1 = self.validate_function(self.functionOneTextEdit, self.functionOneErrorLabel, env)
            func2_valid, y2 = self.validate_function(self.functionTwoTextEdit, self.functionTwoErrorLabel, env)

            if func1_valid and func2_valid:
                self.plottingGraph.canvas.axes.plot(x, y1, label='Function 1', color='blue')
                self.plottingGraph.canvas.axes.plot(x, y2, label='Function 2', color='green')
                
                self.plottingGraph.canvas.axes.legend()
                
                roots = self.find_roots(x, y1, y2)
                if roots.size > 0:
                    solutions = []
                    for root in roots:
                        y_val = np.interp(root, x, y1)
                        solutions.append(f'({root:.2f}, {y_val:.2f})')
                        self.plottingGraph.canvas.axes.plot(root, y_val, 'ro')
                    self.solutionLabel.setText(f"Solutions found at: {', '.join(solutions)}")
                    self.solutionLabel.setStyleSheet("color: green")
                else:
                    self.solutionLabel.setText("No solutions found.")
                    self.solutionLabel.setStyleSheet("color: red")
                
                self.solutionLabel.setHidden(False)
                self.plottingGraph.canvas.draw()



    def validate_function(self, text_edit, error_label, env):
        func_text = text_edit.toPlainText().strip().replace('^', '**')
        error_label.setHidden(True)
        text_edit.setStyleSheet("")
        
        if not func_text:
            error_label.setText("Function cannot be empty.")
            error_label.setHidden(False)
            text_edit.setStyleSheet("background-color: #ffcccc;")
            return False, None
        
        try:
            y = eval(func_text, env)

            if not isinstance(y, np.ndarray) or len(y) != len(env['x']):
                raise ValueError("Function must return an array of the same length as x.")
            if np.any(np.isinf(y)):
                raise ZeroDivisionError("Division by zero in the function.")      
            if np.any(np.isnan(y)):
                raise ValueError("Math domain error (e.g., square root of a negative number or log10 of a negative number).")    
            return True, y
        
        except Exception as e:
            if isinstance(e, NameError):
                name = str(e).split("'")[1]
                error_msg = f"Undefined name '{name}'. Allowed variables: x. Allowed functions: log10(), sqrt()."
            elif isinstance(e, SyntaxError):
                error_msg = "Syntax error in function. Check for missing operators (e.g., *, ^, +, ...), parentheses or x."
            elif isinstance(e, ZeroDivisionError) or (isinstance(e, ValueError) and "division by zero" in str(e)):
                error_msg = "Division by zero in the function."
            elif isinstance(e, ValueError) and "math domain error" in str(e).lower():
                error_msg = "Math domain error (e.g., square root of a negative number or log10 of a negative number)."
            else:
                error_msg = "An error occurred. Please check your function's syntax and variables."
            
            error_label.setText(error_msg)
            error_label.setHidden(False)
            text_edit.setStyleSheet("background-color: #ffcccc;")
            return False, None

    def find_roots(self, x, y1, y2):
        y_diff = y1 - y2
        roots = []
        sign_changes = np.where(np.diff(np.sign(y_diff)))[0]

        for idx in sign_changes:
            x_low, x_high = x[idx], x[idx + 1]
            try:
                root = brentq(lambda t: np.interp(t, x, y1) - np.interp(t, x, y2), x_low, x_high)
                roots.append(root)
            except ValueError:
                continue 

        roots.extend(x[np.abs(y_diff) < 1e-9])
        return np.unique(np.round(roots, decimals=6))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    App = QWidget()
    ui = Ui_App()
    ui.setupUi(App)
    App.show()
    sys.exit(app.exec_())