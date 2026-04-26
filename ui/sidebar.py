from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QWidget
)


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout(self)
        
        self._collection_button = QPushButton("My Collection")
        self._collection_button.setCheckable(True)
        self._collection_button.setAutoExclusive(True)
        layout.addWidget(self._collection_button)

        self._scan_button = QPushButton("Card Scanner")
        self._scan_button.setCheckable(True)
        self._scan_button.setAutoExclusive(True)
        layout.addWidget(self._scan_button)

