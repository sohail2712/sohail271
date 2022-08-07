import pyttsx3 
lms=pyttsx3.init('sapi5')
voices=lms.getProperty('voices')
lms.setProperty('voice',voices[1].id)
from time import sleep


class Library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks

    def displayAvailableBooks(self):
        lms.say('Books present in this library are :  ')
        lms.runAndWait()
        print('Books present in this library are :  ')
        for book in self.books:
            print('\t *' + book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f' You have been issued {bookName}. Please keep it safe and return it within 30 days')
            lms.say(f' You have been issued {bookName}. Please keep it safe and return it within 30 days')
            lms.runAndWait()
            
            self.books.remove(bookName)
            return True
        else:
            print('Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available')
            return False
    def returnBook(self,bookName):
        self.books.append(bookName)
        print('Thanks for returning this book! Hope you enjoyed reading it! Have a great day ahead!')
        lms.say('Thanks for returning this book! Hope you enjoyed reading it! Have a great day ahead!')
        lms.runAndWait()

class Student:
    def requestBook(self):
        lms.say('Enter the name of the book you want to borrow: ')
        lms.runAndWait()
        self.book=input('Enter the name of the book you want to borrow: ')
        return self.book

    def returnBook(self):
        lms.say('Enter the name of the book you want to return: ')
        lms.runAndWait()
        self.book=input('Enter the name of the book you want to return: ')
        return self.book


if __name__=='__main__':
    centralLibrary=Library(['English-1','Maths-1','PPS','BEE','CAEG','HVSP','English-2','Maths-2','Python','ANDE','Aplied Physics','FIMS','IT-EWS'])
    student=Student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        lms.say("Welcome to Central Library")
        lms.runAndWait()
        print('                     Welcome to  MRCET Central Library          ')
        lms.say('Available Options are: ')
        lms.runAndWait()
        print("Available Options are: ")
        lms.say('List all the books')
        lms.runAndWait()
        print('1. List all the books')
        lms.say('Request a book')
        lms.runAndWait()
        print('2. Request a book')
        lms.say('Return a book')
        lms.runAndWait()
        print('3. Return a book')
        lms.say('Exit the library')
        lms.runAndWait()
        print('4. Exit the library')
        lms.say('Please Choose an option')
        lms.runAndWait()
        a=int(input('Please Choose an option: '))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print('Thanks for choosing Central Library! Have a great day ahead.')
            print()
            lms.say('Thanks for choosing central library have a great day ahead')
            lms.runAndWait()
            exit(sleep(5))
        else:
            lms.say('Invalid choice')
            lms.runAndWait()
            print('Invalid Choice!')
        sleep(10)

        
        