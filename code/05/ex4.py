# how can encapsulation protect sensitive data in a class?

class User:
    def __init__(self, username, password):
        # Encapsulated sensitive data (password)
        self.username = username
        self.__password = password
    
    # Method to check if entered password matches
    def check_password(self, password):
        return self.__password == password

# Create a user
user = User("john_doe", "my_secure_password") # data 

# Check if entered password is correct
print(user.check_password("wrong_password"))  # Output: False
print(user.check_password("my_secure_password"))  # Output: True

# Direct access to the password is not allowed
print(user.__password)  # AttributeError: 'User' object has no attribute '__password' bcoz its private
