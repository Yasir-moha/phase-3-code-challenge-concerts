from db_database import get_db_connection

class Band:
    def __init__(self, id, name, hometown):
        self.id = id
        self.name = name
        self.hometown = hometown
        self.conn, self.cursor = get_db_connection()

    def concerts(self):
        """Return all concerts for the band."""
        self.cursor.execute("SELECT * FROM concerts WHERE band_id = ?", (self.id,))
        return self.cursor.fetchall()

    def venues(self):
        """Return all venues where the band has performed."""
        self.cursor.execute('''
        SELECT DISTINCT venues.*
        FROM venues
        JOIN concerts ON venues.id = concerts.venue_id
        WHERE concerts.band_id = ?
        ''', (self.id,))
        return self.cursor.fetchall()

    def play_in_venue(self, venue, date):
        """Schedule a concert for the band at a specific venue."""
        self.cursor.execute("SELECT id FROM venues WHERE title = ?", (venue,))
        result = self.cursor.fetchone()
        if not result:
            print(f"Venue '{venue}' not found.")
            return
        venue_id = result[0]
        self.cursor.execute('''
        INSERT INTO concerts (band_id, venue_id, date)
        VALUES (?, ?, ?)
        ''', (self.id, venue_id, date))
        self.conn.commit()
        print(f"Concert added for '{self.name}' at '{venue}' on {date}.")

    def all_introductions(self):
        """Return a list of all introductions the band has made."""
        self.cursor.execute('''
        SELECT venues.city
        FROM concerts
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.band_id = ?
        ''', (self.id,))
        cities = self.cursor.fetchall()
        return [f"Hello {city[0]}!!!!! We are {self.name} and we're from {self.hometown}" for city in cities]

    @staticmethod
    def most_performances():
        """Return the band with the most performances."""
        conn, cursor = get_db_connection()
        cursor.execute('''
        SELECT bands.name, COUNT(concerts.id) as performance_count
        FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        GROUP BY bands.id
        ORDER BY performance_count DESC
        LIMIT 1
        ''')
        result = cursor.fetchone()
        conn.close()
        if result:
            return result[0]
        return None