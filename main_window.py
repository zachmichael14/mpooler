from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QTabWidget,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("~ MPooler ~")
        self.resize(800, 600)

        central_widget = QTabWidget(self)
        self.setCentralWidget(central_widget)

        tab_placeholder1 = QLabel("Am tab")
        central_widget.addTab(tab_placeholder1, "Placeholder")
