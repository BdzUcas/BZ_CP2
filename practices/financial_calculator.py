#BZ 2nd Financial Calculiator
#Number input function (prompt (default "> "), error (default "Please input a number!"), max (default 1000000000000000000000000000000000000000000))
#user input function
def uinput():
    #take user input and clean it and return it
    return input().strip()
def numInput(prompt = '> ', error = 'Please input a number!', max = 1000000000000000000000000000000000):
    #loop forever
    while not False:
        #set "num" variable to user input
        num = uinput()
        #if "num" is an integer:
        if num.replace('.','').isdigit():
            num = float(num)
            #if number is under max:
            if num <= max:
                #return num
                return num
            #otherwise
            else:
                #display "That's too much!"
                print('Too large!')
        #otherwise:
        else:
            #display error message
            print(error)
#get percent funtion (number, percent)
def getPercent(number, percent):
    #return number * (percent / 100)
    return number * (percent / 100)
#goal calculator function:
def goalCalculator():
    #goal = number input
    print('What is your goal?')
    goal = numInput()
    #when = choice 1 or 2
    print('When are you depositing?\n1. Weekly\n2. Monthly')
    while True:
        when = uinput()
        if when in ['1','2']:
            break
        else:
            print('Enter 1 or 2')
    #deposit = number input
    print('How much are you depositing?')
    deposit = numInput()
    #time = goal/deposit
    time = goal/deposit
    #if when = 1:
    if when == '1':
        #dipslay "It will take (time) weeks to save for your goal"
        print(f"It will take {time} weeks to save for your goal")
    #else if when = 2:
    else:
        #dipslay "It will take (time) months to save for your goal"
        print(f"It will take {time} months to save for your goal")
goalCalculator()
#compount interest function:
    #amount = number input
    #interest = number input (max 100)
    #years = number input
    #loop years * 12 times:
        #addition = get percent (number = amount, percent = interest)
        #add addition to total
    #display (after (years) years you would end with (total) dollars.)
#budget function:
    #variable income = number input
    #create empty dictionary called "categories"
    #loop number input times:
        #create a new dictionary entry with the key being a user input and the value being a number input (max 100)
    #loop through categories
        #display "(key): $(get percent (income, value))"
#sales price function:
    #price = number input
    #discount = number input(max 100)
    #display "The item is now $(get percent (price, discount))"
#tip function:
    #bill = number input
    #tip = number input (max 100)
    #tip = get percent (bill, tip)
    #display "The tip is $(tip), the total is $(tip + bill))"
#main function
    #option input function (error (default "Please choose one of the options"), options)
        #loop forever
            #set "choice" variable to user input
            #if "choice" is in options:
                #return choice
            #otherwise:
                #display error message
    #display "1. Goal Calculator
    #         2. Compound Interest Calculator
    #         3. Budget Calculator
    #         4. Sales Discount Calculator
    #         5. Tip Calculator
    #choice = option input(options: 1, 2, 3, 4, 5)
    #if choice = 1:
        #Goal calculator function
    #if choice = 2
        #Compound interest function
    #if choice = 3:
        #budget function
    #if choice = 4:
        #Sales price function
    #if choice = 5:
        #tip function
#Forever:
    #main function
