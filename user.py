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

  def save_to_file(self):
    with open('{user}.txt'.format(user = self.name), 'w') as f:
      f.write('{user}\n'.format(user = self.name))

      for movie in self.movies:
        f.write(
          '{name}, {genre}, {watched}\n'.format(name = movie.name, genre = movie.genre, watched = str(movie.watched))
        )

  @classmethod
  def read_file(cls, filename):
    # cls stands for class. The method
    with open(filename, 'r') as f:
      content = f.readlines()
      user_name = content[0]
      movies = []

      for line in content[1:]: # this will start at index 1 ending at the last element
        movie_data = line.split(', ')

        movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == True))
      
      user = cls(user_name)
      user.movies = movies
      return user
