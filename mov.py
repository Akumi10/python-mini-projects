
movies = [
    "Interstellar 9",
    "Inception 8",
    "The Batman 7",
    "Avatar 9",
    "Titanic 8",
    "The Godfather 10"
]


movie_names = [movie.rsplit(" ", 1)[0] for movie in movies]
print("Movie Names:", movie_names)

ratings = [movie.rsplit(" ", 1)[1] for movie in movies]
print("Ratings:", ratings)

def movies_rating(movie_names, ratings):
    return list(zip(movie_names, ratings))


combined = movies_rating(movie_names, ratings)
print("Movies with Ratings:", combined)
