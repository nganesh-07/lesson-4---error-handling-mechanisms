valid = False

while not valid:
    try:
        x = int(input("Enter an even number:"))
        while x%2 == 0:
            print("yes")
        valid = True
    except ValueError:
        print("Invalid response.")