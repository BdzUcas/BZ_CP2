#BZ 2nd Financial Calclliator
#Number input function (prompt (default "> "), error (default "Please input a number!"), max (default ))
    #loop forever
        #set "num" variable to user input
        #if "num" is an integer:
            #if number is under max:
                #return num
            #otherwise
                #display "That's too much!"
        #otherwise:
            #display error message
#option input function (prompt,  (default "> "), error (defaul "Please choose one of the options", options)
    #loop forever
        #set "choice" variable to user input
        #if "choice" is in options:
            #return choice
        #otherwise:
            #display error message
#get percent funtion (number, percent)
    #return number * (percent / 100)
#goal calculator function:
    #goal = number input
    #when = choice 1 or 2
    #deposit = number input
    #time = goal/deposit
    #if when = 1:
        #dipslay "It will take (time) months to save for your goal"
    #else if when = 2:
        #dipslay "It will take (time) weeks to save for your goal"
#compount interest function:
    #amount = number input
    #interest = number input (max 100)
    #years = number input
    #loop years * 12 times:
        #addition = get percent (number = amount, percent = interest)
        #add addition to total
    #display (after (years) years you would end with (total) dollars.)
#budget function:
    #create empty list called "categories"
    #loop number input times
    