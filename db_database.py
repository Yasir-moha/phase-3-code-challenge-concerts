import sqlite3

def get_db_connection():
    """Create a connection to the database and return the CURSOR."""
    CONN = sqlite3.connect('concerts.db')
    return CONN, CONN.cursor()

def setup_database():
    """Create the necessary tables."""
    CONN, CURSOR = get_db_connection()

    # Create the bands table
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS bands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            hometown TEXT NOT NULL
        );
    ''')

    # Create the venues table
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS venues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            city TEXT NOT NULL
        );
    ''')

    # Create the concerts table
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS concerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            band_id INTEGER,
            venue_id INTEGER,
            date TEXT,
            FOREIGN KEY (band_id) REFERENCES bands(id),
            FOREIGN KEY (venue_id) REFERENCES venues(id)
        );
    ''')

    CONN.commit()
    CONN.close()