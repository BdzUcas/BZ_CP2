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
#compound interest function:
def compoundInterest():
    #amount = number input
    print('How much are you starting with?')
    amount = numInput()
    #interest = number input (max 100)
    print('What is the interest rate?')
    interest = numInput(max= 100)
    #years = number input
    print('How many years will you leave it for?')
    years = numInput()
    #loop years * 12 times:
    for i in range(int(years * 12)):
        #addition = get percent (number = amount, percent = interest)
        addition = getPercent(amount, interest)
        #add addition to total
        amount += addition
    #display (after (years) years you would end with (total) dollars.)
    print(f'After {years} years you would have ${round(amount,2)}')
#budget function:
def budget():
    #variable income = number input
    print('What is your monthly income?')
    income = numInput()
    #create empty dictionary called "categories"
    categories = {}
    #loop number input times:
    print('How many budget categories do you want?')
    for i in range(int(numInput())):
        #create a new dictionary entry with the key being a user input and the value being a number input (max 100)
        print(f'Category {i+1}:')
        categories[uinput()] = numInput(prompt= 'What percentage of your budget is it?\n> ', max= 100)
    #loop through categories
    for category, percent in categories:
        #display "(key): $(get percent (income, value))"
        print(f'{category.upper()}: ${getPercent(income,percent)}')
budget()
#sales price function:
def salesPrice():
    #price = number input
    print('What is the normal price?')
    price = numInput()
    #discount = number input(max 100)
    print('What percent do you have off?')
    discount = numInput(max=100)
    #display "The item is now $(get percent (price, discount))"
    print(f"The item is now ${price - getPercent(price,discount)}")
#tip function:
def tip():
    #bill = number input
    print('What is the bill?')
    bill = numInput()
    #tip = number input (max 100)
    print('What percent tip are you giving?')
    tip = numInput(max=100)
    #tip_amount = get percent (bill, tip)
    tip_amount = getPercent(bill, tip)
    #display "The tip is $(tip_amount), the total is $(tip + bill))"
    print(f"The tip is ${tip_amount}, and the total is ${tip_amount + bill}")
#main function
def main():
    #option input function (error (default "Please choose one of the options"), options)
    def opInput(options,error="Please choose an option!"):
        #loop forever
        while not False:
            #set "choice" variable to user input
            choice = uinput()
            #if "choice" is in options:
            if choice in options:
                #return choice
                return choice
            #otherwise:
            else:
                #display error message
                print(error)
    #display "1. Goal Calculator
    #         2. Compound Interest Calculator
    #         3. Budget Calculator
    #         4. Sales Discount Calculator
    #         5. Tip Calculator"
    print("1. Goal Calculator\n2. Compound Interest Calculator\n3. Budget Calculator\n4. Sales Discount Calculator\n5. Tip Calculator")
    #choice = option input(options: 1, 2, 3, 4, 5)
    choice = opInput(['1','2','3','4','5'])
    #if choice = 1:
    if choice == '1':
        #Goal calculator function
        goalCalculator()
    #if choice = 2
    elif choice == '2':
        #Compound interest function
        compoundInterest()
    #if choice = 3:
    elif choice == '3':
        #budget function
        budget()
    #if choice = 4:
    elif choice == '4':
        #Sales price function
        salesPrice()
    #if choice = 5:
    elif choice == '5':
        #tip function
        tip()
#Forever:
while not False:
    #main function
    main()