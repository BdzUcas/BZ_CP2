#import libraries
from time_finder import get_time
from helper import *
import re
#retrieve txt file function
def retrieve_txt(file_path):
    #open txt file
    with open(file_path,'r') as file:
        #read and return txt file
        content = file.read()
        return content
    

#get last update function
def get_last_update(file_path):
    #get updates dictionary
    updates = read_dict_csv('practices/word_counter/docs/updates.csv')
    #try to find and rerturn last update for provided file
    try:
        time = updates[file_path]
        return time
    #if there was an error
    except:
        #return "Never"
        return 'Never'
    

#write to txt file function
def txt_append(file_path,add):
    #open txt file
    with open(file_path,'a') as file:
        #write given thing to txt file
        file.write(add)
        #write newline to the txt file
        file.write('\n')


#function to check for if file exists
def check_file_path(file_path):
    #try opening the file
    try:
        with open(file_path,'r'):
            return True
    #if the file doesn't exist
    except FileNotFoundError:
        #say so
        print(f'File path {file_path} not found!')
        return False
    #if there's a different error
    except Exception as error:
        #say what error it its
        print(f'An unexpected error occured: {error}')
        return False
    
    
#word counter function
def count_words(content):
    #split the given string by spaces and new lines
    words = re.split(' |\n',content)
    #loop until there is no blank strings in the split list
    while '' in words:
        #remove the first blank string from the split list
        words.remove('')
    #return the length of the split list
    return len(words)