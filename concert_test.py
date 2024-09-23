from db_database import get_db_connection

class Concert:
    def __init__(self, id, band_id, venue_id, date):
        self.id = id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date
        self.conn, self.cursor = get_db_connection()

    def band(self):
        """Return the band associated with the concert."""
        self.cursor.execute("SELECT * FROM bands WHERE id = ?", (self.band_id,))
        return self.cursor.fetchone()

    def venue(self):
        """Return the venue associated with the concert."""
        self.cursor.execute("SELECT * FROM venues WHERE id = ?", (self.venue_id,))
        return self.cursor.fetchone()

    def hometown_show(self):
        """Return True if the concert is in the band's hometown."""
        self.cursor.execute('''
        SELECT bands.hometown = venues.city
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?
        ''', (self.id,))
        result = self.cursor.fetchone()
        return result[0] == 1 if result else False

    def introduction(self):
        """Return the band's introduction for this concert."""
        self.cursor.execute('''
        SELECT bands.name, bands.hometown, venues.city
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?
        ''', (self.id,))
        row = self.cursor.fetchone()
        if row:
            band_name, band_hometown, venue_city = row
            return f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"
        return ""