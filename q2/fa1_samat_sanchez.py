class Publication:
    def __init__(self, title, author):
        self._title = title
        self._author = author
    #getter mehods 
    def get_title(self):
        return self._title
    def get_author(self):
        return self._author
    #setter methods
    def set_title(self, title):
        self._title = title
    def set_author(self, author):
        self._author = author
    #displaying information
    def display_info(self):
        print("Title:",self._title)
        print("Author:",self._author)
        
class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        self._title = title
        self._author = author
        self._number_of_pages = number_of_pages
    #setter and getter methods for number of pages
    def get_number_of_pages(self):
        return self._number_of_pages
    def set_number_of_pages(self, number_of_pages):
        if number_of_pages > 0:
            self._number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive.")
    #displaying information
    def display_info(self):
        super().display_info()
        print("Number of pages:",self.get_number_of_pages())
    
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        self._title = title
        self._author = author
        self._issue_number = issue_number
    #setter and getter methods for issue number
    def get_issue_number(self):
        return self._issue_number
    def set_issue_number(self, issue_number):
        self._issue_number = issue_number
    #displaying information
    def display_info(self):
        super().display_info()
        print("Issue number:",self.get_issue_number())

pub1 = Publication("Journal of Experimental Psychology","Ratchiff, R. & Van Dongen, H.")
book1 =  Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication information: ")
pub1.display_info()

print("\nBook Information: ")
book1.set_number_of_pages(-310)
book1.display_info()

print("\nMagazine Information: ")
mag1.display_info()
