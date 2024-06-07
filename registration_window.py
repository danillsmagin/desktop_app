from PyQt5 import QtWidgets
from main_window import MainWindow
from registration_from_gui import Ui_RegistrationWindow
from db_patient import connect, create_table, insert_user, close_connection


class RegistrationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegistrationWindow()
        self.ui.setupUi(self)
        self.ui.next_window.setEnabled(True)
        self.ui.next_window.clicked.connect(self.register)
        self.ui.next_window.clicked.connect(self.open_main_window)
        self.username = ''
        self.user_second_name = ''
        self.user_age = 0

    def init_ui(self):
        self.setWindowTitle('Регистрация пользователя')

    def check_input_values(self):
        if not self.ui.name_user.text() or not self.ui.second_name_user.text() or not self.ui.age_user.text():
            QtWidgets.QMessageBox.warning(self, 'Внимание!', 'Не заполнены поля')

    def register(self):
        self.ui.name_user.textChanged.connect(self.update_button_enabled)

        self.username = self.ui.name_user.text()
        self.user_second_name = self.ui.second_name_user.text()
        self.user_age = self.ui.age_user.text()

        connection = connect()
        create_table(connection)
        insert_user(connection, self.username, self.user_second_name, self.user_age)
        close_connection(connection)

    def open_main_window(self):
        if not self.ui.name_user.text() or not self.ui.second_name_user.text() or not self.ui.age_user.text():
            self.ui.next_window.clicked.connect(self.check_input_values)
        else:
            self.hide()
            self.main_window = MainWindow(self.ui.name_user, self.ui.second_name_user, self.ui.age_user)
            self.main_window.show()
