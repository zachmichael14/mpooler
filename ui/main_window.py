from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QSplitter,
    QStackedWidget,
    QWidget,
)

from ui.sidebar import Sidebar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("~ MPooler ~")
        self.resize(800, 600)

        central_splitter = QSplitter(Qt.Orientation.Horizontal)
        self.setCentralWidget(central_splitter)

        self._sidebar = Sidebar()
        self._sidebar.sig_button_clicked.connect(self._on_sidebar_change)
        central_splitter.addWidget(self._sidebar)

        self._content_area = QStackedWidget()
        central_splitter.addWidget(self._content_area)

        location_placeholder = QLabel("Location placeholder")
        self._content_area.addWidget(location_placeholder)

        card_placeholder = QLabel("Card placeholder")
        self._content_area.addWidget(card_placeholder)

        deck_placeholder = QLabel("Deck placeholder")
        self._content_area.addWidget(deck_placeholder)

        scan_placeholder = QLabel("Scan placeholder")
        self._content_area.addWidget(scan_placeholder)

        # Note: keys must match button signal string from sidebar
        self._content_panels: dict[str, QWidget] = {}
        self._content_panels["storage locations"] = location_placeholder
        self._content_panels["cards"] = card_placeholder
        self._content_panels["decks"] = deck_placeholder
        self._content_panels["scan"] = scan_placeholder

    def _on_sidebar_change(self, content_name: str) -> None:
        new_content = self._content_panels.get(content_name)

        # Prevent change if there's an error
        if new_content is not None:
            self._content_area.setCurrentWidget(new_content)