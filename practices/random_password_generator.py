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
        
def count(start, end):
    return list(range(start, end + 1))
specials = count(33, 47) + count(58, 64) + count(91,96) + count(123,126)
def add_character(characters, nums_required, special_required, up_required):
    nums = 0
    special = 0
    upper = 0
    for char in characters:
        if char in count(48,57):
            nums += 1
        if char in specials:
            special += 1
        if char in count(65,90):
            upper += 1
    potentials = count(97,122)
    if nums < nums_required:
        potentials.extend(count(48,57))
    if special < special_required:
        potentials.extend(specials)
    if upper < up_required:
        potentials.extend(count(65,90))
    return r.choice(potentials)
def main():
    characters = []
    print('What length should it be?')
    length = int_input()
    print('How many uppercase letters are required?')
    up_required = int_input()
    print('How many numbers are required?')
    nums_required = int_input()
    print('How many special characters are required?')
    special_required = int_input()
    needed_len = up_required + nums_required + special_required
    if needed_len < length:
        needed_len = length
    else:
        needed_len += r.randint(0,5)
    while len(characters) < needed_len:
        characters.append(add_character(characters, nums_required, special_required, up_required))
    password = ''
    for char in [chr(i) for i in characters]: password = password + char
    print(password)
main()