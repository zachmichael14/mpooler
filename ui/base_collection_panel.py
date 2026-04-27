from abc import abstractmethod

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QListWidget,
    QPushButton,
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

        splitter = QSplitter(Qt.Orientation.Vertical)

        self._object_list = QListWidget()
        # TODO: Connect this change to signal
        splitter.addWidget(self._object_list)

        form_container = self._build_form_container()
        splitter.addWidget(form_container)

        central_layout.addWidget(splitter)

    def _build_toolbar(self) -> QWidget:
        toolbar = QWidget()
        layout = QHBoxLayout(toolbar)

        self._create_button = QPushButton("Create")
        self._create_button.clicked.connect(self._on_create_clicked)

        self._search_button = QPushButton("Search...")
        self._search_button.clicked.connect(self._on_search_clicked)

        layout.addWidget(self._create_button)
        layout.addWidget(self._search_button)
        return toolbar
    
    def _build_form_container(self) -> QWidget:
        container = QWidget()
        layout = QVBoxLayout(container)

        object_form = self._build_object_form()
        form_buttons = self._build_form_buttons()

        layout.addWidget(object_form)
        layout.addWidget(form_buttons)
        return container
    
    def _build_form_buttons(self) -> QWidget:
        container = QWidget()
        layout = QHBoxLayout(container)

        self._save_button = QPushButton("Save")
        self._save_button.clicked.connect(self._on_save_clicked)

        self._delete_button = QPushButton("Delete")
        self._delete_button.clicked.connect(self._on_delete_clicked)

        layout.addWidget(self._save_button)
        layout.addWidget(self._delete_button)
        return container

    def _on_object_selected(self) -> None:
        self._populate_form(object)
    
    def _on_create_clicked(self) -> None:
        self._object_list.clearSelection()
        self._clear_form()        

    def _on_search_clicked(self) -> None:
        self._open_search_dialog()

    def _on_save_clicked(self) -> None:
        """
        TODO: Probably I want this method to create a confirmation dialog
        and subclasses can do any extra steps if necessary
        """
        self._save()
        self._populate_list()

    def _on_delete_clicked(self) -> None:
        """
        TODO: Probably I want this method to create a confirmation dialog
        and subclasses can do any extra steps if necessary
        """
        self._delete()
        self._populate_list()
        self._clear_form()

    @abstractmethod
    def _build_object_form(self) -> QWidget:
        raise NotImplementedError

    @abstractmethod
    def _clear_form(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def _open_search_dialog(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def _save(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def _delete(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def _populate_list(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def _populate_form(self) -> None:
        raise NotImplementedError
