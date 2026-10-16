class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
    #getter mehods 
    def get_title(self):
        return "Title: "+self.__title
    def get_author(self):
        return "Author: "+self.__author
    #setter methods
    def set_title(self, title):
        self.__title = title
    def set_author(self, author):
        self.__author = author
        
class Book(Publication):
    def __init__(self, title, author, number_pages):
        self.__number_of_pages = 0
    #setter and getter methods for number of pages
    def get_number_of_pages(self):
        return "Number of pages: "+self.__number_of_pages
    def set_number_of_pages(self, number_pages):
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive.")
    
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        self.__issue_number = 0
    #setter and getter methods for issue number
    def get_issue_number(self):
        return "Issue number: "+self.__issue_number
    def set_issue_number(self, issue_number):
        self.__issue_number = issue_number

pub1 = Publication("Journal of Experimental Psychology","Ratchiff, R. & Van Dongen, H.")
book1 =  Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication informaion")
pub1.display_info()

print("\nBook Information: ")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information: ")
mag1.display_info()
print(mag1.get_issue_number())
