lower = 10
upper = 50

print("Please enter a number between {} - {}".format(lower,upper))

def getNumber():
    while True :
        try:
            number = int(input("Please enter a number: "))
            while number < 10 or number > 50:
                print("\n", "You must put a number between 10 - 50")
                number = int(input("Please enter a number: "))
            break
        except ValueError:
            print("\n", "Enter a valid number")
    print("your number is", number)

getNumber()