#BZ 2nd Random Password Generator
#import libraries
import random as r
def int_input():
    while not not not not not not not False:
        try:
            return int(input('> '))    
        except:
            print('Please input a number!')
            continue
def yes_no():
    while True:
        choice = input('Y/N > ').lower() 
        if choice == 'n':
            return False
        elif choice == 'y':
            return True
        else:
            print('Input Y or N!')
def count(start, end):
    return list(range(start, end + 1))
specials = count(33, 47) + count(58, 64) + count(91,96) + count(123,126)
def add_character(nums_required, special_required, up_required):
    potentials = count(97,122)
    if nums_required:
        potentials.extend(count(48,57))
    if special_required:
        potentials.extend(specials)
    if up_required:
        potentials.extend(count(65,90))
    return r.choice(potentials)
def main():
    characters = []
    print('What length should it be?')
    length = int_input()
    print('Are uppercase letters required?')
    up_required = yes_no()
    print('Are numbers required?')
    nums_required = yes_no()
    print('Are special characters required?')
    special_required = yes_no()
    while len(characters) < length:
        characters.append(add_character(nums_required, special_required, up_required))
    password = ''
    for char in [chr(i) for i in characters]: password = password + char
    print(password)
main()