class book :
 
    num_book = 0   
    
    def __init__(self, p_title, p_author, p_year, p_isbn) :
        self.title = p_title
        self.author = p_author
        self.year = p_year
        self.isbn = p_isbn
        
        book.num_book = book.num_book + 1 
    
    def display_info(self) :
        print(f"""
              book details :
              Title: {self.title}
              Author: {self.author}
              Year of Edition: {self.year}
              ISNB : {self.isbn}
              """)
        
    def is_old(self) :
        current_year = 2024
        if((current_year - self.year)>=20) : 
            return False
        else : 
            return True
    
    
    def as_same_author(self, other_book) : 
        if (self.author == other_book.author)
        print("")
    @classmethod
    def get_num_books(cls):
        return cls.num_book
    @staticmethod
    def is_valid_isbn(isbn):
        if((len(isbn) == 10) or (len(isbn) ==13)) :
            print("ISBN valide")
        else :
            print("ISBN non valide")
        
print(book.get_num_books())        
print(book.num_book)  
    
book1 = book("soleil des indépendance","Amadou Kourouma",2000,"66584587555425")
book2 = book("Reflechissez et devenez riche","Napoléon hill",1937, "986545222325")    