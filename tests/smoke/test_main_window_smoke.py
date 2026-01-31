import pytest

from PySide6.QtWidgets import QMainWindow

from main_window import MainWindow


@pytest.mark.smoke
def test_main_window_constructs(app) -> None:
    """
    Ensure MainWindow can be instantiated successfully.

    Args:
        app: a QApplication pytest fixture
    """
    window = MainWindow()
    assert isinstance(window, QMainWindow)
