print("Welcome to the Number Analyzer Game!")
name = input("What is your name? ")
print()

print('Hi '+name)
xyz = int(input("Enter a number between 1 and 100  "))
print(xyz)
print()

# Given an integer entered by a user, perform the following conditional actions:
if xyz % 2 != 0 and xyz < 60:
    print("You entered a number that is odd and less than 60")

elif xyz % 2 == 0 and 2 <= xyz <= 24:
    print("You entered a number that is even and less than 25")

elif xyz % 2 == 0 and 26 <= xyz <= 60:
    print("You entered a number that is even and between 26 and 60 inclusive")

elif xyz % 2 == 0 and xyz > 60:
    print("You entered a number that is even and and greater than 60")

elif xyz % 2 != 0 and xyz > 60:
    print("You entered a number that is odd and greater than 60")

elif xyz < 1 or xyz > 100:
    print("You entered an incorrect value. Please try again and enter a number between 1 and 100")

while True:
    print("Would you like to enter another number between 1 and 100? y/n ")
    y_n = input(" > ")
    if y_n == "n":
        print("Thank you for playing "+name + "!" " Have a nice day!")
        break
    print()

    print("Thank you for choosing to play again "+name + "!")
    xyz = int(input("Be sure to enter a number that is between 1 and 100  "))
    print()
    if xyz % 2 != 0 and xyz < 60:
        print("You entered a number that is odd and less than 60")

    elif xyz % 2 == 0 and 2 <= xyz <= 24:
        print("You entered a number that is even and less than 25")

    elif xyz % 2 == 0 and 26 <= xyz <= 60:
        print("You entered a number that is even and between 26 and 60 inclusive")

    elif xyz % 2 == 0 and xyz > 60:
        print("You entered a number that is even and and greater than 60")

    elif xyz % 2 != 0 and xyz > 60:
        print("You entered a number that is odd and greater than 60")

    elif xyz < 1 or xyz > 100:
        print("You entered an incorrect value. Please try again and enter a number between 1 and 100")

