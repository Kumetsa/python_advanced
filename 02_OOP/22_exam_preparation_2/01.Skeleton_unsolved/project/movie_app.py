from typing import List, Optional

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def _get_user_by_username(self, username: str) -> Optional[User]:
        existing_user = [u for u in self.users_collection if u.username == username]
        if existing_user:
            return existing_user[0]
        return None

    def _check_movie_owner(self, username: str, movie: Movie) -> None:
        # if not movie.owner.username == username and movie.owner in self.movies_collection:
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

    def _check_movie_uploaded(self, movie: Movie) -> bool:
        if movie in self.movies_collection:
            return True
        return False

    def register_user(self, username: str, age: int) -> str:
        existing_user = self._get_user_by_username(username)
        if existing_user:
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)

        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie) -> str:
        user = self._get_user_by_username(username)

        if not user:
            raise Exception("This user does not exist!")

        if movie.owner.username != user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        existing_movie = [m for m in self.movies_collection if m.title == movie.title]
        if existing_movie:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs) -> str:
        if not self._check_movie_uploaded(movie):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        self._check_movie_owner(username, movie)

        for key, value in kwargs.items():
            setattr(movie, key, value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie) -> str:
        if not self._check_movie_uploaded(movie):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        self._check_movie_owner(username, movie)

        self.movies_collection.remove(movie)
        user = self._get_user_by_username(username)
        user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie) -> str:
        user = self._get_user_by_username(username)

        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        already_liked = [m for m in user.movies_liked if m.title == movie.title]
        if already_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie) -> str:
        user = self._get_user_by_username(username)

        already_liked = [m for m in user.movies_liked if m.title == movie.title]
        if not already_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self) -> str:
        if not self.movies_collection:
            return "No movies found."

        sorted_movies = sorted(self.movies_collection, key=lambda m: (-m.year, m.title))
        movies_info = "\n".join(movie.details() for movie in sorted_movies)

        return movies_info

    def __str__(self):
        all_users = ", ".join(user.username for user in self.users_collection) or "No users."
        all_movies = ", ".join(movie.title for movie in self.movies_collection) or "No movies."

        return f"All users: {all_users}\nAll movies: {all_movies}"
