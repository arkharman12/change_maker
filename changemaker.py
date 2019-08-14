purchase = float(input("Please, enter your purchase price here: "))     #declared variables purchase
cash = float(input("How much money do you have? "))                     #and cash
while(True):                                                            #while loop begins
    if cash < purchase:
        print ("Retry! You didn't give me enough money")                #this part ensures if user
        cash = float(input("How much money do you have? "))             #is giving me enough money

        if cash < purchase:
            print("Sorry, I can't complete this transaction")           #transaction will be canceled after
            break                                                       #the second time

    if cash >= purchase:                                                #this if statement take care of full transaction
        print("Here's your change")

        change = cash - purchase
        change_left = change * 100                                      #converting user's cash to pennies

        print("\nhundreds: ", change_left//10000)
        change_left = change_left%10000                                 #coverted $100 bill to 10,000 pennies

        print("fifties: ", change_left//5000)
        change_left = change_left%5000                                  #converted $50 bill to 5,000 pennies

        print("twenties: ", change_left//2000)                          #so on...
        change_left = change_left%2000

        print("tens: ", change_left//1000)                              #so on...
        change_left = change_left%1000

        print("fives: ", change_left//500)
        change_left = change_left%500

        print("ones: ", change_left//100)
        change_left = change_left%100

        print("quarters: ", change_left//25)
        change_left = change_left%25

        print("dimes: ", change_left//10)
        change_left = change_left%10

        print("nickels: ", change_left//5)
        change_left = change_left%5

        print("pennies: ", change_left//1)
        change_left = change_left%1

        print("\nTotal change returned: ${0:.2f}".format(change))       #prints remaining balance change to screen
    break                                                               #while loop ends
    
    
