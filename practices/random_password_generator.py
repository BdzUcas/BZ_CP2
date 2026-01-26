#BZ 2nd Random Password Generator
#import libraries
import random as r
#integer input function
def int_input():
    #loop forever
    while not False:
        #Take input
        #if it is an integer
        try:
            #return input
            return int(input('> '))    
        #otherwise
        except:
            #tell user to input a number
            print('Please input a number!')
            continue
#yes no function
def yes_no():
    #loop forevor
    while True:
        #take user input
        choice = input('Y/N > ').lower() 
        #if user input is n
        if choice == 'n':
            #return false
            return False
        #if user input is y
        elif choice == 'y':
            #return true
            return True
        #otherwise
        else:
            #tell user to input y or n
            print('Input Y or N!')
#count function
def count(start, end):
    #count from start number to end number and put them in a list
    return list(range(start, end + 1))
#make list of ascii codes of all special characters
specials = count(33, 47) + count(58, 64) + count(91,96) + count(123,126)
#add character function
def add_character(lower_required, nums_required, special_required, up_required):
    #make list of potential characters
    potentials = []
    #if the password needs lowercase characters
    if lower_required:
        #add ascii codes of all lowercase characters to potentials
        potentials.extend(count(97,122))
    #if the password needs numbers
    if nums_required:
        #add ascii codes of all numbers to potentials
        potentials.extend(count(48,57))
    #if the password needs special characters
    if special_required:
        #add ascii codes of all special characters to potentials
        potentials.extend(specials)
    #if the password needs uppercase letters
    if up_required:
        #add ascii codes of all uppercase characters to potentials
        potentials.extend(count(65,90))
    #return a random pick from potentials
    return r.choice(potentials)
#make password function
def password_maker(lower_required, nums_required, special_required, up_required, length):
    #make an empty list for characters
    characters = []
    #repeat until the characters list is as long as the required length
    while len(characters) < length:
        #use the add character function to add a character to characters list
        characters.append(add_character(lower_required, nums_required, special_required, up_required))
    #make an empty string for password
    password = ''
    #loop through characters corresponding to the ascii ids in characters
    for char in [chr(i) for i in characters]:
        #add character to password
        password = password + char
    #return password
    return password
#main function
def main():
    #ask user what length it should be
    print('What length should it be?')
    length = int_input()
    #ask user if it needs lowercase letters
    print('Are lowercase letters required?')
    lower_required = yes_no()
    #ask user if it needs uppercase letters
    print('Are uppercase letters required?')
    up_required = yes_no()
    #ask user if it needs numbers
    print('Are numbers required?')
    nums_required = yes_no()
    #ask user if it needs special characters
    print('Are special characters required?')
    special_required = yes_no()
    #repeat 4 times
    for i in range(4):
        #make a password and print it
        print(password_maker(lower_required, nums_required, special_required, up_required, length))
#loop forevor
while True:
    #run main function
    main()
    print('Press enter to continue or type exit to end')
    choice = input.lower()
    #if user wants to exit:
    match choice:
        case 'exit':
            #exit
            break
        case _:
            pass