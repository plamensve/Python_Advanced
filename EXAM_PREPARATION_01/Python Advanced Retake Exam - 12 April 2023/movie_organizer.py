def movie_organizer(*movie_info):
    movies = {}
    for movie, genre in sorted(movie_info, key=lambda q: q[1]):
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(movie)
        movies[genre].sort()

    sorted_by_len = sorted(movies.items(), key=lambda s: -len(s[1]))
    msg = ''
    for genre, name in sorted_by_len:
        msg += f"{genre} - {len(name)}\n"
        for n in name:
            msg += f"* {n}\n"

    return msg


print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))


