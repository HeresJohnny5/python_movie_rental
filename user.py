class User:
  def __init__(self, name):
    self.name = name
    self.movies = []

  def __repr__(self):
    # __repr__ allows you to define a string that represents the object when it gets printed out

    return '<User {user_name}>'.format(user_name = self.name)
