from helper import *
from file_handling import *
from time_finder import *


#editor function
def editor(document):
    #loop forever
    while True:
        #ask user what they want to do
        print('What would you like to do?\n1. View Document\n2. Edit Document\n3. Close Document')
        choice = choice_input(['1','2','3'])
        match choice:
            #if they choose to view the document
            case '1':
                doc_content = retrieve_txt(document)
                #print the document
                print(doc_content)
                #print the word count
                print('Word count: ' + str(count_words(doc_content)))
                #print the last updated time
                print('Last updated: ' + get_last_update(document))
            #if they chose to edit the document
            case '2':
                #ask them what they would like to add to the document
                print('What would you like to add?')
                addition = input()
                #add it the end of the file
                txt_append(document,addition)
                #change when the file was last updated
                updates = read_dict_csv('practices/word_counter/docs/updates.csv')
                updates[document] = get_time()
                #write over updates file
                with open('practices/word_counter/docs/updates.csv','w',newline='') as file:
                    #create writer object
                    writer = csv.writer(file)
                    #write header
                    writer.writerow(['file','timestamp'])
                    #loop through dictionary
                    for file_path in updates.keys():
                        #write new line in csv file
                        writer.writerow([file_path,updates[file_path]])
            #if they chose to close the document
            case '3':
                #break loop
                break


#menu function
def menu():
    #loop forever
    while True:
        #ask them if they would like to quit or open another document
        print('What would you like to do?\n1. Open Document\n2. Quit')
        choice = choice_input(['1','2'])
        #if they would like to open a document
        match choice:
            case '1':
                #ask them what document they would like to open
                print('Please give the exact file path of your document:')
                file_path = input()
                #check if that file exists
                #if it doesn't
                if not check_file_path(file_path):
                    #return to top
                    continue
                #open that document in the editor
                editor(file_path)
            #if they want to quit
            case '2':
                #break loop
                break