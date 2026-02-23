import csv
#CSV to dictionary function
def read_dict_csv(file_path):
    #create empty dictionary
    finished = {}
    #open csv file in read mode
    with open(file_path, mode = 'r') as file:
        #create csv reader
        reader = csv.reader(file)
        #get first line in reader
        header = next(reader)
        #loop through reader:
        for line in reader:
            #add new line in dictionary, with the first item in the line as the key and the second as the value
            finished[line[0]] = line[1]
        #return dictionary
        return finished
    
    
#input from choices
def choice_input(choices,prompt = '> '):
    #loop forever
    while True:
        #take user input
        choice = input(prompt).strip().lower()
        #if it is a valid choice
        if choice in choices:
            #return it
            return choice
        #otherwise
        else:
            #tell the user to select a valid choice
            print('Please select a valid choice!')