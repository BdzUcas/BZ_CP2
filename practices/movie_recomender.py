#BZ 2nd Movie Recomender
import csv as csv

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
                current_line[column] = line[i]
                i += 1
            #add dictionary to list
            finished.append(current_line)
        return finished
#print anything function
def uniprint(to_print, indentation = ''):
    #get type of thing to print
    method = type(to_print)
    #if it is an integer, float, or string
    if method is int or method is str or method is float:
        #print it
        print(indentation + to_print)
    #if it is a list, tuple, or set
    elif method is list or method is tuple or method is set:
        #loop through it
        for item in to_print:
            #uniprint item
            uniprint(item, indentation)
            #print new line
            print()
    #if it is a dictionary:
    elif method is dict:
        #loop through the keys
        for key in to_print.keys():
            #get type of value
            nest_method = type(to_print[key])
            #if value is a string, float, or integer:
            if nest_method is int or nest_method is str or nest_method is float:
                #print the key and a colon followed by the value
                print(f'{indentation}{key}: {to_print[key]}')
            #otherwise:
            else:
                #print the key and a colon
                print(f'{indentation}{key}:')
                #uniprint value
                uniprint(to_print[key],indentation + ' ')
        
movies = csv_to_dictionary('practices/movies.csv')
uniprint(movies,'')