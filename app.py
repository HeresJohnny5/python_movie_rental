from user import User

import json

# user = User('John')
# user.add_movie('John Wick', 'Action')
# user.add_movie('No Country for Old Men', 'Western')

# with open('my_file.txt', 'w') as f:
#   json.dump(user.json(), f)

with open('my_file.txt', 'r') as f:
  json_data = json.load(f)
  user = User.from_json(json_data)

  print(user.json())
