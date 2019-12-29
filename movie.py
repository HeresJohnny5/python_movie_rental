class Movie:
  def __init__(self, name, genre):
    self.name = name
    self.genre = genre
  
  def __repr__(self):
    return '<Movie {movie_name}: {movie_genre}>'.format(movie_name = self.name, movie_genre = self.genre)
