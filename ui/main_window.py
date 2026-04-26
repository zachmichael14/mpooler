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

        collection_placeholder = QLabel("Collection placeholder")
        self._content_area.addWidget(collection_placeholder)

        scan_placeholder = QLabel("Scan placeholder")
        self._content_area.addWidget(scan_placeholder)

        # Note: keys must match button signal string from sidebar
        self._content_panels: dict[str, QWidget] = {}
        self._content_panels["collection"] = collection_placeholder
        self._content_panels["scan"] = scan_placeholder


    def _on_sidebar_change(self, content_name: str) -> None:
        new_content = self._content_panels.get(content_name)

        # Prevent change if there's an error
        if new_content is not None:
            self._content_area.setCurrentWidget(new_content)