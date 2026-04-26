from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QListWidget,
    QSplitter,
    QVBoxLayout,
    QWidget
)



class BaseCollectionPanel(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    
    def _build_ui(self) -> None:
        central_layout = QVBoxLayout(self)
        
        toolbar = self._build_toolbar()
        central_layout.addWidget(toolbar)

        splitter = QSplitter(Qt.Orientation.Horizontal)

        self._object_list = QListWidget()
        self._list.currentRowChanged.connnect(self._on_object_selected)
        splitter.addWidget(self._object_list)

        form_container = self._build_form_container()
        splitter.addWidget(form_container)

        central_layout.addWidget(splitter)

    def _build_toolbar(self) -> QWidget:
        pass
    
    def _build_form_container(self) -> QWidget:
        pass

    def _on_object_selected(self) -> None:
        pass
    