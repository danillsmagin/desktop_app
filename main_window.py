from PyQt5 import QtWidgets
from ecg_gui import Ui_MainWindow
from PyQt5.QtGui import QIcon
from db_patient import connect, search_user_for_output_screen, close_connection
from registration_from_gui import Ui_RegistrationWindow
from mne.io import read_raw_edf
from scipy.signal import find_peaks
import pyqtgraph as pg
import numpy as np


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, name_user, second_name_user, age_user):
        self.peaks_list = []
        super().__init__()
        self.ui = Ui_RegistrationWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.graphWidget = pg.PlotWidget()
        self.init_graph()
        self.which_user(name_user, second_name_user, age_user)
        self.name_user = name_user
        self.second_name = second_name_user
        self.age_user = age_user
        self.time = 0
        self.data_ecg = 0

    def init_ui(self):
        self.setWindowTitle('Калькулятор пульса по ЭКГ')
        self.setWindowIcon(QIcon('static\\icon_pulse.png'))
        self.ui.btn_calc_pulse.clicked.connect(self.calculate_pulse)

    def init_graph(self):
        self.graphWidget = read_raw_edf(
            'C:\\Users\\user\\PycharmProjects\\desktop_app\\static\\ECG_1.edf')
        self.graphWidget.pick_channels(['ECG I-Ref', 'ECG II-Ref'])
        self.graphWidget.load_data()
        self.ui.graphicsView.setBackground('white')
        self.data, self.times = self.graphWidget[:]
        self.data = np.squeeze(self.data)
        self.ui.graphicsView.setTitle('ECG graph', color='black', size='19pt')
        style = {
            'color': 'red',
            'font-size': '16pt'
        }
        for i, channel_data in enumerate(self.data):
            self.ui.graphicsView.setLabel('left', 'Amplitude(mV)', **style)
            self.ui.graphicsView.setLabel('bottom', 'Time(s)', **style)
            pen = pg.mkPen(color=(255, 0, 0))
            self.graphWidget = self.ui.graphicsView.plot(self.times, channel_data, pen=pen)
            self.ui.graphicsView.setXRange(0, 5)

            peaks, _ = find_peaks(channel_data, distance=150)
            self.peaks_list.append(peaks)

    def which_user(self, name_user, second_name, age_user):
        print(name_user.text(), second_name.text(), age_user.text())
        connection = connect()
        data = search_user_for_output_screen(connection, name_user.text(), second_name.text(), age_user.text())
        close_connection(connection)
        if data:
            data_string = ' '.join(map(str, data))
            self.ui.info_from_database.setText(f'Привет {data_string}')
        else:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Не получилось извлечь информацию из базы данных')

    def calculate_pulse(self):
        for i, peaks in enumerate(zip(self.peaks_list)):
            # print(self.times)
            rr_intervals = np.diff(self.times[peaks])
            mean_rr_intervals = np.mean(rr_intervals)
            heart_rate = 60.0 / mean_rr_intervals

            self.ui.pulse.setText(f'{round(heart_rate, 2)} уд/мин')
            print(heart_rate)
