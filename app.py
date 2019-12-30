from user import User

import json

user = User('John')
user.add_movie('John Wick', 'Action')
user.add_movie('No Country for Old Men', 'Western')

with open('my_file.txt', 'w') as f:
  json.dump(user.json(), f)