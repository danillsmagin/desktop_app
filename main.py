import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from scipy.signal import find_peaks
import neurokit2 as nk
from registration_window import RegistrationWindow
from main_window import MainWindow


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    registration_window = RegistrationWindow()
    registration_window.show()

    sys.exit(app.exec_())
