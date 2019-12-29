from movie import Movie
from user import User

user = User('John')
john_wick = Movie('John Wick', 'Action', True)
new_star_wars = Movie('Star Wars: Rise', 'Action', False)

user.movies.append(john_wick)
user.movies.append(new_star_wars)

# print(user)
# print(user.movies)

print(user.watched_movies())
