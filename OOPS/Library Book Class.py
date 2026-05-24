class library:

    def __init__(self,book,author):
        self.book_name = book
        self.author_name = author
        self.is_issued = False
    def issue_status(self):
        if self.is_issued:
          print("book is already issued")
        else:
            self.is_issued = True
            print("book is issued successfully")
    def return_book(self):
        if self.is_issued:
            self.is_issued = False
            print("book is returned successfully")
        else:
            print("book is not issued")

    def display_info(self):
        print("book name:",self.book_name)
        print("author:",self.author_name)
        print("issue status:",self.is_issued)

book1 = library("Gulliver's Travel","William shakespeare")
book1.issue_status()
book1.return_book()
book1.display_info()