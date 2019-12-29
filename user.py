from movie import Movie

class User:
  def __init__(self, name):
    self.name = name
    self.movies = []

  def __repr__(self):
    # __repr__ allows you to define a string that represents the object when it gets printed out

    return '<User {user_name}>'.format(user_name = self.name)
  
  def add_movie(self, name, genre):
    movie = Movie(name, genre, False)

    return self.movies.append(movie)
  
  def delete_movie(self, name):
    self.movies = list(filter(lambda movie: movie.name != name, self.movies))

  def watched_movies(self):
    watched_movies = list(filter(lambda movie: movie.watched, self.movies))

    return watched_movies