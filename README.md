# Movie Library Manager

- stores and manages both movies and series, including information like title, release year, genre, and number of plays
- for series, it additionally tracks the episode number and season number
- provides a play() method to increase the play count of a movie or series
- represents movies as "Title (Year)" and series as "Title SxxExx"
- stores movies and series in a unified list for easy access and filtering
- includes functions for retrieving movies or series, searching by title, generating random views, and displaying top titles by popularity
- employs object-oriented principles, including Python's multiple inheritance, to handle different media types efficiently

## Installation

1. Clone this repository to your local machine:

    `git clone https://github.com/andy111223/05.4_MovieLibrary.git`

2. Navigate to the project directory:

    `cd 05.4_MovieLibrary`

3. Run the script:

    `python3 movieLibrary.py`

## Usage

1. Add movies and series to the library by creating instances of Movie and Series classes, providing attributes such as title, release year, genre, and play count.

2. Use the play() method on any movie or series object to increment its play count by 1.

3. Access the library using the get_movies() and get_series() functions to retrieve only movies or only series, sorted alphabetically.

4. Use the search() function to find a movie or series by its title.

5. Generate random views for library items using the generate_views() function, which randomly adds between 1 and 100 views to a movie or series.

6. Call top_titles() to retrieve the most popular titles, with an optional parameter to filter by content type (movies or series).

## Requirements

- Python 3 (tested on Python 3.12)
- random module (part of Python standard library)
- datetime module (part of Python standard library)