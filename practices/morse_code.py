#BZ 2nd Morse Code Translator
#Create tuples to store data
alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9',' ')
morse = ('.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','.----','..---','...--','....-','.....','-....','--...','---..','----.','-----','/')
def translate(char):
    if char in alphabet:
        pos = alphabet.index(char)
        return morse[pos]
    elif char in morse:
        pos = morse.index(char)
        return alphabet[pos]
    else:
        return 'error'
def validate(string):
    for char in string:
        all_chars = alphabet + morse
        if not char in all_chars:
            return False
    return True
def to_morse(string):
    if not validate(string):
        return 'You can only use letters and numbers!'
    translated = ''
    for char in string:
        translated = translated + translate(char) + ' '
    return translated
def to_alpha(string):
    string = string.split(' ')
    translated = ''
    for char in string:
        translated = translated + translate(char) + ''
    return translated
print(to_alpha(to_morse('jingle bells jingle bells jingle all the way')))
    