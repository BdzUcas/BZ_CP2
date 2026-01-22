#BZ 2nd Random Password Generator
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
    
    