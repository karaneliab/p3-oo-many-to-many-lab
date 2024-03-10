class Author:
    all = []
    def __init__(self,name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        self.name = name
        Author.all.append(self)
    def contracts(self):
        return[contract for contract in Contract.all if contract.author ==self]
    def books(self):
        return[contract.book for contract in Contract.all if contract.author== self]

    def sign_contract(self,book, date, royalties):
        if not isinstance(book,Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date ,str):
            raise Exception("date must be a string")
        if not isinstance(royalties,int):
            raise Exception("royalties muss be an interger")
        new_contract = Contract(self,book,date,royalties)
        return new_contract

    def total_royalties(self):
        return sum(contract.royalties for contract in Contract.all if contract.author == self)


class Book:
    all = []
    def __init__(self,title):
        if not isinstance(title,str):
            raise ValueError("Title must be a string")
        self.title = title
        Book.all.append(self)
    def contracts(self):
        """
        Returns a list of contracts associated with this book.
        """
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """
        Returns a list of authors associated with this book through contracts.
        """
        return [contract.author for contract in Contract.all if contract.book == self]

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

    def __str__(self):
        return f"Contract for '{self.book.title}' by {self.author.name}, dated {self.date}, with royalties of {self.royalties}%"
