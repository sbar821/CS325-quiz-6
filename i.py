# Imagine you're developing a library management system with a Library class.
# Currently, Library offers functionality for:
# ● Adding and removing books from the catalog
# ● Searching for books by title, author, or genre
# ● Borrowing and returning books for registered users
# ● Generating reports on borrowings, overdue books, and book popularity
# Question:
# WAP in which Library classes adhere to the Interface Segregation Principle (ISP).
# Consider the following issues and Name your program i.py:
# ● Not all users need all functionalities. For example, a guest user might only be
# interested in searching for books, while a librarian needs broader
# management features.
# ● Large interface can lead to tight coupling and inflexibility. Adding new
# functionalities can potentially affect all users, even those who don't need
# them.

from abc import ABC, abstractmethod
import datetime

class BookCatalog(ABC):
    @abstractmethod
    def add_book(self, book):
        pass

    @abstractmethod
    def remove_book(self, book):
        pass

    @abstractmethod
    def search_by_title(self, title):
        pass

    @abstractmethod
    def search_by_author(self, author):
        pass

    @abstractmethod
    def search_by_genre(self, genre):
        pass

class BookBorrowing(ABC):
    @abstractmethod
    def borrow_book(self, book, user):
        pass

    @abstractmethod
    def return_book(self, book, user):
        pass

class ReportGeneration(ABC):
    @abstractmethod
    def generate_borrowing_report(self):
        pass

    @abstractmethod
    def generate_overdue_report(self):
        pass

    @abstractmethod
    def generate_popularity_report(self):
        pass

class LibraryGuestInterface(BookCatalog):
    def search_by_title(self, title):
        if(isinstance(super().search_by_title(title), list)):
            return super().search_by_title(title)
        else:
            raise Exception("No books found with that title.")

    def search_by_author(self, author):
        # Implement search by author functionality
        if(type(author).__name__ == 'list'):
            result = []
            for a in author:
                result.extend(super().search_by_author(a))
            return result
        else:
            return super().search_by_author(author)

    def search_by_genre(self, genre):
        # Implement search by genre functionality
        return [b for b in self.books if genre in b.get_genres()]

class LibrarianInterface(BookCatalog, BookBorrowing, ReportGeneration):
    def add_book(self, book):
        # Implement add book functionality
        if not isinstance(self, book):
            raise TypeError('The object must be of type "Book".')
        elif book in self.books:
            print('This book already exists in the catalogue.')
        else:
            self.books.append(book)

    def remove_book(self, book):
        # Implement remove book functionality
        if(book in self.books):
            self.books.remove(book)
        else:
            raise ValueError('The specified book does not exist in the library.')

    def search_by_title(self, title):
        # Implement search by title functionality
        if(isinstance(super().search_by_title(title), list)):
            return super().search_by_title(title)
        else:
            raise Exception("No books found with that title.")

    def search_by_author(self, author):
        # Implement search by author functionality
        if(type(author).__name__ == 'list'):
            result = []
            for a in author:
                result.extend(super().search_by_author(a))
            return result
        else:
            return super().search_by_author(author)

    def search_by_genre(self, genre):
        # Implement search by genre functionality
        return [b for b in self.books if genre in b.get_genres()]

    def borrow_book(self, book, user):
        # Implement borrow book functionality
        if(user in self.users and book in self.books):
            if(not any([b for b in user.borrowed_books if b.get_id() == book.get_id()])):
                user.add_borrowed_book(book)
                book.set_available(False)
                return True
            else:
                raise Exception("User has already borrowed this book.")
        else:
            raise Exception("Either the user or the book is invalid.")

    def return_book(self, book, user):
        # Implement return book functionality
        if(user in self.users and book in user.borrowed_books):
            user.return_book(book)
            book.set_available(True)
            return True
        else:
            raise Exception("The user does not have this book borrowed or the book is invalid.")

    def generate_borrowing_report(self):
        # Implement borrowing report generation functionality
        users_with_books = {}
        for u in self.users:
            user_data = {"Name": u.getName(), "Borrowed books": len(u.borrowed_books)}
            users_with_books[u.getId()] = user_data
        return users_with_books

    def generate_overdue_report(self):
        # Implement overdue report generation functionality
        today = datetime.datetime.now()
        overdue_books = []
        for b in self.books:
            due_date = b.get_due_date()
            if(due_date < today): 
                overdue_books.append({"Title": b.getTitle(), "Author": b.getAuthor(),  
                                      "Due Date": str(due_date), "Borrower ID": b.get_borrower().getId()})
        return overdue_books

    def generate_popularity_report(self):
        most_popular_books = self.books[-10:]
        most_popular_books_report = [
            {"Title": book.getTitle(), "Number of Copies": book.getNumCopies()} for book in most_popular_books]
        return most_popular_books_report