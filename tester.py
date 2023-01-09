import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGridLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # self.statusBar().showMessage("Waiting")

        label = QLabel('Hello PyQt6')

        layout = QGridLayout()
        layout.addWidget(label)

        self.setLayout(layout)

        self.setWindowTitle("My Test Window")
        self.setGeometry(300, 300, 320, 240)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())


# def main():
#     w = QWidget()

#     w.resize(600, 240)
#     w.setWindowTitle('달래의 테스트 프로그램')
#     w.show()

#     sys.exit(app.exec())


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main()
