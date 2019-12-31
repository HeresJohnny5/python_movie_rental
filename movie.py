class Movie:
  def __init__(self, name, genre, watched):
    self.name = name
    self.genre = genre
    self.watched = watched
  
  def __repr__(self):
    return '<Movie {movie_name}: {movie_genre} - {movie_watched}>'.format(movie_name = self.name, movie_genre = self.genre, movie_watched = self.watched)
  
  def json(self):
    return {
      'name': self.name,
      'genre': self.genre,
      'watched': self.watched
    }
  
  @classmethod
  def from_json(cls, json_data):
    return Movie(json_data['name'], json_data['genre'], json_data['watched'])
