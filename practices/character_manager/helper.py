import random
import csv

#text formatting function
def f(format, text = ''):
    formatters = { 
        'gray': "\033[30m",
        'grey': "\033[30m",
        'green': "\033[32m",
        'clear': "\033c",
        'blue': "\033[34m",
        'white': "\033[0m",
        '###': "\033[30m###\033[0m",
        'red': "\033[31m",
        'magenta': "\033[31m",
        'cyan': "\033[36m",
        'lime': "\033[92m",
        'yellow': "\033[93m",
        'light blue': "\033[94m",
        "bright red": "\033[91m"
    }
    try:
        return formatters[format] + str(text) + "\033[0m"
    except:
        return text
    
#user input
def uinput(prompt = '> '):
    uinput = input(prompt + '\033[34m').lower().strip()
    print(f("white"),end='')
    return uinput

def stringify(list):
    #turn every item in the given list into a string
    return [str(i).lower() for i in list]

#random chance based on chance given
def chance(chance):
    if random.random() <= chance:
        return True
    return False

#input from choices
def choice_input(choices,prompt = '> ',error = 'Please select a valid choice!'):
    #loop forever
    while True:
        #take user input
        choice = uinput(prompt)
        #if it is a valid choice
        if choice in stringify(choices):
            #return it
            return choice
        #otherwise
        else:
            #tell the user to select a valid choice
            print(error)


#number input
def int_input(prompt='> ',error = 'Input is not a number',max = 100000,min = 0):
    #loop fovever
    while True:
        #get user input
        num = uinput(prompt)
        try:
            num = float(num)
        #if it is not a number
        except:
            #tell user
            print(error)
            continue
        #if it is within range
        if num <= max and num >= min:
            #return it
            return num
        else:
            print('Input is out of range!')

#CSV to dictionary function
def csv_to_dictionary(file_path):
    try:
        with open(file_path, mode = 'r'):
            pass
    except FileNotFoundError:
        print('An error was encountered! Invalid file path.')
        return {'error': FileNotFoundError}
    except Exception as e:
        print(f"An unexpected error was encountered: {e}. ")
        return {'error': e}
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

#save dictionary to csv function
def save_csv(dic,save_to):
    try:
        with open(save_to, mode = 'r'):
            pass
    except FileNotFoundError:
        print('An error was encountered! Invalid file path.')
        return {'error': FileNotFoundError}
    except Exception as e:
        print(f"An unexpected error was encountered: {e}. ")
        return {'error': e}
    #get header info
    header = dic[0].keys()
    #open file
    with open(save_to,'w',newline='') as file:
        #create dict writer object
        writer = csv.DictWriter(file,header)
        #write header
        writer.writeheader()
        #write all rows
        writer.writerows(dic)
    
#search dictionary function
def search(dictionaries):
    #query = take user input "search"
    query = uinput("Search: ")
    #create list for potential matches
    potential = []
    #loop over list
    for dic in dictionaries:
        #loop through keys of current dictionary:
        for feild in dic.keys():
            #if potentials already contains current dictionary:
            if dic in potential:
                #break loop
                break
            #if current feild of current dictionary contains query:
            if query in str(dic[feild]).lower():
                #add current dictionary to potential dictionaries
                potential.append(dic)
    #return potentials
    return potential


#print anything function
def uniprint(to_print, indentation = ''):
    #get type of thing to print
    method = type(to_print)
    #if it is an integer or float
    if method is int or method is float:
        #print it
        print(indentation + to_print)
    elif method is str:
        #print it, removing underscores and capitalizing it
        print(indentation + to_print.capitalize().replace('_',' '))
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
                print(f'{indentation}{key.capitalize().replace('_',' ')}: \033[34m{to_print[key]}\033[0m')
            #otherwise:
            else:
                #print the key and a colon
                print(f'{indentation}{key}:')
                #uniprint value
                uniprint(to_print[key.capitalize().replace('_',' ')],indentation + ' ')

#choice from a list
def list_choice(choices,prompt = 'Choose an option:'):
    choices = stringify(choices)
    #print prompt
    print(prompt)
    #create a list with a number for each choice
    choice_ints = list(range(1,len(choices) + 1))
    #loop through that list
    for i in choice_ints:
        #print each item with its number (ie 1. Thing 1)
        print(f'{i}. {f('gray',choices[i-1].title())}')
    #get an input that is either a number assigned to an item or one of the items
    chosen = choice_input(choice_ints + choices)
    #if it was a number assigned to an item
    if chosen in stringify(choice_ints):
        #return the item that number was assigned to
        return choices[int(chosen) - 1]
    #otherwise
    else:
        #return what they chose
        return chosen