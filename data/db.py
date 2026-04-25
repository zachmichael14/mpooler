from pathlib import Path
import sqlite3


DATABASE_PATH = Path("data/collection.db")


def connect_to_database() -> sqlite3.Connection:
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    # Make responses dict-like
    connection.row_factory = sqlite3.Row
    # Enforce foreing key constraints. 
    # SQLite has them disabled by default for some reason
    connection.execute("PRAGMA foreign_keys = ON")
    return connection
