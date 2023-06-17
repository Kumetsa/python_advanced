def movie_organizer(*movies):
    movies_by_genre = {}

    result = []

    for movie in movies:
        if movie[1] not in movies_by_genre:
            movies_by_genre[movie[1]] = []
        movies_by_genre[movie[1]].append(movie[0])

    # Sort titles by number movies and equal numbers by alphabetical order
    movies_by_genre = dict(sorted(movies_by_genre.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    # Sort movies within each genre alphabetically
    for genre, movies in movies_by_genre.items():
        movies_by_genre[genre] = sorted(movies)

    # Print the result
    for genre, movies in movies_by_genre.items():
        result.append(f"{genre} - {len(movies)}")
        for movie in movies:
            result.append(f"* {movie}")

    return "\n".join(result)


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
