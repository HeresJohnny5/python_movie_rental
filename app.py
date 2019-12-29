from movie import Movie
from user import User

user = User('John')
my_movie = Movie('John Wick', 'Action')

user.movies.append(my_movie)

print(user)
print(user.movies)
