import sys
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import (
    # QLabel,
    # QErrorMessage,
    QApplication,
    QFileDialog,
    QWidget,
    QMainWindow,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QPlainTextEdit,
    QSpinBox,
)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Lunch Member Matching")
        # self.setGeometry(300, 300, 480, 360)
        self.setGeometry(200, 200, 600, 480)
        self.setContentsMargins(20, 20, 20, 10)

        self.status_bar = self.statusBar()
        self.button_open_file = QPushButton("Open File", self)
        self.file_path_box = QLineEdit(self)
        self.team_number_box = QSpinBox(self)
        self.button_team_set = QPushButton("Team Set", self)
        self.result_box = QPlainTextEdit(self)
        self.button_start = QPushButton("Start", self)
        # self.input_box = QLineEdit(self)

        self._init_ui()
        self._init_util()
        self._init_data()

    def _init_ui(self):
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout(widget)

        # File Set up
        grid.addWidget(
            self.file_path_box, 0, 0, 1, 3
            # QtCore.Qt.AlignmentFlag.AlignVCenter | QtCore.Qt.AlignmentFlag.AlignBottom
        )
        self.file_path_box.setPlaceholderText("Select file")
        grid.addWidget(
            self.button_open_file, 0, 3, 1, 1,
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        # Team Set up
        grid.addWidget(
            self.team_number_box, 1, 0, 1, 1,
            # QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        grid.addWidget(
            self.button_team_set, 1, 1, 1, 1,
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        # Result Box
        grid.addWidget(
            self.result_box, 2, 0, 3, 3,
            # QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        # Action
        grid.addWidget(
            self.button_start, 2, 3, 1, 2,
        )

        # # test
        # grid.addWidget(
        #     self.input_box, 3, 0,)

        # Set Status Bar
        self.status_bar.showMessage("made by Dale")

    def _init_util(self):
        self.team_number_box.setRange(3, 9)
        self.team_number_box.setValue(5)
        self.button_team_set.clicked.connect(self.set_total_team_number)
        self.button_open_file.clicked.connect(self.open_file)
        self.button_start.clicked.connect(self.match_team)
        self.error_dialog = QMessageBox()
        # self.input_box.returnPressed.connect(self.set_total_team_number)

    def _init_data(self):
        self.total_team_number = 5

    def open_file(self):
        window = QFileDialog()
        filename = window.getOpenFileName()
        try:
            self.file_path = filename[0]
            self.file_name = self.file_path.split("/")[-1]
            if self.file_name.split(".")[-1] != "csv":
                self.error_dialog.about(self, "파일 선택 에러", "csv 파일을 선택해주세요")
            self.file_path_box.setText(self.file_path)
        except IndexError as e:
            self.error_dialog.about(self, "알수 없는 에러", f"{e}")

    def set_total_team_number(self):
        try:
            self.total_team_number = self.team_number_box.value()
        except ValueError:
            self.error_dialog.about(self, "입력값 에러", "숫자를 입력해주세요")
            # QErrorMessage()
            # error_dialog.showMessage("Input Number!!")

    def match_team(self):
        print("start matching")
        self.error_dialog.about(self, "Work in Progress", "미완성")


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

# def func(self):
#     self.input.setText("Hello World")
