#Multiple if statement in Python

height = int(input("What is your height? "))
Bill = 0
if height> 3:
    print("You can able to ride")
    age=int(input("What is your age? "))
    if age<12:
        Bill = 150
        print("Ticket Price is 150 Rs.")
    elif age<=18:
        Bill = 250
        print("Ticket Price is 250 Rs.")
    else:
        Bill = 500
        print("Ticket Price is 500 Rs.")


    want_photo = input("Do you want to take photo(Y/N)?")
    if want_photo == "y" or want_photo == "Y":                      #Here we use another if statement with operators
        Bill = Bill + 50

    print(f"Your total bill is {Bill}")

else:
    print("can't ride")
print("Thank You Enjoy Your Ride !!!")

