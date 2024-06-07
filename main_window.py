from PyQt5 import QtWidgets
import pyqtgraph as pg
from ecg_gui import Ui_MainWindow
import pandas as pd
from PyQt5.QtGui import QIcon, QPen, QPainter
from db_patient import connect, search_user_for_output_screen, close_connection
from registration_from_gui import Ui_RegistrationWindow


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, name_user, second_name_user, age_user):
        super().__init__()
        self.ui = Ui_RegistrationWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.graphWidget = pg.PlotWidget()
        self.init_graph()
        self.name_user_for_main_window = name_user
        self.second_name_user_for_main_window = second_name_user
        self.age_user_for_main_window = age_user
        self.time = 0
        self.data_ecg = 0

        # TODO:Add title from database on the main window

    def init_ui(self):
        self.setWindowTitle('Калькулятор пульса по ЭКГ')
        self.setWindowIcon(QIcon('static\icon_pulse.png'))
        # self.ui.btn_calc_pulse.clicked.connect(self.ecg_pulse)

    def init_graph(self):
        self.graphWidget = pd.read_csv('static/data.csv')
        time = self.graphWidget['elapsedtime']
        data_ecg = self.graphWidget['ECG']
        # self.ecg_signal = self.graphWidget(time, data_ecg)

        self.ui.graphicsView.setBackground('white')
        self.ui.graphicsView.setTitle('ECG graph(no)', color='black', size='19pt')
        style = {
            'color': 'red',
            'font-size': '16pt'
        }
        self.ui.graphicsView.setLabel('left', 'влэл', **style)
        self.ui.graphicsView.setLabel('bottom', 'sus', **style)
        pen = pg.mkPen(color=(255, 0, 0))
        self.graphWidget = self.ui.graphicsView.plot(time, data_ecg, pen=pen)

    def which_user(self):
        data = ''
        connection = connect()
        search_user_for_output_screen(connection, self.name_user_for_main_window,
                                      self.second_name_user_for_main_window, self.age_user_for_main_window, data)
        close_connection(connection)

        if data:
            data_string = ' '.join(map(str, data))

            self.ui.info_from_database.setText(data_string)

        else:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Не получилось извлечь информацию из базы данных')

    def calculate_pulse(self):
        pass
        # pulse calculate 60/dist between teeths R * coeffic
        # threshold = 0.5
        # r_peaks = []
        # processed_signal = p
        # peaks = find_peaks(data_)
