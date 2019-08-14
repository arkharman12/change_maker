print("***Welcome to iStore! Before we begin, I am going to ask you a few questions***\n")

name = input("Do you mind if I ask your name? ")                                #declared a variable name
greeting = input("Hello, how you doing today(good/bad): ")                      #and greeting
greeting = greeting.lower()                                                     #converting user's input to small letters
if greeting == "good":
    print("Glad to hear that, {}!".format(name))
elif greeting == "bad":                                                         #if/elif/else statement adjusts based of user's input
    print("Sad to hear that, {}!".format(name))
else:
    print("I see, {}!".format(name))

asking = input("Did you find everything ok today in the store(y/n): ")          #declared a variable asking
asking = asking.lower()                                                         #converting to small letters
if asking == "y":
    print("Awesome!\n")                                                         #if/elif/else adjusts automatically
elif asking == "yes":
    print("Awesome!\n")
elif asking == "n":
    print("Sorry for the inconvenience, {}. We will try harder next time!\n".format(name))
elif asking == "no":
    print("Sorry for the inconvenience, {}. We will try harder next time!\n".format(name))
else:
    print("I know you find everything ok today ;)\n")

print("Items that you can buy today: \n")
print("joggers($25.99)")
print("shoes($49.49)")
print("tshirt($31.99)")                                     #printing items to the screens
print("jacket($59.99)")
print("greyhuddy($9.99) \n")

def my_i_store():                                                                                    #defining a function my_i_store
    count = 0                                                                                        #set count to 0
    total_credit = 0                                                                                 #set total_credit to 0
    coin_num = int(input("How many coins would you like to enter into iStore(enter a number): "))    #declaring a variable coin_num
    while count in range(coin_num):                                                                  #while loop begins
        coin = float(input("Enter the value of coin: $"))
        total_credit = total_credit + coin                                      #Basically this function runs based of coin_num
        count = count + 1                                                       #and stops when reaches the value of coin_num
    print("You have entered ${} for your purchases today\n".format(round(total_credit, 2)))             #it also adds money to total_credit
    print("Choose your item: \n")

    joggers = 25.99
    shoes = 49.49                                                   #declaring some variable for prices
    tshirt = 31.99
    jacket = 59.99
    greyhuddy = 9.99

    item_name = input("Enter the name of your item(joggers, tshirt etc.): ")        #this variable takes users shopping request
    item_name = item_name.lower()

    if item_name == "joggers":
        if total_credit >= joggers:
            final_credit = total_credit - joggers
            print("Congratulations! You have got Joggers for yourself")
            print("Your remaining balance is ${}".format(round(final_credit, 2)))
        else:
            print("Sorry, I can't complete this transaction because your item is worth more.")

    elif item_name == "shoes":
        if total_credit >= shoes:
            final_credit = total_credit - shoes
            print("Hurrayy! You have got Shoes for yourself")
            print("Your remaining balance is ${}".format(round(final_credit, 2)))                           #all these if/elif/else statments
        else:                                                                                               #runs according to user's input
            print("Sorry, I can't complete this transaction because your item is worth more.")

    elif item_name == "tshirt":
        if total_credit >= tshirt:
            final_credit = total_credit - tshirt
            print("Congratulations! You have got a T-shirt for yourself")
            print("Your remaining balance is ${}".format(round(final_credit, 2)))
        else:
            print("Sorry, I can't complete this transaction because your item is worth more.")

    elif item_name == "jacket":
        if total_credit >= jacket:
            final_credit = total_credit -jacket
            print("Yipppieee! You have got a Jacket for yourself")
            print("Your remaining balance is ${}".format(round(final_credit, 2)))
        else:
            print("Sorry, I can't complete this transaction because your item is worth more.")

    elif item_name == "greyhuddy":
        if total_credit >= greyhuddy:
            final_credit = total_credit - greyhuddy
            print("Congratulations! You have got a Grey huddy for yourself")
            print("Your remaining balance is ${}".format(round(final_credit, 2)))
        else:
            print("Sorry, I can't complete this transaction because your item is worth more.")

    else:
        print("We don't have that item available")

my_i_store()                                                                                             #calling the function


