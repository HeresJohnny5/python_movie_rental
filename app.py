from user import User

user = User('John')
john_wick = user.add_movie('John Wick', 'Action')
new_star_wars = user.add_movie('No Country for Old Men', 'Western')

user.save_to_file()