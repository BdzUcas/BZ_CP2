#BZ 1st Updated Personal Library
import csv as csv
import time as t


#CSV to dictionary function
def csv_to_dictionary(file_path):
    #create empty list
    finished = []
    #open csv file in read mode
    with open(file_path, mode = 'r') as file:
        #create csv reader
        reader = csv.reader(file)
        #get first line in reader
        header = next(reader)
        #loop through reader:
        for line in reader:
            #create empty dictionary
            current_line = {}
            #set iterator to 0
            i = 0
            #loop through first line:
            for column in header:
                #create new line in the dictionary with the first line value as the key and the respective line value as the value
                if line:
                    current_line[column] = line[i]
                i += 1
            #add dictionary to list
            finished.append(current_line)
        return finished
    

#user input function
def uInput(prompt = '> '):
    #take user input and clean it and return it
    return input(prompt).strip().lower()


#book input function
def bookInput():
    #name = take user input "Title: "
    name = uInput('Title: ')
    #author = take user input "Author: "
    author = uInput('Author: ')
    #display "Added (title) by (author)"
    print(f'Added {name.title()} by {author.title()}')
    #book = dictionary containing title: name and author: author
    book = {'title': name.title(), 'author': author.title()}
    #return book
    return book


#display books function
def bookDisplay(shelf):
    #loop over books
    i = 0
    for book in shelf:
        i += 1
        #display "(current book title) by (current book author)"
        print(f'{i}. {book['title']} by {book['author']}')


#search books function
def search(shelf):
    #query = take user input "search"
    query = uInput("Search: ")
    #create list for potential books
    potential = []
    #loop over books
    for book in shelf:
        #if current book title contains query:
        if query in book['title'].lower() or query in book['author'].lower():
            #add current book to potential books
            potential.append(book)
    #return potential books
    return potential


#select book function
def select(options):
    #display book options numbered
    bookDisplay(options)
    while True:
        #take user input "choose book (by number) or 0 to exit: "
        choice = uInput('Choose book (by number) or 0 to exit: ')
        #if choice is 0:
        if choice == '0':
            #exit function
            return False
        #if choice is a number
        try:
            #return book with that number
            return options[int(choice)-1]
        #otherwise:
        except:
            #ask again
            print('Please choose by number!')
            continue


#save books function
def save_books(shelf,save_to):
    #get header info
    header = shelf[0].keys()
    #open file
    with open(save_to,'w',newline='') as file:
        #create dict writer object
        writer = csv.DictWriter(file,header)
        #write header
        writer.writeheader()
        #write all rows
        writer.writerows(shelf)


#main function
def main():
    #import info from csv file
    books = csv_to_dictionary('practices/shelf.csv')
    while True:
        #display choices
        print("1. Add\n2. View\n3. Remove\n4. Search\n5. Exit")
        #take user input for one of the choices
        while True:
            choice = uInput()
            if choice in ['1','add','2','view','3','remove','4','search','5','exit']:
                break
            else:
                print('Please select one of the choices!')
        #if choice is add
        if choice in ['1','add']:
            #add (book input) to books
            books.append(bookInput())
        #otherwise if choice is view
        elif choice in ['2','view']:
            #display books
            bookDisplay(books)
        #otherwise if choice is remove
        elif choice in ['3','remove']:
            #book search
            potential = search(books)
            #chosen = book select
            chosen = select(potential)
            #if chosen is empty:
            if chosen == False:
                #return to top of function
                print('\033c')
                continue
            #remove (chosen) from books
            books.remove(chosen)
            print(f'Removed {chosen['title']} by {chosen['author']}')
        #otherwise if choice is search
        elif choice in ['4','search']:
            #book search
            searched = search(books)
            #display books
            bookDisplay(searched)
        #otherwise if choice is exit
        elif choice in ['5','exit']:
            #tell the user goodbye
            print('\033cGoodbye!')
            save_books(books,'practices/shelf.csv')
            #exit program
            return
        #return to top of function
        input('Press ENTER to Continue > ')
        print('\033c')


main()