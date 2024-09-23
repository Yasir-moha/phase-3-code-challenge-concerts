# this file is for testing

from db_database import setup_database
from  band_test import Band
from venue_test import Venue
from concert_test import Concert

# Setup the database
setup_database()

# Create some sample data
band_1 = Band(1, 'The Beatles', 'Liverpool')
band_2 = Band(2, 'The Rolling Stones', 'London')

venue_1 = Venue(1, 'Madison Square Garden', 'New York')
venue_2 = Venue(2, 'The O2 Arena', 'London')

# Add a concert
band_1.play_in_venue('Madison Square Garden', '2023-09-20')

# Get concerts for a band
print(band_1.concerts())

# Get all introductions for a band
print(band_1.all_introductions())

# Check hometown show
concert_1 = Concert(1, band_1.id, venue_1.id, '2023-09-20')
print(concert_1.hometown_show())

# Get the band with the most performances
print(Band.most_performances())