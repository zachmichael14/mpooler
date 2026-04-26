from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QVBoxLayout,
    QWidget
)


class Sidebar(QWidget):
    sig_button_clicked = Signal(str)
    sig_sub_option_changed = Signal(str)

    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout(self)
        
        self._collection_button = QPushButton("My Collection")
        self._collection_button.setCheckable(True)
        self._collection_button.setChecked(True) # Default first page
        self._collection_button.setAutoExclusive(True)
        self._collection_button.clicked.connect(self._on_collection_clicked)
        layout.addWidget(self._collection_button)

        self._sub_options = QListWidget()
        layout.addWidget(self._sub_options)

        locations = QListWidgetItem("Storage Locations")
        self._sub_options.addItem(locations)

        cards = QListWidgetItem("Cards")
        self._sub_options.addItem(cards)

        decks = QListWidgetItem("Decks")
        self._sub_options.addItem(decks)
        self._sub_options.currentItemChanged.connect(self._on_sub_option_changed)
        self._sub_options.setCurrentItem(locations) # Default selection

        self._scan_button = QPushButton("Card Scanner")
        self._scan_button.setCheckable(True)
        self._scan_button.setAutoExclusive(True)
        self._scan_button.clicked.connect(self._on_scan_clicked)
        layout.addWidget(self._scan_button)

    def _on_sub_option_changed(self, current_option: QListWidgetItem) -> None:
        selection = current_option.text().casefold()
        self.sig_button_clicked.emit(selection)

    def _on_collection_clicked(self) -> None:
        # Ensure main window shows currently-selected sub_option
        current_sub_option = self._sub_options.currentItem()
        self.sig_button_clicked.emit(current_sub_option.text().casefold())
        # Only show sub-options when collection mgmt is selected
        self._sub_options.setVisible(True)

    def _on_scan_clicked(self) -> None:
        self.sig_button_clicked.emit("scan")
        # only show sub-options when collection mgmt is selected
        self._sub_options.setVisible(False)
