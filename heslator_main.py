import sys
from PySide6.QtWidgets import QApplication
from heslator_window import Heslator

# import os


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Heslator()
    window.show()
    sys.exit(app.exec())
