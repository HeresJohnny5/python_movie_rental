from movie import Movie
from user import User

user = User('John')
john_wick = user.add_movie('John Wick', 'Action')
new_star_wars = user.add_movie('Star Wars: Rise', 'Action')

user.delete_movie('John Wick')

print(user.movies)

# print(user.watched_movies())
