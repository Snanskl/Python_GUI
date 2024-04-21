class Book():
    def __init__(self, title, author, isbn, genre, date_of_publication, publisher, number_of_pages, language, status, description, rating, number_of_copies_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.date_of_publication = date_of_publication
        self.publisher = publisher
        self.number_of_pages = number_of_pages
        self.language = language
        self.status = status
        self.description = description
        self.rating = rating    
        self.number_of_copies_available = number_of_copies_available

#---------------------------------------------GETTER METHODS---------------------------------------------
#Now we will implementing a getter methods for each feature of the book class.
#Since we have no need to change the values of the features, we will not implement setter methods.

#Feature 1: Title of the book
    def get_title(self) -> str:
        return self.title

#Feature 2: Author of the book
    def get_author(self) -> str:
        return self.author

#Feature 3: ISBN of the book
    def get_isbn(self) -> str:
        return self.isbn

#Feature 4: Genre of the book/Category
    def get_genre(self) -> str:
        return self.genre

#Feature 5: Date of publication
    def get_date_of_publication(self) -> str:
        return self.date_of_publication
    
#Feature 6: Publisher
    def get_publisher(self) -> str:
        return self.publisher

#Feature 7: Number of pages
    def get_number_of_pages(self) -> int: #type hinting to tell the function to return an integer
        return self.number_of_pages

#Feature 8: Language of the book
    def get_language(self) -> str:
        return self.language

    def get_status(self) -> str:
        return self.status

#Feature 10: Description of the book
    def get_description(self) -> str:
        return self.description

#Feature 11: Rating of the book
    def get_rating(self) -> float:#type hinting to tell the function to return a float
        return self.rating

#Feature 12: Number of copies available
    def get_number_of_copies_available(self) -> int: #type hinting to tell the function to return an integer
        return self.number_of_copies_available
    
    #---------------------------------------------SETTER METHODS---------------------------------------------
    
    #This method is actually a setter method, since we know that the status of the book can change.
#Feature 9: Status of the book
    def set_status(self, new_status : str) -> str: #this time we have str inside a method beacuse we are passing a string as an argument
        if new_status in ["Available", "Checked Out", "Lost", "Under Repair", "Not Available", "Reserved"]:
            self.status = new_status
            print(f"The status of the book has been updated to {new_status}.")
        else:
            print("Invalid status. Please enter a valid status.")
            
            
    def set_rating(self, new_rating : float) -> float:
        self.rating = new_rating
        
    
    
    
    
    
    

#we use a different method for returning string because of encapsulation rules
    def __str__(self) -> str: #-> str is a type hint that tells the function to return a string
        return f"'{self.title}' by {self.author} is a {self.genre} book published by {self.publisher} in 
        {self.date_of_publication}. It has {self.number_of_pages} pages and is written in {self.language}. 
        The book has a rating of {self.rating} and {self.number_of_copies_available} copies are available."