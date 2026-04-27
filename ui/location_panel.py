from PySide6.QtWidgets import (
    QWidget
)

from ui.base_collection_panel import BaseCollectionPanel


class LocationPanel(BaseCollectionPanel):

    def __init__(self):
        super().__init__()

    def _build_object_form(self) -> QWidget:
        return QWidget()

    def _clear_form(self) -> None:
        pass
    
    def _open_search_dialog(self) -> None:
        pass

    def _save(self) -> None:
        pass

    def _delete(self) -> None:
        pass

    def _populate_list(self) -> None:
        pass

    def _populate_form(self) -> None:
        pass
