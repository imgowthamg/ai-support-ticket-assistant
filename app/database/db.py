import sqlite3

DB_PATH = "app/database/support.db"


def get_connection():
    return sqlite3.connect(DB_PATH)