#BZ 2nd Random Password Generator
#import libraries
import random as r
def count(start, end):
    return list(range(start, end + 1))
specials = count(33, 47) + count(58, 64) + count(91,96) + count(123,126)
def add_character(characters, nums_required, special_required, up_required):
    nums = 0
    special = 0
    upper = 0
    for i in characters:
        char = ord(i)
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
    