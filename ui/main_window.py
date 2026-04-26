from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QSplitter,
    QTabWidget,
    QWidget,
)

from PySide6.QtCore import Qt

from ui.sidebar import Sidebar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("~ MPooler ~")
        self.resize(800, 600)

        central_splitter = QSplitter(Qt.Orientation.Horizontal)
        self.setCentralWidget(central_splitter)

        self._sidebar = Sidebar()
        central_splitter.addWidget(self._sidebar)
