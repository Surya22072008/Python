# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 17:49:43 2022

@author: ankit computer
"""
class Books:
    def _int_(self,name,author,price,date_of_released):
        self.book_name = name
        self.book_author = author
        self.book_price = price
        self.book_date_of_released = date_of_released
    def add_book(self):
        print("Name",+self.book_name)
        print("author",+self.book_author)
        print("Price of the book",+str(self.book_price))
        print("Book was published in",+str(self.book_date_of_released))
        print("Book Added")
    def book_age(self):
        age = 2022 - self.book_date_of_released
        print("Book is " + age + " years old")
        
book1 = Books("Harry Potter","J.K. Rowling",1928,1997)
book1.add_book()
book2 = Books("Diary of Wimpy kid","Jeff Kinney",700,2017)
book2.add_book()
