from PySide6.QtWidgets import QMainWindow, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("~ MPooler ~")
        self.resize(800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
