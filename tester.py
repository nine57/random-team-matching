import sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QLabel,
    QGridLayout,
    QLineEdit,
    QPushButton
)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.status_bar = self.statusBar()
        self.setWindowTitle("Dale UI Project Window")
        self.setGeometry(300, 300, 480, 360)
        self.setContentsMargins(20, 20, 20, 10)
        self.button_click_me = QPushButton("Click me", self)
        self.button_open_file = QPushButton("Open File", self)
        self.input_box = QLineEdit(self)
        # Set Size
        # self.resize(600, 240)
        self.init_UI()

        # Set Label (With QWidget module)
        # label = QLabel("Random Lunch Program - PyQt6 UI")
        # layout = QGridLayout()
        # layout.addWidget(label)
        # self.setLayout(layout)
    def init_UI(self):
        # Set Status Bar
        self.status_bar.showMessage("Random Lunch Program - PyQt6 UI")

        # Set Button
        self.button_click_me.clicked.connect(self.func)

        w = QWidget()
        self.setCentralWidget(w)
        grid = QGridLayout(w)
        grid.addWidget(self.button_click_me, 0, 3, 0, 2,
                       QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignBottom)
        grid.addWidget(self.button_open_file, 0, 4, 0, 2,
                       QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignBottom)

        # Set Input Box
        grid.addWidget(self.input_box, 0, 1, 0, 1,
                       QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.input_box.setPlaceholderText("input 박스")
        self.input_box.returnPressed.connect(self.func)

    def func(self):
        print(self.input_box.text())

    # def func(self):
    #     self.input.setText("Hello World")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
