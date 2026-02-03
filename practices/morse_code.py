#BZ 2nd Morse Code Translator
#Create tuples to store data
alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',' ','')
morse = ('.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','.----','..---','...--','....-','.....','-....','--...','---..','----.','-----','/','')
#translate character function
def translate(char):
    #if character is in alphabet
    if char in alphabet:
        #translate to morse code
        pos = alphabet.index(char)
        return morse[pos]
    #if character is in morse code
    elif char in morse:
        #translate to alphabet
        pos = morse.index(char)
        return alphabet[pos]
    #otherwise
    else:
        #error
        return 'error'
    
#validation function
def validate(string):
    #loop through string
    for char in string:
        #if character is not in alphabet or morse
        all_chars = alphabet + morse
        if not char in all_chars:
            #return false
            return False
    #return true
    return True

#translate to morse code function
def to_morse(string):
    #if string is not valid
    if not validate(string):
        #tell user to use a valid input
        return 'You can only use letters and numbers!'
    #loop through the string, translating characters and adding them to a new string with spaces inbetween
    translated = ''
    for char in string:
        translated = translated + translate(char) + ' '

    return translated

#translate to alphabet function
def to_alpha(string):
    #if string is not valid
    if not validate(string):
        #tell user to use a valid input
        return 'You can only use valid morse symbols!'
    #seperate string into a list
    string = string.split(' ')
    #loop through string list, translating characters and adding them to a new string
    translated = ''
    for char in string:
        translated = translated + translate(char)

    return translated

#menu function
def menu():
    #loop forever
    while True:
        #ask user for thing to translate
        print("Type what you would like to translate here. Use / for space in morse code.")
        to_translate = input().strip().lower()
        #if the first letter is in the alphabet
        if to_translate[0] in alphabet:
            #translate it all to morse code
            translated = to_morse(to_translate)
        #if the first letter is in morse code
        elif to_translate.split(' ')[0] in morse:
            #translate it all into the alphabet
            translated = to_alpha(to_translate)
        #if it is in neither
        else:
            #tell the user to only use english and morse characters
            print('Please use english letter or numbers or morse characters!')
        #print out the translated string
        print(translated)
        #ask user if they want to end the program
        user_chosen = input('Type exit to end program, or press ENTER to continue >')
        if user_chosen.lower() == 'exit':
            return
        
#run menu function
def main():
    print("This is a morse code translator.")
    menu()
    print('Thank you for using this morse code translator.')

main()