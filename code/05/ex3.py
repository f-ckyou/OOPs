# Q: How can encapsulation be used to create read-only attributes?

class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    # Public method to get the title (no setter provided, making it read-only)
    def get_title(self):
        return self.__title
    
    # Public method to get the author (no setter provided, making it read-only)
    def get_author(self):
        return self.__author


# create instance
book = Book("Life", "Zoro")

# Access the title and author using getter methods
print("Title:", book.get_title())
print("Author:", book.get_author())

# Trying to modify 
