print("Welcome to the Number Analyzer Game!")
name = input("What is your name? ")
print()

print('Hi '+name)
xyz = int(input("Please enter an integer between 1 and 100  "))
print(xyz)
print()

# Given an integer entered by a user, perform the following conditional actions:
if xyz % 2 != 0 and xyz < 60:
    print("You entered an integer that is odd and less than 60")

elif xyz % 2 == 0 and 2 <= xyz <= 24:
    print("You entered an integer that is even and less than 25")

elif xyz % 2 == 0 and 26 <= xyz <= 60:
    print("You entered an integer that is even and between 26 and 60 inclusive")

elif xyz % 2 == 0 and xyz > 60:
    print("You entered an integer that is even and and greater than 60")

elif xyz % 2 != 0 and xyz > 60:
    print("You entered an integer that is odd and greater than 60")

elif xyz < 1 or xyz > 100:
    print("You entered an incorrect value! Please try again and enter an integer between 1 and 100")

while True:
    print("Would you like to enter another integer between 1 and 100? y/n ")
    y_n = input(" > ")
    if y_n == "n":
        print("Thank you for playing "+name + "!" " Have a nice day!")
        break
    print()

    print("Thank you for choosing to play again "+name + "!")
    xyz = int(input("Please enter an integer between 1 and 100  "))
    print(xyz)
    print()
    if xyz % 2 != 0 and xyz < 60:
        print("You entered an integer that is odd and less than 60")

    elif xyz % 2 == 0 and 2 <= xyz <= 24:
        print("You entered an integer that is even and less than 25")

    elif xyz % 2 == 0 and 26 <= xyz <= 60:
        print("You entered an integer that is even and between 26 and 60 inclusive")

    elif xyz < 1 or xyz > 100:
        print("You entered an incorrect value! Please try again and enter an integer between 1 and 100")

    elif xyz % 2 != 0 and xyz > 60:
        print("You entered an integer that is odd and greater than 60")

    elif xyz % 2 == 0 and xyz > 60:
        print("You entered an integer that is even and and greater than 60")






# need help with not allowing terminal to be able to enter anything other than y_n
