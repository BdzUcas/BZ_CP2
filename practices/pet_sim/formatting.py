#text formatting function
def f(format, text = ''):
    formatters = { 
        'gray': "\033[30m",
        'grey': "\033[30m",
        'green': "\033[32m",
        'clear': "\033c",
        'blue': "\033[34m",
        'white': "\033[0m",
        '###': "\033[30m###\033[0m",
        'red': "\033[31m",
        'magenta': "\033[31m",
        'cyan': "\033[36m",
        'lime': "\033[92m",
        'yellow': "\033[93m",
        'light blue': "\033[94m",
        "bright red": "\033[91m"
    }
    try:
        return formatters[format] + text + "\033[0m"
    except:
        return