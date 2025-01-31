# mplwidget.py

from PySide2.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas,  NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class MplWidget(QWidget):
    def __init__(self, parent=None):
        super(MplWidget, self).__init__(parent)
        self.canvas = FigureCanvas(Figure())
        self.toolbar = NavigationToolbar(self.canvas, self)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        vertical_layout.addWidget(self.toolbar)
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.set_xlabel('X-Axis', labelpad=8, fontweight='bold')  
        self.canvas.axes.set_ylabel('Y-Axis', labelpad=8, fontweight='bold') 
        self.setLayout(vertical_layout)