from db_database import get_db_connection

class Venue:
    def __init__(self, id, title, city):
        self.id = id
        self.title = title
        self.city = city
        self.conn, self.cursor = get_db_connection()

    def concerts(self):
        """Return all concerts at the venue."""
        self.cursor.execute("SELECT * FROM concerts WHERE venue_id = ?", (self.id,))
        return self.cursor.fetchall()

    def bands(self):
        """Return all bands that have performed at the venue."""
        self.cursor.execute('''
        SELECT DISTINCT bands.*
        FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        WHERE concerts.venue_id = ?
        ''', (self.id,))
        return self.cursor.fetchall()

    def concert_on(self, date):
        """Find the first concert on a specific date."""
        self.cursor.execute('''
        SELECT * FROM concerts
        WHERE venue_id = ? AND date = ?
        LIMIT 1
        ''', (self.id, date))
        return self.cursor.fetchone()

    def most_frequent_band(self):
        """Return the band that has performed the most at this venue."""
        self.cursor.execute('''
        SELECT bands.name, COUNT(concerts.id) as performance_count
        FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        WHERE concerts.venue_id = ?
        GROUP BY bands.id
        ORDER BY performance_count DESC
        LIMIT 1
        ''', (self.id,))
        return self.cursor.fetchone()