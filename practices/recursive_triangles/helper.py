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
def int_input(max = 100000,prompt='> ',min = 0):
    while True:
        num = input(prompt).strip()
        try:
            num = int(num)
        except:
            print('Input is not a number!')
            continue
        if num <= max and num >= min:
            return num
        else:
            print('Input is out of range!')