import csv
import sys
from PyQt6.QtWidgets import (
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
    QCheckBox,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)
from data_handler import DataLoader
from error import FileTypeError


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self._init_ui()
        self._init_util()

    def _init_ui(self):
        # window
        self.setWindowTitle("Random Lunch Member Matching")
        self.setGeometry(200, 200, 600, 480)
        self.setContentsMargins(20, 20, 20, 10)
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("made by Dale")

        # component
        self.open_file_button = QPushButton("Open File", self)
        self.file_path_box = QLineEdit(self)
        self.team_number_box = QSpinBox(self)
        self.team_set_button = QPushButton("Team Set", self)
        # self.round_number_box = QSpinBox(self)
        # self.round_set_button = QPushButton("Round Set", self)
        # self.result_box = QPlainTextEdit(self)
        self.start_button = QPushButton("Start", self)
        self.save_result_button = QPushButton("Save Result", self)
        self.show_members_button = QPushButton("Show Members", self)
        # self.leader_exist_check = QCheckBox(self)
        self.error_dialog = QMessageBox()
        # self.input_box = QLineEdit(self)
        # self.member_table = QTableWidget(self)
        self.result_table = QTableWidget(self)
        self.result_table.resize(200, 200)
        self.result_table.setRowCount(7)
        self.result_table.setColumnCount(3)
        header = self.result_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        # header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

        # position
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout(widget)
        # File Select
        grid.addWidget(self.file_path_box, 0, 0, 1, 3)
        self.file_path_box.setPlaceholderText("파일을 선택해주세요")
        grid.addWidget(self.open_file_button, 0, 3, 1, 1)
        grid.addWidget(self.show_members_button, 0, 4, 1, 1)
        # Data Set up
        grid.addWidget(self.team_number_box, 1, 0, 1, 1)
        grid.addWidget(self.team_set_button, 1, 1, 1, 1)
        # grid.addWidget(self.leader_exist_check, 2, 3, 1, 1)
        # grid.addWidget(self.round_number_box, 2, 0, 1, 1)
        # grid.addWidget(self.round_set_button, 2, 1, 1, 1)
        # Action
        # grid.addWidget(self.result_box, 3, 0, 3, 3)
        # self.result_box.setPlaceholderText("랜덤 매칭 결과")
        grid.addWidget(self.result_table, 2, 0, 3, 4)
        grid.addWidget(self.start_button, 2, 4, 1, 1)
        grid.addWidget(self.save_result_button, 3, 4, 1, 1)

    def _init_util(self):
        self.open_file_button.clicked.connect(self.open_file)
        self.team_number_box.setRange(3, 9)
        self.team_number_box.setValue(5)
        self.total_team_number = 5
        self.team_set_button.clicked.connect(self.set_total_team_number)
        self.show_members_button.clicked.connect(self.set_table_by_org_member)
        # self.round_number_box.setValue(1)
        # self.round_number = 1
        # self.round_set_button.clicked.connect(self.set_round_number)
        self.start_button.clicked.connect(self.match_team)
        self.save_result_button.clicked.connect(self.save_result_to_csv_file)
        # self.input_box.returnPressed.connect(self.set_total_team_number)

    def open_file(self):
        window = QFileDialog()
        filename = window.getOpenFileName()
        try:
            self.file_path = filename[0]
            self.file_name = self.file_path.split("/")[-1]
            if self.file_name.split(".")[-1] != "csv":
                raise FileTypeError("csv 파일을 선택해주세요")
        except IndexError as e:
            self.error_dialog.about(self, "알수 없는 에러", f"{e}")
        except FileTypeError as e:
            self.error_dialog.about(self, "파일 선택 에러", f"{e}")
        else:
            self.file_path_box.setText(self.file_path)
            loader = DataLoader(self.file_path)
            print(loader.load_prev_data())

    def set_total_team_number(self):
        self.total_team_number = self.team_number_box.value()

    def set_round_number(self):
        self.round_number = self.round_number_box.value()

    def match_team(self):
        print("start matching")
        self.error_dialog.about(self, "작업 중", "미완성 영역입니다")

    def save_result_to_csv_file(self):
        print("start saving result")
        self.error_dialog.about(self, "작업 중", "미완성 영역입니다")

    def set_table_by_org_member(self):
        row = 0
        self.set_cell_with_data(row, 0, "소속")
        self.set_cell_with_data(row, 1, "구성원")
        with open("members.csv", "r") as f:
            reader = csv.reader(f)
            for line in reader:
                row += 1
                self.set_cell_with_data(row, 0, line[0])
                self.set_cell_with_data(row, 1, line[1])

    def set_cell_with_data(self, row, column, data):
        return self.result_table.setItem(row, column, QTableWidgetItem(data))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
