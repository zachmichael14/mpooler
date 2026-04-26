from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QWidget
)


class Sidebar(QWidget):
    sig_button_clicked = Signal(str)

    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout(self)
        
        self._collection_button = QPushButton("My Collection")
        self._collection_button.setCheckable(True)
        self._collection_button.setAutoExclusive(True)
        self._collection_button.clicked.connect(self._on_collection_clicked)
        layout.addWidget(self._collection_button)

        self._scan_button = QPushButton("Card Scanner")
        self._scan_button.setCheckable(True)
        self._scan_button.setAutoExclusive(True)
        self._scan_button.clicked.connect(self._on_scan_clicked)
        layout.addWidget(self._scan_button)

    
    def _on_collection_clicked(self):
        self.sig_button_clicked.emit("collection")

    def _on_scan_clicked(self) -> None:
        self.sig_button_clicked.emit("scan")
