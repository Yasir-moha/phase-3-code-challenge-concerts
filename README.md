
# Concert Management System
This project is a simple Concert Management System that allows you to manage bands, venues, and concerts using a SQLite database. It provides functionalities to add concerts, retrieve information about bands and venues, and check various details related to concerts.

# Features
Manage Bands: Add and retrieve information about bands.
Manage Venues: Add and retrieve information about venues.
Concert Management: Schedule concerts, view concerts for a specific band, and check if a concert is in the band's hometown.
Performance Tracking: Retrieve the band with the most performances at a venue.
Requirements
Python 3.x
SQLite3
Setup
Clone the repository:

bash
Copy code
git clone <repository_url>
cd concert_management
Install dependencies (if any, for this example no external packages are required).

# Setup the database:
 Run the following Python script to create the necessary database tables:

python
Copy code
from db_database import setup_database
setup_database()
Create Sample Data: You can use the provided test script to create sample data:

python
Copy code
from band_test import Band
from venue_test import Venue
from concert_test import Concert

# Create sample data and add concerts
band_1 = Band(1, 'The Beatles', 'Liverpool')
band_2 = Band(2, 'The Rolling Stones', 'London')

venue_1 = Venue(1, 'Madison Square Garden', 'New York')
venue_2 = Venue(2, 'The O2 Arena', 'London')

# Add a concert
band_1.play_in_venue('Madison Square Garden', '2023-09-20')

# Retrieve and print data
print(band_1.concerts())
print(band_1.all_introductions())
Usage
Classes and Methods
Concert:

band(): Returns the band associated with the concert.
venue(): Returns the venue associated with the concert.
hometown_show(): Checks if the concert is in the band's hometown.
introduction(): Returns the band's introduction for the concert.
Band:

concerts(): Returns all concerts for the band.
venues(): Returns all venues where the band has performed.
play_in_venue(venue, date): Schedules a concert for the band at a specific venue.
all_introductions(): Returns a list of all introductions the band has made.
most_performances(): Returns the band with the most performances.
Venue:

concerts(): Returns all concerts at the venue.
bands(): Returns all bands that have performed at the venue.
concert_on(date): Finds the first concert on a specific date.
most_frequent_band(): Returns the band that has performed the most at this venue.
Contributing
Feel free to submit issues or pull requests for any enhancements or fixes.



## License
This project is open-source and available under the MIT License.





