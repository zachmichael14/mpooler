import pytest

from PySide6.QtWidgets import QApplication

@pytest.fixture(scope="session")
def app():
    """
    Use a single instance of the app for all the test
    """
    app = QApplication().instance()
    if app == None:
        app = QApplication()

    return app

