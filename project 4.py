try:
    age = int(input("Enter your age here:"))
    if age%2 == 0:
        print("Age has been identified as even.")
    else:
        print("Age has been identified as odd.")
except ValueError:
    print("Invalid input. Try again!")
