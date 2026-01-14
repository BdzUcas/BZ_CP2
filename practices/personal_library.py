#BZ 2nd Personal Library
#Create set for books
books = {}
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
    book = {'title': name,'author': author}
    #return book
    return book
#display books function
def bookDisplay(shelf):
    #loop over books
    i = 0
    for book in shelf:
        i += 1
        #display "(current book title) by (current book author)"
        print(f'{i}. {book['title'].title()} by {book['author'].title()}')
#search books function
def search(shelf):
    #query = take user input "search"
    query = uInput("Search: ")
    #create list for potential books
    potential = []
    #loop over books
    for book in shelf:
        #if current book title contains query:
        if query in book['title']:
            #add current book to potential books
            potential.append(book)
        #else if current book author contains query:
        elif query in book['author']:
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
#main function
def main():
    #display choices
    print("1. Add\n2. View\n3. Remove\n4. Search")
    #take user input for one of the choices
    choice = uInput()
    #if choice is add
        #add (book input) to books
    #otherwise if choice is view
        #display books
    #otherwise if choice is remove
        #book search
        #chosen = book select
        #if chosen is empty:
            #return to top of function
        #remove (chosen) from books
    #otherwise if choice is search
        #book search
        #display books
    #return to top of function