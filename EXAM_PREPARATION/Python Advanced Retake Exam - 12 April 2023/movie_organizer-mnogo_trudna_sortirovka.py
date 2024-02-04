def movie_organizer(*info):
    film_genres = {}
    for movie in info:
        name = movie[0]
        movie_type = movie[1]
        if movie_type not in film_genres:
            film_genres[movie_type] = []
        film_genres[movie_type].append(name)

    sorted_result = sorted(film_genres.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ''

    for genre, movie_name in sorted_result:
        sorted_movies = sorted(movie_name)
        result += f"{genre} - {len(sorted_movies)}\n"
        for name in sorted_movies:
            result += f"* {name}\n"
    return result.strip()



print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))


