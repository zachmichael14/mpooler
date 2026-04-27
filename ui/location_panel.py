from PySide6.QtWidgets import (
    QComboBox,
    QFormLayout,
    QLineEdit,
    QWidget
)

from models.location_type import LocationType
from ui.base_collection_panel import BaseCollectionPanel



class LocationPanel(BaseCollectionPanel):

    def __init__(self):
        super().__init__()

    def _build_object_form(self) -> QWidget:
        form = QWidget()
        layout = QFormLayout(form)

        self._name = QLineEdit()
        
        self._type = QComboBox()
        for type in LocationType:
            #userData stores metadata, essentially
            self._type.addItem(type.value, userData=type)

        layout.addRow("Name", self._name)
        layout.addRow("Type", self._type)
        return form

    def _build_left_pane(self) -> QWidget:
        pass

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
