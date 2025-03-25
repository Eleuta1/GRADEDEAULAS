from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QApplication
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Colégio Renascença")
        self.setGeometry(200, 200, 1280, 720)

        self.initUI()

    def initUI(self):
        widget = QWidget()
        layout = QVBoxLayout()

        titulo = QLabel("Welcome to Homepage")
        btn_sair = QPushButton("Sair")
        btn_sair.setFixedSize(100, 25)
        btn_sair.setIcon(QApplication.style().standardIcon(QApplication.style().SP_DialogCloseButton))
        btn_sair.clicked.connect(self.close)

        layout.addWidget(titulo)
        layout.addWidget(btn_sair)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

