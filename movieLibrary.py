class Movie:
    def __init__(self, title, release_year, genre, plays=0):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.plays = plays

    def play(self):
        self.plays += 1

    def __str__(self):
        return f"{self.title} ({self.release_year})"

class Series(Movie):
    def __init__(self, season_number, episode_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season_number = season_number
        self.episode_number = episode_number

    def __str__(self):
        return f"{self.title} S{self.season_number:02d}E{self.episode_number:02d}"
    

library = []

movie_data = [
    ("Pulp Fiction", 1994, "Crime"),
    ("Inception", 2010, "Sci-Fi"),
    ("The Matrix", 1999, "Action"),
    ("Forrest Gump", 1994, "Drama"),
    ("The Godfather", 1972, "Crime")
]

series_data = [
    ("Breaking Bad", 2008, "Crime", 1, 1),
    ("Game of Thrones", 2011, "Fantasy", 1, 1),
    ("The Simpsons", 1989, "Animation", 1, 1),
    ("Stranger Things", 2016, "Sci-Fi", 1, 1),
    ("Friends", 1994, "Comedy", 1, 1)
]

for title, year, genre in movie_data:
    library.append(Movie(title, year, genre, 0))

for title, year, genre, season, episode in series_data:
    library.append(Series(season, episode, title=title, release_year=year, genre=genre, plays=0))

for item in library:
    print(item)


def get_movies():
    movies = [item for item in library if isinstance(item, Movie) and not isinstance(item, Series)]
    return sorted(movies, key=lambda movie: movie.title)

def get_series():
    series = [item for item in library if isinstance(item, Series)]
    return sorted(series, key=lambda series: series.title)

print("\nMovies:")
for movie in get_movies():
    print(movie)

print("\nSeries:")
for series in get_series():
    print(series)

def search(title):
    results = [item for item in library if item.title.lower() == title.lower()]
    if results:
        return results
    else: 
        return "No matches found."
    
# Test search()
search_result = search('Inception')
if isinstance(search_result, list):
    for item in search_result:
        print(item)
    else:
        print(search_result)


import random

def generate_views():
    item = random.choice(library)
    views = random.randint(1,100)
    item.plays += views
    print(f"{item.title} received {views} new plays. Total plays: {item.plays}")

def generate_multiple_views(times=10):
    for _ in range(times):
        generate_views()

generate_multiple_views()


def top_titles(number_of_titles, content_type=None):
    if content_type == 'movies':
        filtered_list = get_movies()
    elif content_type == 'series':
        filtered_list = get_series()
    else:
        filtered_list = library

    sorted_list = sorted(filtered_list, key=lambda item: item.plays, reverse=True)
    return sorted_list[:number_of_titles]

# Test top_titles()
top_movies = top_titles(3, 'movies')
top_sersies = top_titles(3, 'series')
top_all = top_titles(5)