from PyQt6.QtWidgets import QApplication
import sys

from view.Board import BoardWidget

def main():
    app = QApplication(sys.argv)
    window = BoardWidget()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()