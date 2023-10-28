import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPen, QPainter
import pyqtgraph as pg
from ecg_gui import Ui_MainWindow
import neurokit2 as nk
import db_patient  # in future will be database


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.generating_ecg = nk.ecg_simulate(duration=7, sampling_rate=2300)
        self.graphWidget = pg.PlotWidget()
        self.init_graph()

    def init_ui(self):
        self.setWindowTitle('Калькулятор пульса по ЭКГ')
        self.setWindowIcon(QIcon('static\icon_pulse.png'))

        self.ui.btn_calc_pulse.clicked.connect(self.ecg_pulse)

    def init_graph(self):
        self.graphWidget = nk.signal_plot(self.generating_ecg, sampling_rate=2300)

        self.ui.graphicsView.setBackground('white')
        self.ui.graphicsView.setTitle('ECG graph(no)', color='black', size='19pt')
        style = {'color': 'red',
                 'font-size': '16pt'}
        self.ui.graphicsView.setLabel('left', 'влэл', **style)
        self.ui.graphicsView.setLabel('bottom', 'sus', **style)
        pen = pg.mkPen(color=(255, 0, 0))
        self.graphWidget = self.ui.graphicsView.plot(self.generating_ecg, pen=pen)

    def ecg_pulse(self):
        processed_ecg = nk.ecg_process(self.generating_ecg, sampling_rate=2300)
        pulse = processed_ecg[0]["ECG_Rate"][1]
        self.ui.pulse.setText(str(pulse))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
