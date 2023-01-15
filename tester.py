import sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QWidget,
    QMainWindow,
    QLabel,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QErrorMessage,
    QMessageBox,
)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.status_bar = self.statusBar()
        self.setWindowTitle("Dale Project")
        self.setGeometry(300, 300, 480, 360)
        self.setContentsMargins(20, 20, 20, 10)
        self.button_team_set = QPushButton("Team Set", self)
        self.button_open_file = QPushButton("Open File", self)
        self.button_start = QPushButton("Start", self)
        self.input_box = QLineEdit(self)
        self._init_ui()
        self._init_util()
        self._init_data()

    def _init_ui(self):
        # Set Status Bar
        self.status_bar.showMessage("Random Lunch Program")

        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout(widget)
        # Set Button
        grid.addWidget(
            self.button_team_set, 0, 2, 0, 2,
            QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop
        )
        grid.addWidget(
            self.button_open_file, 0, 3, 0, 2,
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignBottom
        )
        grid.addWidget(
            self.button_start, 0, 4, 0, 2,
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignBottom
        )
        # Set Input Box
        grid.addWidget(
            self.input_box, 0, 1, 0, 1,
            QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.input_box.setPlaceholderText("Input Box")

    def _init_util(self):
        self.button_team_set.clicked.connect(self.set_total_team_number)
        self.button_open_file.clicked.connect(self.open_file)
        self.input_box.returnPressed.connect(self.func)

    def _init_data(self):
        self.total_team_number = 5

    def open_file(self):
        window = QFileDialog()
        filename = window.getOpenFileName()
        print(filename)

    def set_total_team_number(self):
        try:
            print("이전", self.total_team_number)
            input_text = self.input_box.text()
            self.total_team_number = int(self.input_box.text())
            print("이후", self.total_team_number)
        except ValueError as e:
            print(e)
            error_dialog = QMessageBox()
            error_dialog.about(self, "에러", "숫자를 입력해주세요")
            # QErrorMessage()
            # error_dialog.showMessage("Input Number!!")

    def func(self):
        self.input.setText("Hello World")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())


# init
    # Set Size
    # self.resize(600, 240)

    # Set Label (With QWidget module)
    # label = QLabel("Random Lunch Program - PyQt6 UI")
    # layout = QGridLayout()
    # layout.addWidget(label)
    # self.setLayout(layout)
