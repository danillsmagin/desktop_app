import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPen, QPainter
import pyqtgraph as pg
from ecg_gui import Ui_MainWindow
import db_patient  # in future will be database
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

        self.graphWidget = pg.PlotWidget()
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 36, 46]

        pen = pg.mkPen(color=(255, 0, 0))
        self.graphWidget = self.ui.graphicsView.plot(hour, temperature, pen=pen)

        self.ui.graphicsView.setBackground('white')
        self.ui.graphicsView.setTitle('ECG graph(no)', color='black', size='19pt')
        style = {'color': 'red',
                 'font-size': '16pt'}
        self.ui.graphicsView.setLabel('left', 'влэл', **style)
        self.ui.graphicsView.setLabel('bottom', 'sus', **style)

    def init_ui(self):
        self.setWindowTitle('Калькулятор пульса по ЭКГ')
        self.setWindowIcon(QIcon('static\icon_pulse.png'))

        self.ui.dist_between_teeth.setPlaceholderText('ДА ДАВАЙ БЛЯТЬ')
        self.ui.ecg_removal_rate.setPlaceholderText('влэд')

        self.ui.btn_calc_pulse.clicked.connect(self.pulse_calculation)

    def pulse_calculation(self):
        dist_between_teeth = int(self.ui.dist_between_teeth.text())
        ecg_removal_rate = int(self.ui.ecg_removal_rate.text())

        pulse_result = 60 / (dist_between_teeth - ecg_removal_rate)

        self.ui.pulse.setText(str(round(pulse_result, 2)))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
