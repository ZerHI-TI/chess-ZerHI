from PyQt6.QtWidgets import (
    QApplication, QMainWindow
)

from .Board import BoardWidget

class ChessMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Шахматы ZerHI")
        self.setGeometry(100, 100, 600, 650)

        central_widget = BoardWidget()
        self.setCentralWidget(central_widget)